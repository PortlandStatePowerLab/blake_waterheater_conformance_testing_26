# WH1 Deployment Manifest

This manifest is the allow-list for Raspberry Pi copy. Do not copy
`legacy_deprecated/`, `docs/`, `hardware/`, generated caches, or audit reports as
runtime payload.

Suggested Pi destination: `/home/pi/wh1`

## Runtime files to copy

| Staged file | Suggested Pi destination | Purpose |
|-------------|--------------------------|---------|
| `software/__init__.py` | `/home/pi/wh1/software/__init__.py` | Python package marker |
| `software/requirements.txt` | `/home/pi/wh1/software/requirements.txt` | Python dependency list |
| `software/common/__init__.py` | `/home/pi/wh1/software/common/__init__.py` | Shared package marker |
| `software/common/hardware_map.py` | `/home/pi/wh1/software/common/hardware_map.py` | Current hardware constants |
| `software/adc/__init__.py` | `/home/pi/wh1/software/adc/__init__.py` | ADC package marker |
| `software/adc/max1238.py` | `/home/pi/wh1/software/adc/max1238.py` | MAX1238 I2C ADC driver |
| `software/operator_checks/__init__.py` | `/home/pi/wh1/software/operator_checks/__init__.py` | Operator-check package marker |
| `software/operator_checks/read_adc_raw.py` | `/home/pi/wh1/software/operator_checks/read_adc_raw.py` | Read-only MAX1238 raw channel check |
| `software/operator_checks/read_acs37800_once.py` | `/home/pi/wh1/software/operator_checks/read_acs37800_once.py` | Safe ACS37800 review-required check |
| `software/operator_checks/valve_gpio_check.py` | `/home/pi/wh1/software/operator_checks/valve_gpio_check.py` | Valve GPIO dry-run check; output disabled by default |
| `software/water_draw/__init__.py` | `/home/pi/wh1/software/water_draw/__init__.py` | Water draw package marker |
| `software/water_draw/whs.py` | `/home/pi/wh1/software/water_draw/whs.py` | Dry-run-first water draw controller |

## First safe Pi commands

Run from `/home/pi/wh1` after copying the runtime files:

```bash
python3 -m pip install -r software/requirements.txt
python3 -m compileall software
ls -l /dev/i2c-1
i2cdetect -y 1
python3 software/operator_checks/read_adc_raw.py
python3 software/operator_checks/read_acs37800_once.py
python3 software/operator_checks/valve_gpio_check.py
```

`read_acs37800_once.py` is intentionally a review-required stub until the usable
register map is verified.

## Controlled output commands

`software/operator_checks/valve_gpio_check.py --enable-output` may be used only after
confirming the completed valve relay verification record:

```text
project_control/verification_completed/valve_relay_operation_VERIFIED_2026-07-01.md
```

`software/water_draw/whs.py --enable-output` still requires ADC values, flow
scaling, temperature scaling, and stop behavior to be reviewed on the real
station before routine use.

## Do not run yet

- Anything under `legacy_deprecated/`.
- Any direct DS18B20 or GPIO6 flow-count script from legacy.
- `software/water_draw/whs.py --enable-output` until ADC values, flow scaling,
  relay polarity, temperature scaling, and stop behavior have been reviewed on
  the real station.
