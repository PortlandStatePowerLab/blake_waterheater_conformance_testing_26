#!/usr/bin/env python3
"""ADC-based WH1 water draw control for the current PCB-ribbon hardware."""
from __future__ import annotations

import argparse
import atexit
import signal
import sys
import time
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from software.adc.max1238 import Max1238
from software.common.hardware_map import (
    ADC_VREF,
    CH_AMBIENT,
    CH_COLD,
    CH_FLOW,
    CH_HOT,
    VALVE_PIN,
)

ADC_MAX = 4095
R_SHUNT_OHMS = 120.0

T_MAX_C = 150.0
T_MIN_C = -50.0
Q_MAX_GPM = 10.0
Q_MIN_GPM = 0.0

MAX_RUN_MINUTES = 5.0
MIN_FLOW_GPM = 0.05
LOW_FLOW_TIMEOUT_S = 20.0
PRINT_PERIOD_S = 0.5

_gpio = None


def _load_gpio():
    global _gpio
    if _gpio is None:
        import RPi.GPIO as GPIO

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(VALVE_PIN, GPIO.OUT, initial=GPIO.LOW)
        _gpio = GPIO
    return _gpio


def _fail_safe_close() -> None:
    if _gpio is None:
        return
    try:
        _gpio.output(VALVE_PIN, _gpio.LOW)
    except Exception:
        pass


atexit.register(_fail_safe_close)


def _signal_handler(signum, frame) -> None:
    print(f"\n[!] Caught signal {signum}. Closing valve and exiting.")
    _fail_safe_close()
    sys.exit(1)


signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)


def _raw_to_voltage(raw: Optional[int]) -> float:
    if raw is None:
        return float("nan")
    return (float(raw) / ADC_MAX) * ADC_VREF


def _volt_to_span(value_v: float, span_max: float, span_min: float) -> float:
    if value_v != value_v:
        return float("nan")
    loop_current_a = max(value_v / R_SHUNT_OHMS, 0.0)
    normalized = (loop_current_a - 0.004) / 0.016
    return (normalized * (span_max - span_min)) + span_min


def read_voltage(adc: Max1238, channel: int) -> float:
    return _raw_to_voltage(adc.read_single(channel))


def read_ambient_temp_c(adc: Max1238) -> float:
    return read_voltage(adc, CH_AMBIENT) / 0.010


def read_external_temps_c(adc: Max1238) -> dict[str, float]:
    return {
        "hot": _volt_to_span(read_voltage(adc, CH_HOT), T_MAX_C, T_MIN_C),
        "cold": _volt_to_span(read_voltage(adc, CH_COLD), T_MAX_C, T_MIN_C),
    }


def read_flow_gpm(adc: Max1238) -> float:
    return _volt_to_span(read_voltage(adc, CH_FLOW), Q_MAX_GPM, Q_MIN_GPM)


def draw_water(
    target_vol_gal: float,
    *,
    enable_output: bool = False,
    max_run_minutes: float = MAX_RUN_MINUTES,
) -> float:
    if target_vol_gal <= 0:
        raise ValueError("target volume must be greater than 0 gallons")

    print(f"Target: {target_vol_gal:.3f} gal")
    if not enable_output:
        print(f"[DRY-RUN] GPIO{VALVE_PIN} output is disabled.")
        print("No ADC bus was opened and no GPIO output was configured.")
        print("Re-run with --enable-output only after review-required items are closed.")
        return 0.0

    gpio = _load_gpio()
    adc = Max1238()
    adc.setup_adc()

    volume_gal = 0.0
    start = time.monotonic()
    last_log = start
    low_flow_start = None

    gpio.output(VALVE_PIN, gpio.HIGH)
    print(f"GPIO{VALVE_PIN} HIGH: valve command asserted")

    try:
        previous = time.monotonic()
        while volume_gal < target_vol_gal:
            now = time.monotonic()
            dt = now - previous
            previous = now

            if (now - start) > (max_run_minutes * 60.0):
                print("[!] Timeout reached. Stopping.")
                break

            temps = read_external_temps_c(adc)
            ambient = read_ambient_temp_c(adc)
            flow = read_flow_gpm(adc)

            if any(value != value for value in temps.values()) or ambient != ambient or flow != flow:
                print("[!] Sensor read error. Stopping.")
                break

            volume_gal += max(flow, 0.0) * (dt / 60.0)

            if flow < MIN_FLOW_GPM:
                if low_flow_start is None:
                    low_flow_start = now
                elif (now - low_flow_start) >= LOW_FLOW_TIMEOUT_S:
                    print("[!] Low flow persisted. Stopping.")
                    break
            else:
                low_flow_start = None

            if (now - last_log) >= PRINT_PERIOD_S:
                print(
                    f"T_hot={temps['hot']:.1f} C  "
                    f"T_cold={temps['cold']:.1f} C  "
                    f"T_ambient={ambient:.1f} C  "
                    f"Flow={flow:.2f} gpm  "
                    f"Volume={volume_gal:.3f} gal"
                )
                last_log = now

            time.sleep(0.05)
    finally:
        _fail_safe_close()
        adc.close()
        print(f"GPIO{VALVE_PIN} LOW: valve command cleared")

    print(f"Volume drawn: {volume_gal:.3f} gal")
    return volume_gal


def main() -> int:
    parser = argparse.ArgumentParser(description="WH1 ADC-based water draw control")
    parser.add_argument("--target-gal", type=float, required=True)
    parser.add_argument("--max-run-minutes", type=float, default=MAX_RUN_MINUTES)
    parser.add_argument(
        "--enable-output",
        action="store_true",
        help="actually drive GPIO17; dry-run by default",
    )
    args = parser.parse_args()

    draw_water(
        args.target_gal,
        enable_output=args.enable_output,
        max_run_minutes=args.max_run_minutes,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
