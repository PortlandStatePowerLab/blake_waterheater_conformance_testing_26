# Hardware Coupling Split Audit

## Purpose

Map active Python software into hardware-coupled versus laptop-testable logic before refactoring.

This is an audit-only document. It does not change runtime behavior.

## Scope

Included:

- Tracked Python files under `software/`.
- Active runtime, diagnostic, helper, and package software files.
- Functions, methods, and classes discoverable through Python AST parsing.

Excluded:

- `legacy_deprecated/` files.
- Runtime edits.
- Import rewrites.
- File moves.
- New helper modules.

## Coupling bins

| Bin | Meaning |
| --- | --- |
| `REQUIRES_PI_STATION` | Requires Raspberry Pi, station hardware, GPIO, I2C bus, sensor/relay hardware, RS-485, or connected devices. |
| `LAPTOP_TESTABLE` | Can be tested on a normal laptop if isolated from hardware calls. Includes conversion math, formatting, schema, plotting, and config lookup. |
| `MIXED_ORCHESTRATION` | Coordinates hardware and pure logic together. Usually entrypoint, CLI, safety, diagnostic, or class wrapper code. |
| `PACKAGE_INIT` | Package marker file. |
| `UNKNOWN_COUPLING` | Coupling unclear from automatic scan; inspect manually. |

## Hardware-coupled examples

- GPIO17 relay control.
- I2C read from MAX1238.
- I2C read from ACS37800.
- RS-485 serial communication.

## Laptop-testable examples

- ADC code to voltage conversion.
- Voltage to current_mA conversion.
- current_mA to temp_f conversion.
- Flow pulse/count to flow_gpm conversion.
- Timestamp formatting.
- CSV row schema.
- Plot generation.

## Summary counts by file

| Bin | Count |
| --- | ---: |
| `REQUIRES_PI_STATION` | 6 |
| `LAPTOP_TESTABLE` | 0 |
| `MIXED_ORCHESTRATION` | 0 |
| `PACKAGE_INIT` | 0 |
| `UNKNOWN_COUPLING` | 0 |

## Summary counts by symbol

| Bin | Count |
| --- | ---: |
| `REQUIRES_PI_STATION` | 33 |
| `LAPTOP_TESTABLE` | 1 |
| `MIXED_ORCHESTRATION` | 0 |
| `PACKAGE_INIT` | 0 |
| `UNKNOWN_COUPLING` | 0 |

## File-level coupling map

| File | Coupling bin | Symbols found | Entrypoint-looking file | Evidence / reason |
| --- | --- | ---: | --- | --- |
| `software/adc/max1238.py` | `REQUIRES_PI_STATION` | 18 | no | Direct hardware, bus, GPIO, relay, valve, ADC, power monitor, or serial terms found. |
| `software/diagnostics/read_acs37800_once.py` | `REQUIRES_PI_STATION` | 1 | yes | Direct hardware, bus, GPIO, relay, valve, ADC, power monitor, or serial terms found. |
| `software/diagnostics/read_adc_raw.py` | `REQUIRES_PI_STATION` | 2 | yes | Direct hardware, bus, GPIO, relay, valve, ADC, power monitor, or serial terms found. |
| `software/diagnostics/valve_gpio_check.py` | `REQUIRES_PI_STATION` | 1 | yes | Direct hardware, bus, GPIO, relay, valve, ADC, power monitor, or serial terms found. |
| `software/rs485_cta2045/gs10_modbus_test.py` | `REQUIRES_PI_STATION` | 1 | yes | Direct hardware, bus, GPIO, relay, valve, ADC, power monitor, or serial terms found. |
| `software/water_draw/whs.py` | `REQUIRES_PI_STATION` | 11 | yes | Direct hardware, bus, GPIO, relay, valve, ADC, power monitor, or serial terms found. |

## Symbol-level coupling map

