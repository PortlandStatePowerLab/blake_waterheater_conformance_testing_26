#!/usr/bin/env python3
"""Read and report MAX1238 ADC channels from the current WH1 channel map.

This diagnostic constructs and configures the station ADC, reads each mapped
sensor channel, and reports both the raw count and canonically converted input
voltage. It does not drive station outputs.
"""

# region Imports

# Enables postponed evaluation of type annotations as a Python language feature.
from __future__ import annotations

# Standard-library helpers for command-line parsing, timestamps, and root discovery.
import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Sequence

# Makes the project package importable when this diagnostic runs as a script.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Concrete station ADC construction and setup from ``max1238_builder.py``.
from software.adc.max1238_builder import build_max1238

# ADC configuration and channel assignments from ``hardware_map.py``.
from software.common.hardware_map import (
    ADC_PART,
    CH_AMBIENT,
    CH_COLD,
    CH_FLOW,
    CH_FUTURE,
    CH_HOT,
    MAX1238_I2C_ADDR,
    MAX1238_I2C_BUS,
)

# Nominal ADC configuration and canonical conversion from ``sensor_conversion.py``.
from software.sensor_conversion import (
    NOMINAL_SENSOR_CONFIG,
    adc_counts_to_voltage,
)

# endregion Imports

# region Diagnostic Configuration

CHANNELS = (
    ("hot_temp_transmitter", CH_HOT),
    ("cold_temp_transmitter", CH_COLD),
    ("flow_transmitter", CH_FLOW),
    ("future_input", CH_FUTURE),
    ("ambient_lm35", CH_AMBIENT),
)

# endregion Diagnostic Configuration

# region Diagnostic Reporting

# Formats and prints one ADC raw diagnostic report.
def print_adc_raw_report(
    *,
    timestamp: datetime,
    adc_part: str,
    bus: int,
    address: int,
    reference_voltage_v: float,
    channel_readings: Sequence[tuple[str, int, int, float]],
) -> None:
    """Print one timestamped ADC raw report with explicit names and units."""
    timestamp_text = timestamp.astimezone().isoformat(timespec="seconds")

    print(
        f"ADC raw diagnostic at {timestamp_text}\n"
        "\n"
        "ADC configuration\n"
        f"  {'adc_part':<22}: {adc_part}\n"
        f"  {'i2c_bus':<22}: {bus}\n"
        f"  {'i2c_address':<22}: 0x{address:02X}\n"
        f"  {'reference_voltage_v':<22}: {reference_voltage_v:.3f} V\n"
        "\n"
        "Channel readings"
    )

    for label, channel, raw_counts, voltage_v in channel_readings:
        print(
            f"  CH{channel} {label}\n"
            f"    {'raw_counts':<18}: {raw_counts} counts\n"
            f"    {'input_voltage_v':<18}: {voltage_v:.4f} V"
        )

# endregion Diagnostic Reporting

# region Diagnostic Entry Point

# Parses diagnostic command-line options.
def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse read-adc-raw command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Read raw MAX1238 channels without driving outputs."
    )
    parser.add_argument(
        "--bus",
        type=int,
        default=MAX1238_I2C_BUS,
        help=f"I2C bus number, default {MAX1238_I2C_BUS}",
    )
    parser.add_argument(
        "--address",
        type=lambda value: int(value, 0),
        default=MAX1238_I2C_ADDR,
        help=f"MAX1238 I2C address, default 0x{MAX1238_I2C_ADDR:02X}",
    )
    return parser.parse_args(argv)

# Constructs the ADC and reports raw counts and converted voltages without
# driving station outputs.
def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    adc = build_max1238(
        bus_num=args.bus,
        address=args.address,
    )

    try:
        channel_readings: list[tuple[str, int, int, float]] = []

        for label, channel in CHANNELS:
            raw_counts = adc.read_single(channel)

            if raw_counts is None:
                raise RuntimeError(f"ADC returned no value for channel {channel}")

            voltage_v = adc_counts_to_voltage(raw_counts)
            channel_readings.append((label, channel, raw_counts, voltage_v))

        print_adc_raw_report(
            timestamp=datetime.now().astimezone(),
            adc_part=ADC_PART,
            bus=args.bus,
            address=args.address,
            reference_voltage_v=NOMINAL_SENSOR_CONFIG.adc_reference_voltage_v,
            channel_readings=channel_readings,
        )
    finally:
        adc.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# endregion Diagnostic Entry Point
