"""Report the verified external ACS37800 implementation boundary."""

from software.station.station_hardware_map import ACS37800_I2C_ADDR


def print_power_monitor_status() -> None:
    """Print the non-actuating WH1 power-monitor ownership status."""
    print("STATUS=VERIFIED_EXTERNAL_IMPLEMENTATION")
    print(f"ACS37800 expected I2C address: 0x{ACS37800_I2C_ADDR:02X}")
    print("No I2C register read was attempted.")
    print("Power monitoring is owned by the team power branch pending path integration.")
    print("Evidence: project_control/verification_completed/acs37800_power_path_VERIFIED_2026-07-22.md")
