"""Tests for the hardware-independent sensor-check assembly point."""

from __future__ import annotations

import contextlib
import io
import sys
import unittest
from unittest.mock import patch

from software.common.hardware_map import (
    CH_AMBIENT,
    CH_COLD,
    CH_FLOW,
    CH_HOT,
)
from software.diagnostics import sensor_check


class FakeAdc:
    """Provide deterministic grouped counts without importing Pi hardware."""

    def __init__(self) -> None:
        self.read_range_calls = 0
        self.closed = False

    def read_single(self, channel: int, /) -> int:
        raise AssertionError("A sensor snapshot must use one grouped read")

    def read_range(
        self,
        first_channel: int,
        last_channel: int,
        /,
    ) -> dict[int, int]:
        self.read_range_calls += 1
        self.requested_range = (first_channel, last_channel)
        return {
            CH_HOT: 1000,
            CH_COLD: 900,
            CH_FLOW: 800,
            CH_AMBIENT: 700,
        }

    def close(self) -> None:
        self.closed = True


class SensorCheckTest(unittest.TestCase):
    """Verify one-shot diagnostic assembly with a pure fake ADC."""

    def test_main_builds_once_prints_one_grouped_snapshot_and_closes(self) -> None:
        fake_adc = FakeAdc()
        captured_output = io.StringIO()

        with (
            patch.object(
                sensor_check,
                "build_max1238",
                return_value=fake_adc,
            ) as build_max1238,
            contextlib.redirect_stdout(captured_output),
        ):
            exit_code = sensor_check.main([])

        self.assertEqual(exit_code, 0)
        build_max1238.assert_called_once_with()
        self.assertEqual(fake_adc.read_range_calls, 1)
        self.assertEqual(fake_adc.requested_range, (CH_HOT, CH_AMBIENT))
        self.assertTrue(fake_adc.closed)
        self.assertNotIn("software.adc.max1238", sys.modules)
        self.assertNotIn("smbus2", sys.modules)

        output = captured_output.getvalue()
        for report_text in (
            "Sensor snapshot at ",
            "Raw ADC counts",
            "  hot_raw_counts    : 1000 counts",
            "  cold_raw_counts   : 900 counts",
            "  flow_raw_counts   : 800 counts",
            "  ambient_raw_counts: 700 counts",
            "Converted values",
            "  hot_temp_c        :",
            "  hot_temp_f        :",
            "  cold_temp_c       :",
            "  cold_temp_f       :",
            "  flow_gpm          :",
            "  ambient_temp_c    :",
            "  ambient_temp_f    :",
            " °C",
            " °F",
            " GPM",
        ):
            self.assertIn(report_text, output)


if __name__ == "__main__":
    unittest.main()
