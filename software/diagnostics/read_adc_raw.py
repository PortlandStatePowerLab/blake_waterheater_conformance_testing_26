#!/usr/bin/env python3
"""Read raw MAX1238 ADC values from the current WH1 channel map."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from software.adc.max1238 import Max1238
from software.common.hardware_map import (
    ADC_PART,
    ADC_VREF,
    CH_AMBIENT,
    CH_COLD,
    CH_FLOW,
    CH_FUTURE,
    CH_HOT,
)

ADC_COUNTS = 4095

CHANNELS = (
    ("hot_temp_transmitter", CH_HOT),
    ("cold_temp_transmitter", CH_COLD),
    ("flow_transmitter", CH_FLOW),
    ("future_input", CH_FUTURE),
    ("ambient_lm35", CH_AMBIENT),
)


def raw_to_voltage(raw: int) -> float:
    return (raw / ADC_COUNTS) * ADC_VREF


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read raw MAX1238 channels without driving outputs."
    )
    parser.add_argument("--bus", type=int, default=1, help="I2C bus number")
    parser.add_argument(
        "--address",
        type=lambda value: int(value, 0),
        default=0x35,
        help="MAX1238 I2C address, default 0x35",
    )
    args = parser.parse_args()

    print(f"ADC part: {ADC_PART}")
    print(f"I2C bus: {args.bus}")
    print(f"I2C address: 0x{args.address:02X}")
    print(f"ADC_VREF: {ADC_VREF:.3f} V")

    with Max1238(address=args.address, bus_num=args.bus) as adc:
        adc.setup_adc()
        for label, channel in CHANNELS:
            raw = adc.read_single(channel)
            voltage = raw_to_voltage(raw)
            print(f"CH{channel} {label}: raw={raw:4d} voltage={voltage:.4f} V")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
