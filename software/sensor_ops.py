"""Configured sensor operations for the water-heater test station.

This module owns the boundary between the MAX1238 ADC driver and the pure
sensor-conversion functions. It loads optional JSON calibration overrides,
builds one effective conversion configuration, and caches the corresponding
temperature and flow spans for individual reads and grouped sensor snapshots.

The module performs ADC reads and converts them into station measurements. It
does not control the valve, schedule draws, print results, or write CSV files.
"""

# region Imports

# Enables postponed evaluation of type annotations as a Python language feature.
from __future__ import annotations

# Standard-library helpers for immutable data models and calibration files.
import json
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Optional

# MAX1238 ADC hardware driver ``Max1238``.
from software.adc.max1238 import Max1238

# Station sensor-channel assignments.
from software.common.hardware_map import (
    CH_AMBIENT,
    CH_COLD,
    CH_FLOW,
    CH_HOT,
)

# Sensor-conversion configuration and pure conversion helpers.
from software.sensor_conversion import (
    NOMINAL_SENSOR_CONFIG,
    SensorConversionConfig,
    adc_counts_to_voltage,
    lm35_voltage_to_temp_c,
    voltage_to_linear_loop_value,
)

# endregion Imports

# region Sensor Conversion Configuration

# Loads optional calibration values into ``SensorConversionConfig`` while retaining nominal defaults for omitted values.
def load_sensor_conversion_config(
    calibration_path: Path | None,
) -> SensorConversionConfig:
    """Load optional calibration overrides onto the nominal configuration.

    Args:
        calibration_path (Path | None): JSON calibration path. When ``None`` or absent,
            nominal conversion values are returned.

    Returns:
        Effective sensor-conversion configuration.

    Raises:
        ValueError: If an existing calibration file is malformed or contains
            invalid values.
    """
    if calibration_path is None or not calibration_path.exists():
        return NOMINAL_SENSOR_CONFIG

    # Parses the calibration file into root mapping ``calibration_data``.
    calibration_data = json.loads(
        calibration_path.read_text(encoding="utf-8")
    )
    if not isinstance(calibration_data, dict):
        raise ValueError("calibration data must be a JSON object")

    # Separates electrical values into ``electrical_overrides``.
    electrical_overrides = calibration_data.get("electrical", {})

    # Separates sensor ranges into ``sensor_overrides``.
    sensor_overrides = calibration_data.get("sensor_ranges", {})

    if not isinstance(electrical_overrides, dict):
        raise ValueError("electrical calibration data must be a JSON object")

    if not isinstance(sensor_overrides, dict):
        raise ValueError("sensor_ranges calibration data must be a JSON object")

    return replace(
        NOMINAL_SENSOR_CONFIG,
        adc_reference_voltage_v=float(
            electrical_overrides.get(
                "adc_reference_voltage_v",
                NOMINAL_SENSOR_CONFIG.adc_reference_voltage_v,
            )
        ),
        shunt_ohms=float(
            electrical_overrides.get(
                "shunt_ohms",
                NOMINAL_SENSOR_CONFIG.shunt_ohms,
            )
        ),
        temperature_min_c=float(
            sensor_overrides.get(
                "temperature_min_c",
                NOMINAL_SENSOR_CONFIG.temperature_min_c,
            )
        ),
        temperature_max_c=float(
            sensor_overrides.get(
                "temperature_max_c",
                NOMINAL_SENSOR_CONFIG.temperature_max_c,
            )
        ),
        flow_min_gpm=float(
            sensor_overrides.get(
                "flow_min_gpm",
                NOMINAL_SENSOR_CONFIG.flow_min_gpm,
            )
        ),
        flow_max_gpm=float(
            sensor_overrides.get(
                "flow_max_gpm",
                NOMINAL_SENSOR_CONFIG.flow_max_gpm,
            )
        ),
    )

# endregion Sensor Conversion Configuration

# region Sensor Data

# Holds one processed reading from each active station sensor in ``SensorSnapshot``.
@dataclass(frozen=True)
class SensorSnapshot:
    """Contains one processed reading from each active station sensor.

    Attributes:
        hot_temp_c (float): Hot-water transmitter temperature in degrees Celsius.
        cold_temp_c (float): Cold-water transmitter temperature in degrees Celsius.
        ambient_temp_c (float): PCB-mounted LM35 ambient temperature in degrees Celsius.
        flow_gpm (float): Flow transmitter reading in gallons per minute.

    Timing:
        Values are read sequentially during one ADC scan and are not physically
        simultaneous.
    """

    hot_temp_c: float
    cold_temp_c: float
    ambient_temp_c: float
    flow_gpm: float


