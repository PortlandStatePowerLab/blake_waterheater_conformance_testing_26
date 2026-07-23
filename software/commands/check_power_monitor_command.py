"""Command-line entrypoint for the non-actuating ACS37800 status check."""

from software.power.power_monitor_diagnostic import print_power_monitor_status


def main() -> int:
    print_power_monitor_status()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
