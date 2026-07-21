#!/usr/bin/env python3
"""Dry-run-first GPIO17 valve relay diagnostic.

This script checks the Raspberry Pi GPIO path used to control the WH1 valve
relay. By default, it does NOT touch the GPIO hardware. It only prints what it
would do. Actual output is only enabled with --enable-output.

Safety behavior:
- Dry-run mode imports no GPIO library and drives no pins.
- Real output mode always drives the valve GPIO LOW before exiting.
- ON pulses are capped at MAX_PULSE_SECONDS to avoid accidentally holding the
  valve open too long during diagnostics.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

# Resolve the project root from this file location.
# This file is expected to live under something like:
#   software/operator_checks/valve_gpio_check.py
# parents[2] walks up to the repository root so imports work even when the
# script is launched directly.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Add the project root to Python's import search path.
# This lets you import project modules like software.common.hardware_map
# without requiring the user to install the repo as a Python package first.
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import the valve GPIO pin from the shared hardware map instead of hardcoding
# GPIO17 here. That keeps the physical pin assignment in one central location.
from software.common.hardware_map import VALVE_PIN

# Hard safety limit for commanded ON time.
# Even if the user types a larger --pulse-seconds value, argparse rejects it.
MAX_PULSE_SECONDS = 5.0


def main() -> int:
    """Run the valve relay GPIO diagnostic.

    Parses command-line arguments, optionally configures the Raspberry Pi GPIO
    pin, drives the valve relay pin HIGH or LOW, and always cleans up the pin
    before exit.

    Returns:
        int: Process exit code. Returns 0 when the diagnostic completes cleanly.

    Safety notes:
        - Default mode is dry-run only.
        - GPIO output only happens when --enable-output is present.
        - GPIO is forced LOW in the finally block so the valve is not left ON
          after the script exits or errors.
    """
    # Build the command-line interface for the script.
    parser = argparse.ArgumentParser(
        description="Check WH1 valve relay GPIO path. Dry-run unless enabled."
    )

    # Safety gate: without this flag, the script only prints what it would do.
    parser.add_argument(
        "--enable-output",
        action="store_true",
        help="actually configure and drive GPIO17",
    )

    # Desired logical relay state.
    # "on" means drive the GPIO HIGH briefly.
    # "off" means request/confirm GPIO LOW.
    parser.add_argument(
        "--state",
        choices=("off", "on"),
        default="off",
        help="requested output state when --enable-output is present",
    )

    # ON duration for pulse testing.
    # This only matters when --state on and --enable-output are both used.
    parser.add_argument(
        "--pulse-seconds",
        type=float,
        default=0.25,
        help="maximum on-time for --state on; capped at 5 seconds",
    )

    args = parser.parse_args()

    # Reject negative values and anything above the hard safety cap.
    if args.pulse_seconds < 0 or args.pulse_seconds > MAX_PULSE_SECONDS:
        parser.error("--pulse-seconds must be between 0 and 5 seconds")

    # Default safe path:
    # Do not import RPi.GPIO, do not configure the pin, and do not touch output.
    if not args.enable_output:
        print(f"[DRY-RUN] GPIO{VALVE_PIN} would be requested {args.state.upper()}.")
        print("No GPIO library was imported and no output was configured.")
        print("Re-run with --enable-output only after relay behavior is reviewed.")
        return 0

    # Import GPIO only after the user explicitly enables hardware output.
    # This keeps dry-run mode completely passive.
    import RPi.GPIO as GPIO

    # Use Broadcom GPIO numbering, not physical header pin numbering.
    # VALVE_PIN is expected to be a BCM GPIO number.
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # Configure the valve relay GPIO as an output and start LOW.
    # Starting LOW prevents a brief accidental HIGH during setup.
    GPIO.setup(VALVE_PIN, GPIO.OUT, initial=GPIO.LOW)

    try:
        if args.state == "on":
            # Energize the relay input by driving the GPIO HIGH.
            GPIO.output(VALVE_PIN, GPIO.HIGH)
            print(f"GPIO{VALVE_PIN} HIGH for {args.pulse_seconds:.2f} seconds")

            # Hold the relay ON only for the requested capped pulse duration.
            time.sleep(args.pulse_seconds)
        else:
            # OFF state intentionally does not pulse HIGH.
            # The finally block below will force LOW and clean up.
            print(f"GPIO{VALVE_PIN} LOW requested")

    finally:
        # Always return the GPIO LOW, even if an error or Ctrl+C happens while ON.
        GPIO.output(VALVE_PIN, GPIO.LOW)

        # Release this pin from RPi.GPIO control.
        # Cleaning up only VALVE_PIN avoids disturbing other GPIOs that another
        # process might be using.
        GPIO.cleanup(VALVE_PIN)
        print(f"GPIO{VALVE_PIN} LOW and cleaned up")

    return 0


if __name__ == "__main__":
    # Convert main()'s return value into the script's shell exit code.
    raise SystemExit(main())
