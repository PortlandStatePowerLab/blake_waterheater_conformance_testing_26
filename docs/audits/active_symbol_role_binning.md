# Active Python Symbol Role Binning Audit

## Purpose

Classify functions, classes, and methods in active Python software by role before refactoring.

This is an audit-only document. It does not change runtime behavior.

## Scope

Included:

- Tracked Python files under `software/`.
- Active runtime, diagnostic, helper, and package software files.
- Functions, methods, and classes discoverable through Python AST parsing.

Excluded:

- `legacy_deprecated/` files.
- Hardware behavior changes.
- Runtime edits.
- Import rewrites.
- File moves.

## Bin definitions

| Bin | Meaning |
| --- | --- |
| `HARDWARE_IO` | Direct communication with external hardware interfaces that are not specifically GPIO or I2C-register helpers. |
| `GPIO_CONTROL` | GPIO, relay, or valve control behavior. |
| `I2C_REGISTER_ACCESS` | I2C bus access, register reads/writes, ADC/power-monitor register helpers. |
| `SENSOR_CONVERSION` | Raw sensor code/current/voltage/temperature conversion or calibration math. |
| `FLOW_VOLUME_MATH` | Flow rate, elapsed-time integration, draw volume, gallons/GPM calculations. |
| `POWER_MONITORING_MATH` | Voltage/current/power/power-factor calculations. |
| `SAFETY_LIMIT` | Max-run, low-flow, timeout, emergency stop, guardrail, or cleanup safety behavior. |
| `CONFIG_LOOKUP` | Pin/channel/address/config/hardware-map lookup logic. |
| `DATA_LOGGING` | CSV, JSON, file, path, log writing, or saved output behavior. |
| `CLI_OR_MAIN_GLUE` | Main functions, argument parsing, command-line setup, or entrypoint glue. |
| `DIAGNOSTIC_HELPER` | Helper symbol inside a diagnostic/test-style module. |
| `CLASS_CONTAINER` | Class definitions; requires manual review to determine whether class is a data container, hardware wrapper, or runtime object. |
| `UNKNOWN_SYMBOL` | Role unclear from automatic scan; needs manual inspection. |

## Summary counts by bin

| Bin | Count |
| --- | ---: |
| `HARDWARE_IO` | 0 |
| `GPIO_CONTROL` | 6 |
| `I2C_REGISTER_ACCESS` | 13 |
| `SENSOR_CONVERSION` | 2 |
| `FLOW_VOLUME_MATH` | 0 |
| `POWER_MONITORING_MATH` | 0 |
| `SAFETY_LIMIT` | 0 |
| `CONFIG_LOOKUP` | 0 |
| `DATA_LOGGING` | 0 |
| `CLI_OR_MAIN_GLUE` | 5 |
| `DIAGNOSTIC_HELPER` | 1 |
| `CLASS_CONTAINER` | 7 |
| `UNKNOWN_SYMBOL` | 0 |

## Summary counts by symbol kind

| Kind | Count |
| --- | ---: |
| `function` | 16 |
| `method` | 11 |
| `class` | 7 |

## File summary

| File | Symbols found | Entrypoint-looking file |
| --- | ---: | --- |
| `software/adc/max1238.py` | 18 | no |
| `software/diagnostics/read_acs37800_once.py` | 1 | yes |
| `software/diagnostics/read_adc_raw.py` | 2 | yes |
| `software/diagnostics/valve_gpio_check.py` | 1 | yes |
| `software/rs485_cta2045/gs10_modbus_test.py` | 1 | yes |
| `software/water_draw/whs.py` | 11 | yes |

## Symbol inventory by role

