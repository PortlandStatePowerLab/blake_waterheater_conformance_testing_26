"""Command-line entrypoint for the dry-run-first valve diagnostic."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from software.valve.gpio_valve_builder import build_gpio_valve
from software.valve.valve_diagnostic import MAX_PULSE_SECONDS, run_valve_diagnostic


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check the WH1 valve relay path.")
    parser.add_argument("--enable-output", action="store_true")
    parser.add_argument("--state", choices=("off", "on"), default="off")
    parser.add_argument("--pulse-seconds", type=float, default=0.25)
    args = parser.parse_args(argv)
    if not 0.0 <= args.pulse_seconds <= MAX_PULSE_SECONDS:
        parser.error("--pulse-seconds must be between 0 and 5 seconds")
    return args


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    valve = build_gpio_valve() if args.enable_output else None
    try:
        run_valve_diagnostic(
            valve=valve,
            requested_state=args.state,
            pulse_seconds=args.pulse_seconds,
        )
    finally:
        if valve is not None:
            valve.cleanup()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