| File | Line | Symbol | Kind | Coupling bin | Evidence / reason |
| --- | ---: | --- | --- | --- | --- |
| `software/adc/max1238.py` | 9 | `InputMode` | `class` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 14 | `ClockType` | `class` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 19 | `Polarity` | `class` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 24 | `ResetMode` | `class` | `REQUIRES_PI_STATION` | GPIO/relay/valve control requires Pi/station hardware. |
| `software/adc/max1238.py` | 29 | `ScanMode` | `class` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 37 | `ReferenceVoltage` | `class` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 47 | `Max1238` | `class` | `REQUIRES_PI_STATION` | GPIO/relay/valve control requires Pi/station hardware. |
| `software/adc/max1238.py` | 56 | `Max1238.__init__` | `method` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 61 | `Max1238._xfer` | `method` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 114 | `Max1238._build_setup_byte` | `method` | `REQUIRES_PI_STATION` | GPIO/relay/valve control requires Pi/station hardware. |
| `software/adc/max1238.py` | 131 | `Max1238._build_config_byte` | `method` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 148 | `Max1238.setup_adc` | `method` | `REQUIRES_PI_STATION` | GPIO/relay/valve control requires Pi/station hardware. |
| `software/adc/max1238.py` | 158 | `Max1238.read_single` | `method` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 167 | `Max1238.read_range` | `method` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 192 | `Max1238.read_multiple` | `method` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 216 | `Max1238.close` | `method` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 222 | `Max1238.__enter__` | `method` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/adc/max1238.py` | 225 | `Max1238.__exit__` | `method` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/diagnostics/read_acs37800_once.py` | 21 | `main` | `function` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/diagnostics/read_adc_raw.py` | 35 | `raw_to_voltage` | `function` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/diagnostics/read_adc_raw.py` | 39 | `main` | `function` | `REQUIRES_PI_STATION` | GPIO/relay/valve control requires Pi/station hardware. |
| `software/diagnostics/valve_gpio_check.py` | 44 | `main` | `function` | `REQUIRES_PI_STATION` | GPIO/relay/valve control requires Pi/station hardware. |
| `software/rs485_cta2045/gs10_modbus_test.py` | 8 | `main` | `function` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/water_draw/whs.py` | 43 | `_load_gpio` | `function` | `REQUIRES_PI_STATION` | GPIO/relay/valve control requires Pi/station hardware. |
| `software/water_draw/whs.py` | 55 | `_fail_safe_close` | `function` | `REQUIRES_PI_STATION` | GPIO/relay/valve control requires Pi/station hardware. |
| `software/water_draw/whs.py` | 67 | `_signal_handler` | `function` | `REQUIRES_PI_STATION` | GPIO/relay/valve control requires Pi/station hardware. |
| `software/water_draw/whs.py` | 77 | `_raw_to_voltage` | `function` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/water_draw/whs.py` | 83 | `_volt_to_span` | `function` | `LAPTOP_TESTABLE` | Conversion/math/calibration terms found; should be testable without live hardware if isolated. |
| `software/water_draw/whs.py` | 91 | `read_voltage` | `function` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/water_draw/whs.py` | 95 | `read_ambient_temp_c` | `function` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/water_draw/whs.py` | 99 | `read_external_temps_c` | `function` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/water_draw/whs.py` | 106 | `read_flow_gpm` | `function` | `REQUIRES_PI_STATION` | I2C/register/ADC/power-monitor access requires connected hardware. |
| `software/water_draw/whs.py` | 110 | `draw_water` | `function` | `REQUIRES_PI_STATION` | GPIO/relay/valve control requires Pi/station hardware. |
| `software/water_draw/whs.py` | 188 | `main` | `function` | `REQUIRES_PI_STATION` | GPIO/relay/valve control requires Pi/station hardware. |

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

- Active software now has a first-pass hardware coupling map.
- `REQUIRES_PI_STATION` items should stay behind a hardware boundary and need Pi/station validation.
- `LAPTOP_TESTABLE` items are candidates for future unit tests on any laptop.
- `MIXED_ORCHESTRATION` items are the most likely refactor targets because they often glue hardware calls to pure conversion/logging logic.
- `software/water_draw/whs.py` remains active hardware-coupled runtime code and should not be moved in this audit-only card.
- ACS37800 helper extraction remains a future card; this audit only maps the boundary.

## Next action

- Review this audit for obvious mis-bins.
- Choose one small future refactor card that extracts laptop-testable conversion logic without changing hardware behavior.
