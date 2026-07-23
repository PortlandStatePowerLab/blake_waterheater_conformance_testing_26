#!/usr/bin/env python3
"""Safe ACS37800 diagnostic placeholder.

The active ACS37800 register map is not implemented in this staged tree. This
script intentionally does not guess register addresses and does not write to the
device. Use it as a clear review gate after confirming the device appears at the
expected I2C address with i2cdetect.
"""
from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from software.common.hardware_map import ACS37800_I2C_ADDR


def main() -> int:
    print("STATUS=REVIEW_REQUIRED")
    print(f"ACS37800 expected I2C address: 0x{ACS37800_I2C_ADDR:02X}")
    print("No I2C register read was attempted.")
    print("Verify ACS37800 part variant, register map, and scaling before adding reads.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
