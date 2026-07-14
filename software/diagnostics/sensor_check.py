#!/usr/bin/env python3
"""Read and report grouped water-heater sensor snapshots.

This diagnostic assembles the station MAX1238 and ``SensorReader`` boundaries.
It reads one snapshot by default or watches continuously when requested. It does
not configure GPIO, actuate the valve, or access the ACS37800.
"""

# region Imports

# Enables postponed evaluation of type annotations as a Python language feature.
from __future__ import annotations

# Standard-library helpers for command-line parsing, timing, and timestamps.
import argparse
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Sequence

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Concrete station ADC construction and setup from ``max1238_builder.py``.
from software.adc.max1238_builder import build_max1238

# Grouped sensor reads and canonical conversions from ``sensor_ops.py``.
from software.sensor_ops import SensorReader, SensorSnapshot

# endregion Imports

# region Diagnostic Configuration

DEFAULT_WATCH_INTERVAL_S = 1.0

# endregion Diagnostic Configuration

# region Snapshot Reporting

# Formats and prints one grouped ``snapshot`` with its local ``timestamp``.
def print_sensor_snapshot(
    snapshot: SensorSnapshot,
    timestamp: datetime,
) -> None:
    """Print one timestamped sensor snapshot with explicit names and units."""
    timestamp_text = timestamp.astimezone().isoformat(timespec="seconds")

    print(
        f"{timestamp_text} "
        f"hot_raw_counts={snapshot.hot_raw_counts} "
        f"cold_raw_counts={snapshot.cold_raw_counts} "
        f"flow_raw_counts={snapshot.flow_raw_counts} "
        f"ambient_raw_counts={snapshot.ambient_raw_counts} "
        f"hot_temp_c={snapshot.hot_temp_c:.3f} "
        f"cold_temp_c={snapshot.cold_temp_c:.3f} "
        f"flow_gpm={snapshot.flow_gpm:.3f} "
        f"ambient_temp_c={snapshot.ambient_temp_c:.3f}"
    )


# Obtains and prints one snapshot or watches at ``interval_s`` until interrupted.
def run_sensor_check(
    reader: SensorReader,
    *,
    watch: bool,
    interval_s: float,
) -> None:
    """Collect and print grouped snapshots through an injected sensor reader."""
    while True:
        sensor_snapshot = reader.get_sensor_snapshot()
        print_sensor_snapshot(sensor_snapshot, datetime.now().astimezone())

        if not watch:
            return

        time.sleep(interval_s)

# endregion Snapshot Reporting

# region Diagnostic Entry Point

# Parses diagnostic command-line options.
def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse sensor-check command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Read one grouped sensor snapshot or watch continuously."
    )
    parser.add_argument(
        "--watch",
        action="store_true",
        help="read snapshots continuously until Ctrl+C",
    )
    parser.add_argument(
        "--interval-s",
        type=float,
        default=DEFAULT_WATCH_INTERVAL_S,
        help=(
            "seconds between snapshots in watch mode, "
            f"default {DEFAULT_WATCH_INTERVAL_S}"
        ),
    )
    args = parser.parse_args(argv)

    if args.interval_s <= 0.0:
        parser.error("--interval-s must be greater than zero")

    return args


# Builds one ADC, injects it into ``SensorReader``, and owns ADC cleanup.
def main(argv: Sequence[str] | None = None) -> int:
    """Run the sensor diagnostic and close its ADC on every exit path."""
    args = parse_args(argv)
    adc = build_max1238()

    try:
        reader = SensorReader(adc)
        run_sensor_check(
            reader,
            watch=args.watch,
            interval_s=args.interval_s,
        )
    except KeyboardInterrupt:
        print("Sensor check stopped.")
    finally:
        adc.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# endregion Diagnostic Entry Point
