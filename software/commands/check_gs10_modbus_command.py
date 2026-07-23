"""Command-line entrypoint for a read-only GS10 Modbus register check."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from software.gs10_drive.gs10_modbus_driver import read_holding_registers


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read GS10 holding registers over RS-485.")
    parser.add_argument("--port", default="/dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=9600)
    parser.add_argument("--parity", choices=("N", "E", "O"), default="N")
    parser.add_argument("--stopbits", type=int, choices=(1, 2), default=1)
    parser.add_argument("--bytesize", type=int, choices=(7, 8), default=8)
    parser.add_argument("--slave", type=int, default=1)
    parser.add_argument("--reg", type=lambda value: int(value, 0), default=0x2000)
    parser.add_argument("--count", type=int, default=1)
    parser.add_argument("--timeout", type=float, default=0.5)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        registers = read_holding_registers(
            port=args.port,
            baud=args.baud,
            parity=args.parity,
            stopbits=args.stopbits,
            bytesize=args.bytesize,
            slave=args.slave,
            register=args.reg,
            count=args.count,
            timeout=args.timeout,
        )
    except (ConnectionError, RuntimeError) as error:
        print(f"ERROR: {error}")
        return 1
    print(f"OK, client={args.slave} reg=0x{args.reg:04X} ({args.reg})->{registers}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
