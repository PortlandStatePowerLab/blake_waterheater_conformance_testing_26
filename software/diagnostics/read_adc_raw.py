#!/usr/bin/env python3
"""Read and report MAX1238 ADC channels from the current WH1 channel map.

This diagnostic constructs and configures the station ADC, reads each mapped
sensor channel, and reports both the raw count and canonically converted input
voltage. It does not drive station outputs.
"""

# region Imports

# Enables postponed evaluation of type annotations as a Python language feature.
from __future__ import annotations

# Standard-library helpers for command-line parsing and project-root discovery.
import argparse
import sys
from pathlib import Path

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

# region Diagnostic Entry Point

# Constructs the ADC and reports raw counts and converted voltages without
# driving station outputs.
def main() -> int:
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
    args = parser.parse_args()

    print(f"ADC part: {ADC_PART}")
    print(f"I2C bus: {args.bus}")
    print(f"I2C address: 0x{args.address:02X}")
    print(
        "ADC reference voltage: "
        f"{NOMINAL_SENSOR_CONFIG.adc_reference_voltage_v:.3f} V"
    )

    adc = build_max1238(
        bus_num=args.bus,
        address=args.address,
    )

    try:
        for label, channel in CHANNELS:
            raw_counts = adc.read_single(channel)

            if raw_counts is None:
                raise RuntimeError(f"ADC returned no value for channel {channel}")

            voltage_v = adc_counts_to_voltage(raw_counts)

            print(
                f"CH{channel} {label}: "
                f"raw={raw_counts:4d} "
                f"voltage={voltage_v:.4f} V"
            )
    finally:
        adc.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# endregion Diagnostic Entry Point