# endregion Sensor Data

# region Scanned-Channel Lookup

# Returns one validated sensor ``channel`` value from the completed ADC scan ``channel_counts``.
def get_scanned_channel_raw(
    channel_counts: dict[int, int],
    channel: int,
) -> int:
    """Return one raw channel value from a completed ADC scan.

    Args:
        channel_counts (dict[int, int]): Mapping of ADC channel numbers to raw counts.
        channel (int): Active station sensor channel to retrieve.

    Returns:
        Raw ADC counts stored for ``channel``.

    Raises:
        ValueError: If ``channel`` is not an active sensor channel.
    """
    valid_channels = {
        CH_HOT,
        CH_COLD,
        CH_FLOW,
        CH_AMBIENT,
    }

    if channel not in valid_channels:
        raise ValueError(f"Unsupported sensor channel: {channel}")

    return channel_counts[channel]

# endregion Scanned-Channel Lookup

# region Sensor Reader

# Reads ADC channels with ``SensorReader`` and converts their values into sensor measurements.
class SensorReader:
    """Read and convert active water-heater station sensor channels.

    Args:
        adc (Optional[Max1238]): Optional existing ``Max1238`` driver. When omitted, this class
            opens its own MAX1238 connection.
        initialize_adc (bool): Configure the ADC during initialization. This should
            normally remain true for hardware operation. Tests using a fake ADC
            may set it false.
        calibration_path (Path | None): Optional JSON calibration path. When omitted or when
            the path does not exist, nominal sensor-conversion values are used.

    Resource ownership:
        A MAX1238 instance created internally is closed by :meth:`close`.
        An externally supplied ADC instance remains owned by the caller.
    """
    # region Initialization

    # Initializes ADC ownership ``_adc``, configuration ``_conversion_config``, cached spans, and optional ADC setup.
    def __init__(
        self,
        adc: Optional[Max1238] = None,
        *,
        initialize_adc: bool = True,
        calibration_path: Path | None = None,
    ) -> None:
        self._owns_adc = adc is None
        self._adc = adc if adc is not None else Max1238()

        self._conversion_config = load_sensor_conversion_config(
            calibration_path
        )
        self._temperature_span = (
            self._conversion_config.temperature_span
        )
        self._flow_span = self._conversion_config.flow_span

        if initialize_adc:
            self._adc.setup_adc()

    # endregion Initialization

    # region ADC Access

    # Reads raw ADC counts from ``self._adc`` for the specified ADC ``channel``.
    def get_adc_raw(self, channel: int) -> int:
        """Read one raw MAX1238 channel.

        Args:
            channel (int): MAX1238 analog input channel number.

        Returns:
            Raw 12-bit ADC result in counts.

        Raises:
            RuntimeError: If ``self._adc`` returns no reading.
        """
        raw_counts = self._adc.read_single(channel)
        if raw_counts is None:
            raise RuntimeError(f"MAX1238 returned no value for channel {channel}")

        return raw_counts

    # Reads raw counts from ADC ``channel`` and converts them using ``self._conversion_config``.
    def get_adc_voltage(self, channel: int) -> float:
        """Read one MAX1238 channel and convert it to volts.

        Args:
            channel (int): MAX1238 analog input channel number.

        Returns:
            ADC input voltage in volts.
        """
        channel_counts = self.get_adc_raw(channel)
        return adc_counts_to_voltage(
            channel_counts,
            self._conversion_config,
        )

    # endregion ADC Access

    # region Sensor Measurements

    # Reads hot-water voltage ``hot_voltage_v`` and converts it with ``_temperature_span``.
    def get_hot_temp_c(self) -> float:
        """Read the hot-water 4–20 mA transmitter.

        Returns:
            Hot-water temperature in degrees Celsius.

        Calibration:
            Uses the effective temperature span and electrical configuration.
        """
        hot_voltage_v = self.get_adc_voltage(CH_HOT)
        return voltage_to_linear_loop_value(
            hot_voltage_v,
            self._temperature_span,
            self._conversion_config,
        )

    # Reads cold-water voltage ``cold_voltage_v`` and converts it with ``_temperature_span``.
    def get_cold_temp_c(self) -> float:
        """Read the cold-water 4–20 mA transmitter.

        Returns:
            Cold-water temperature in degrees Celsius.

        Calibration:
            Uses the effective temperature span and electrical configuration.
        """
        cold_voltage_v = self.get_adc_voltage(CH_COLD)
        return voltage_to_linear_loop_value(
            cold_voltage_v,
            self._temperature_span,
            self._conversion_config,
        )

    # Reads flow voltage ``flow_voltage_v`` and converts it with ``_flow_span``.
    def get_flow_gpm(self) -> float:
        """Read the 4–20 mA flow transmitter.

        Returns:
            Flow rate in gallons per minute.

        Calibration:
            Uses the effective flow span and electrical configuration.
        """
        flow_voltage_v = self.get_adc_voltage(CH_FLOW)
        return voltage_to_linear_loop_value(
            flow_voltage_v,
            self._flow_span,
            self._conversion_config,
        )

    # Converts LM35 voltage ``ambient_voltage_v`` into degrees Celsius.
    def get_ambient_temp_c(self) -> float:
        """Read the PCB-mounted LM35 ambient sensor.

        Returns:
            Ambient temperature in degrees Celsius.
        """
        ambient_voltage_v = self.get_adc_voltage(CH_AMBIENT)
        return lm35_voltage_to_temp_c(
            ambient_voltage_v,
        )

    # endregion Sensor Measurements

    # region Sensor Snapshots

    # Reads all active channels into ``channel_counts`` and returns one ``SensorSnapshot``.
    def get_sensor_snapshot(self) -> SensorSnapshot:
        """Read all active sensors into one structured snapshot.

        Returns:
            ``SensorSnapshot`` containing temperature and flow measurements.

        Timing:
            The ADC (MAX1238) channels are read sequentially during one scan.
            Measurements are tightly grouped but not physically simultaneous.
        """
        channel_counts = self._adc.read_range(CH_HOT, CH_AMBIENT)

        hot_voltage_v = adc_counts_to_voltage(
            channel_counts[CH_HOT],
            self._conversion_config,
        )
        cold_voltage_v = adc_counts_to_voltage(
            channel_counts[CH_COLD],
            self._conversion_config,
        )
        flow_voltage_v = adc_counts_to_voltage(
            channel_counts[CH_FLOW],
            self._conversion_config,
        )
        ambient_voltage_v = adc_counts_to_voltage(
            channel_counts[CH_AMBIENT],
            self._conversion_config,
        )

        return SensorSnapshot(
            hot_temp_c=voltage_to_linear_loop_value(
                hot_voltage_v,
                self._temperature_span,
                self._conversion_config,
            ),
            cold_temp_c=voltage_to_linear_loop_value(
                cold_voltage_v,
                self._temperature_span,
                self._conversion_config,
            ),
            ambient_temp_c=lm35_voltage_to_temp_c(
                ambient_voltage_v
            ),
            flow_gpm=voltage_to_linear_loop_value(
                flow_voltage_v,
                self._flow_span,
                self._conversion_config,
            ),
        )

    # endregion Sensor Snapshots

    # region Resource Management

    # Closes ADC connection ``self._adc`` only when ownership flag ``self._owns_adc`` is true.
    def close(self) -> None:
        """Close the internally owned MAX1238 connection.

        Returns:
            None.

        Resource notes:
            Externally supplied ADC instances are not closed.
        """
        if self._owns_adc:
            self._adc.close()

    # Context-management methods allow ``SensorReader`` to be used in a with-statement.

    # Returns this ``SensorReader`` when entering its managed context.
    def __enter__(self) -> "SensorReader":
        """Enter a context-managed sensor-reader session.

        Returns:
            This ``SensorReader`` instance.
        """
        return self

    # Receives context exception details and closes owned ``self._adc`` resources.
    def __exit__(self, exc_type, exc, traceback) -> None:
        """Close owned hardware resources when leaving a context.

        Args:
            exc_type: Exception type raised inside the context, when present.
            exc: Exception instance raised inside the context, when present.
            traceback: Exception traceback raised inside the context, when present.

        Returns:
            None. Exceptions are not suppressed.
        """
        self.close()

    # endregion Resource Management

# endregion Sensor Reader