| File | Line | Symbol | Kind | Bin | Evidence / reason |
| --- | ---: | --- | --- | --- | --- |
| `software/adc/max1238.py` | 9 | `InputMode` | `class` | `CLASS_CONTAINER` | Class definition; inspect whether it is data/container logic or hardware wrapper before refactor. |
| `software/adc/max1238.py` | 14 | `ClockType` | `class` | `CLASS_CONTAINER` | Class definition; inspect whether it is data/container logic or hardware wrapper before refactor. |
| `software/adc/max1238.py` | 19 | `Polarity` | `class` | `CLASS_CONTAINER` | Class definition; inspect whether it is data/container logic or hardware wrapper before refactor. |
| `software/adc/max1238.py` | 24 | `ResetMode` | `class` | `CLASS_CONTAINER` | Class definition; inspect whether it is data/container logic or hardware wrapper before refactor. |
| `software/adc/max1238.py` | 29 | `ScanMode` | `class` | `CLASS_CONTAINER` | Class definition; inspect whether it is data/container logic or hardware wrapper before refactor. |
| `software/adc/max1238.py` | 37 | `ReferenceVoltage` | `class` | `CLASS_CONTAINER` | Class definition; inspect whether it is data/container logic or hardware wrapper before refactor. |
| `software/adc/max1238.py` | 47 | `Max1238` | `class` | `CLASS_CONTAINER` | Class definition; inspect whether it is data/container logic or hardware wrapper before refactor. |
| `software/adc/max1238.py` | 56 | `Max1238.__init__` | `method` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/adc/max1238.py` | 61 | `Max1238._xfer` | `method` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/adc/max1238.py` | 114 | `Max1238._build_setup_byte` | `method` | `GPIO_CONTROL` | GPIO/relay/valve control terms found. |
| `software/adc/max1238.py` | 131 | `Max1238._build_config_byte` | `method` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/adc/max1238.py` | 148 | `Max1238.setup_adc` | `method` | `GPIO_CONTROL` | GPIO/relay/valve control terms found. |
| `software/adc/max1238.py` | 158 | `Max1238.read_single` | `method` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/adc/max1238.py` | 167 | `Max1238.read_range` | `method` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/adc/max1238.py` | 192 | `Max1238.read_multiple` | `method` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/adc/max1238.py` | 216 | `Max1238.close` | `method` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/adc/max1238.py` | 222 | `Max1238.__enter__` | `method` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/adc/max1238.py` | 225 | `Max1238.__exit__` | `method` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/diagnostics/read_acs37800_once.py` | 21 | `main` | `function` | `CLI_OR_MAIN_GLUE` | Main/argument parsing symbol. |
| `software/diagnostics/read_adc_raw.py` | 35 | `raw_to_voltage` | `function` | `DIAGNOSTIC_HELPER` | Symbol lives in diagnostic/test-style entrypoint file. |
| `software/diagnostics/read_adc_raw.py` | 39 | `main` | `function` | `CLI_OR_MAIN_GLUE` | Main/argument parsing symbol. |
| `software/diagnostics/valve_gpio_check.py` | 44 | `main` | `function` | `CLI_OR_MAIN_GLUE` | Main/argument parsing symbol. |
| `software/rs485_cta2045/gs10_modbus_test.py` | 8 | `main` | `function` | `CLI_OR_MAIN_GLUE` | Main/argument parsing symbol. |
| `software/water_draw/whs.py` | 43 | `_load_gpio` | `function` | `GPIO_CONTROL` | GPIO/relay/valve control terms found. |
| `software/water_draw/whs.py` | 55 | `_fail_safe_close` | `function` | `GPIO_CONTROL` | GPIO/relay/valve control terms found. |
| `software/water_draw/whs.py` | 67 | `_signal_handler` | `function` | `GPIO_CONTROL` | GPIO/relay/valve control terms found. |
| `software/water_draw/whs.py` | 77 | `_raw_to_voltage` | `function` | `SENSOR_CONVERSION` | Sensor conversion/calibration terms found. |
| `software/water_draw/whs.py` | 83 | `_volt_to_span` | `function` | `SENSOR_CONVERSION` | Sensor conversion/calibration terms found. |
| `software/water_draw/whs.py` | 91 | `read_voltage` | `function` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/water_draw/whs.py` | 95 | `read_ambient_temp_c` | `function` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/water_draw/whs.py` | 99 | `read_external_temps_c` | `function` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/water_draw/whs.py` | 106 | `read_flow_gpm` | `function` | `I2C_REGISTER_ACCESS` | I2C/register/bus access terms found. |
| `software/water_draw/whs.py` | 110 | `draw_water` | `function` | `GPIO_CONTROL` | GPIO/relay/valve control terms found. |
| `software/water_draw/whs.py` | 188 | `main` | `function` | `CLI_OR_MAIN_GLUE` | Main/argument parsing symbol. |

## Parse errors

> Historical note: these UTF-8 BOM / U+FEFF parse errors were resolved by PR 103.
> They are retained here as pre-cleanup audit findings, not current failures.

| File | Line | Error |
| --- | ---: | --- |
| `software/__init__.py` | 1 | invalid non-printable character U+FEFF |
| `software/adc/__init__.py` | 1 | invalid non-printable character U+FEFF |
| `software/common/__init__.py` | 1 | invalid non-printable character U+FEFF |
| `software/common/hardware_map.py` | 1 | invalid non-printable character U+FEFF |
| `software/diagnostics/__init__.py` | 1 | invalid non-printable character U+FEFF |
| `software/power_monitoring/__init__.py` | 1 | invalid non-printable character U+FEFF |
| `software/rs485_cta2045/__init__.py` | 1 | invalid non-printable character U+FEFF |
| `software/valve_control/__init__.py` | 1 | invalid non-printable character U+FEFF |
| `software/water_draw/__init__.py` | 1 | invalid non-printable character U+FEFF |

## Findings

- Active symbol roles are now mapped before refactor work.
- This audit is intentionally heuristic; review `UNKNOWN_SYMBOL`, `CLASS_CONTAINER`, and active runtime symbols manually before moving code.
- Keep `software/water_draw/whs.py` treated as active hardware-coupled runtime code until a separate refactor card exists.
- ACS37800 reusable helper extraction should remain a future card; this audit should not create or move that module.

## Next action

- Review this audit for obvious mis-bins.
- Use the results to choose one small refactor-prep card, not a broad rewrite.
