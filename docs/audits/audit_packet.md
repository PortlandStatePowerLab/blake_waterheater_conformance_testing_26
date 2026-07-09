# Source file: docs/audits/software_symbol_inventory.md

# Software Symbol Inventory

Generated: 2026-07-07T15:47:25

Purpose: whole-system inventory before binning entrypoints, helper files, classes, methods, functions, data I/O, and hardware-coupled code.

## Summary

- Python files found: 46

- Files with `if __name__ == '__main__'`: 16
- Classes found: 17
- Methods found: 28
- Standalone functions found: 60

## Files and Symbols

### `legacy_deprecated/broken_or_incomplete/CheckCurrent_cpp_saved_as_py.py`

- Parse status: `SyntaxError line 6: invalid syntax`

### `legacy_deprecated/broken_or_incomplete/DrawController_FM_missing_24H_WDP.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `csv`
  - `from datetime`
  - `from numpy`
  - `from numpy.random`
  - `from queue`
  - `from threading`
  - `from time`
  - `os`
  - `random`
- Classes: none found
- Standalone functions:
  - `draw_water(targetVol)` at line 20
  - `draw_water_with_queue(targetVol, queue)` at line 55

### `legacy_deprecated/ds18b20_direct_pi_scripts/GetTemp.py`

- Appears directly runnable: `True`
- Imports:
  - `csv`
  - `datetime`
  - `glob`
  - `os`
  - `time`
- Classes: none found
- Standalone functions:
  - `read_temp(device, decimals)` at line 9
  - `write_to_csv(file_name, temp_data)` at line 43

### `legacy_deprecated/ds18b20_direct_pi_scripts/TempQuick.py`

- Appears directly runnable: `True`
- Imports:
  - `csv`
  - `datetime`
  - `glob`
  - `os`
  - `time`
- Classes: none found
- Standalone functions:
  - `read_temp(device, decimals)` at line 9

### `legacy_deprecated/gpio6_flow_scripts/DrawController.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `csv`
  - `from datetime`
  - `from numpy`
  - `from numpy.random`
  - `from threading`
  - `from time`
  - `os`
  - `random`
  - `sys`
- Classes: none found
- Standalone functions:
  - `draw_water(targetVol)` at line 24

### `legacy_deprecated/gpio6_flow_scripts/FMTest.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `from time`
- Classes: none found
- Standalone functions: none found

### `legacy_deprecated/gpio6_flow_scripts/ValveControl_direct_gpio17.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
- Classes: none found
- Standalone functions: none found

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/controller/DeltaTSchedule.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `from datetime`
  - `from time`
- Classes: none found
- Standalone functions:
  - `draw_water(targetVol)` at line 20

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/controller/DrawController.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `csv`
  - `from datetime`
  - `from numpy`
  - `from numpy.random`
  - `from threading`
  - `from time`
  - `os`
  - `random`
  - `sys`
- Classes: none found
- Standalone functions:
  - `draw_water(targetVol)` at line 24

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/controller/DrawController_Conformance.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `csv`
  - `from datetime`
  - `from numpy`
  - `from numpy.random`
  - `from threading`
  - `from time`
  - `os`
  - `random`
  - `sys`
- Classes: none found
- Standalone functions:
  - `draw_water(targetVol)` at line 24

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/GetTemp.py`

- Appears directly runnable: `True`
- Imports:
  - `csv`
  - `datetime`
  - `glob`
  - `os`
  - `time`
- Classes: none found
- Standalone functions:
  - `read_temp(device, decimals)` at line 9
  - `write_to_csv(file_name, temp_data)` at line 43

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/sample2/sample2/CheckCurrent.py`

- Parse status: `SyntaxError line 6: invalid syntax`

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/sample2/sample2/ReadCT.py`

- Appears directly runnable: `True`
- Imports:
  - `csv`
  - `from datetime`
  - `from gpiozero`
  - `time`
- Classes:
  - `class MCP3008Current` at line 6
    - `__init__(self, channel)` at line 10
    - `get_current(self)` at line 13
- Standalone functions: none found

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/TempQuick.py`

- Appears directly runnable: `True`
- Imports:
  - `csv`
  - `datetime`
  - `glob`
  - `os`
  - `time`
- Classes: none found
- Standalone functions:
  - `read_temp(device, decimals)` at line 9

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/test.py`

- Appears directly runnable: `True`
- Imports:
  - `from fpdf`
  - `os`
- Classes:
  - `class PDF` at line 4
    - `__init__(self)` at line 5
    - `add_code_file(self, filename, content)` at line 11
- Standalone functions:
  - `get_code_files(root_dir, extensions)` at line 18
  - `main()` at line 27

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/StartController.py`

- Appears directly runnable: `False`
- Imports:
  - `os`
  - `schedule`
  - `signal`
  - `subprocess`
  - `time`
- Classes: none found
- Standalone functions:
  - `SchedDraw(mode)` at line 13

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/water_draw_scripts/FMTest.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `from time`
- Classes: none found
- Standalone functions: none found

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/water_draw_scripts/ValveControl.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
- Classes: none found
- Standalone functions: none found

### `legacy_deprecated/old_duplicates/acs37800_final_original_reference.py`

- Appears directly runnable: `True`
- Imports:
  - `from datetime`
  - `from smbus2`
  - `json`
  - `os`
  - `time`
- Classes: none found
- Standalone functions:
  - `u16(x)` at line 36
  - `s16(x)` at line 38
  - `read32_le(bus, reg)` at line 42
  - `pf_from_11bit(pf11)` at line 50
  - `load_cal()` at line 57
  - `save_cal(cal)` at line 78
  - `get_values(bus, cal)` at line 83
  - `calibrate(bus, cal)` at line 145
  - `main()` at line 212

### `legacy_deprecated/old_duplicates/max1238_root_duplicate.py`

- Appears directly runnable: `False`
- Imports:
  - `from __future__`
  - `from enum`
  - `from smbus2`
  - `from typing`
  - `time`
- Classes:
  - `class InputMode` at line 9
    - no methods found
  - `class ClockType` at line 14
    - no methods found
  - `class Polarity` at line 19
    - no methods found
  - `class ResetMode` at line 24
    - no methods found
  - `class ScanMode` at line 29
    - no methods found
  - `class ReferenceVoltage` at line 37
    - no methods found
  - `class Max1238` at line 47
    - `__init__(self, address, bus_num)` at line 56
    - `_xfer(self, write_bytes, read_len, retries, retry_delay_s)` at line 61
    - `_build_setup_byte(self, referenceVoltage, clock, polarity, reset)` at line 114
    - `_build_config_byte(self, scan, channel, mode)` at line 131
    - `setup_adc(self, referenceVoltage, clock, polarity, reset)` at line 148
    - `read_single(self, channel, mode)` at line 158
    - `read_range(self, start_channel, end_channel, mode)` at line 167
    - `read_multiple(self, start_channel, count, mode)` at line 192
    - `close(self)` at line 216
    - `__enter__(self)` at line 222
    - `__exit__(self, exc_type, exc, tb)` at line 225
- Standalone functions: none found

### `legacy_deprecated/old_duplicates/sensor_test_duplicate_of_whs.py`

- Appears directly runnable: `True`
- Imports:
  - `RPi.GPIO`
  - `atexit`
  - `from max1238`
  - `signal`
  - `sys`
  - `time`
- Classes: none found
- Standalone functions:
  - `_fail_safe_close()` at line 47
  - `_signal_handler(signum, frame)` at line 57
  - `_raw_to_voltage(raw)` at line 67
  - `_volt_to_span(val_v, span_max, span_min)` at line 73
  - `read_voltage(channel)` at line 85
  - `read_amb_temps()` at line 90
  - `read_externel_temps()` at line 93
  - `read_flow_gpm()` at line 100
  - `draw_water(target_vol_gal)` at line 104

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DeltaTSchedule.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `from datetime`
  - `from time`
- Classes: none found
- Standalone functions:
  - `draw_water(targetVol)` at line 20

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `csv`
  - `from datetime`
  - `from numpy`
  - `from numpy.random`
  - `from threading`
  - `from time`
  - `os`
  - `random`
  - `sys`
- Classes: none found
- Standalone functions:
  - `draw_water(targetVol)` at line 24

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController2.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `csv`
  - `from datetime`
  - `from numpy`
  - `from numpy.random`
  - `from threading`
  - `from time`
  - `os`
  - `random`
- Classes: none found
- Standalone functions:
  - `draw_water(targetVol)` at line 21

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController_Conformance.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `csv`
  - `from datetime`
  - `from numpy`
  - `from numpy.random`
  - `from threading`
  - `from time`
  - `os`
  - `random`
  - `sys`
- Classes: none found
- Standalone functions:
  - `draw_water(targetVol)` at line 24

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController_FM.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `csv`
  - `from datetime`
  - `from numpy`
  - `from numpy.random`
  - `from queue`
  - `from threading`
  - `from time`
  - `os`
  - `random`
- Classes: none found
- Standalone functions:
  - `draw_water(targetVol)` at line 20
  - `draw_water_with_queue(targetVol, queue)` at line 55

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/dcs/GetTemp.py`

- Appears directly runnable: `True`
- Imports:
  - `csv`
  - `datetime`
  - `glob`
  - `os`
  - `time`
- Classes: none found
- Standalone functions:
  - `read_temp(device, decimals)` at line 9
  - `write_to_csv(file_name, temp_data)` at line 43

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/dcs/TempQuick.py`

- Appears directly runnable: `True`
- Imports:
  - `csv`
  - `datetime`
  - `glob`
  - `os`
  - `time`
- Classes: none found
- Standalone functions:
  - `read_temp(device, decimals)` at line 9

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/dcs/test.py`

- Appears directly runnable: `True`
- Imports:
  - `from fpdf`
  - `os`
- Classes:
  - `class PDF` at line 4
    - `__init__(self)` at line 5
    - `add_code_file(self, filename, content)` at line 11
- Standalone functions:
  - `get_code_files(root_dir, extensions)` at line 18
  - `main()` at line 27

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/water_draw_scripts/FMTest.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
  - `from time`
- Classes: none found
- Standalone functions: none found

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/water_draw_scripts/ValveControl.py`

- Appears directly runnable: `False`
- Imports:
  - `RPi.GPIO`
- Classes: none found
- Standalone functions: none found

### `software/__init__.py`

> Historical note: these UTF-8 BOM / U+FEFF parse errors were resolved by PR 103.
> They are retained here as pre-cleanup audit findings, not current failures.

- Parse status: `SyntaxError line 1: invalid non-printable character U+FEFF`

> Historical note: these UTF-8 BOM / U+FEFF parse errors were resolved by PR 103.
> They are retained here as pre-cleanup audit findings, not current failures.

### `software/adc/__init__.py`

> Historical note: these UTF-8 BOM / U+FEFF parse errors were resolved by PR 103.
> They are retained here as pre-cleanup audit findings, not current failures.

- Parse status: `SyntaxError line 1: invalid non-printable character U+FEFF`

### `software/adc/max1238.py`

- Appears directly runnable: `False`
- Imports:
  - `from __future__`
  - `from enum`
  - `from smbus2`
  - `from typing`
  - `time`
- Classes:
  - `class InputMode` at line 9
    - no methods found
  - `class ClockType` at line 14
    - no methods found
  - `class Polarity` at line 19
    - no methods found
  - `class ResetMode` at line 24
    - no methods found
  - `class ScanMode` at line 29
    - no methods found
  - `class ReferenceVoltage` at line 37
    - no methods found
  - `class Max1238` at line 47
    - `__init__(self, address, bus_num)` at line 56
    - `_xfer(self, write_bytes, read_len, retries, retry_delay_s)` at line 61
    - `_build_setup_byte(self, referenceVoltage, clock, polarity, reset)` at line 114
    - `_build_config_byte(self, scan, channel, mode)` at line 131
    - `setup_adc(self, referenceVoltage, clock, polarity, reset)` at line 148
    - `read_single(self, channel, mode)` at line 158
    - `read_range(self, start_channel, end_channel, mode)` at line 167
    - `read_multiple(self, start_channel, count, mode)` at line 192
    - `close(self)` at line 216
    - `__enter__(self)` at line 222
    - `__exit__(self, exc_type, exc, tb)` at line 225
- Standalone functions: none found

### `software/common/__init__.py`

> Historical note: these UTF-8 BOM / U+FEFF parse errors were resolved by PR 103.
> They are retained here as pre-cleanup audit findings, not current failures.

- Parse status: `SyntaxError line 1: invalid non-printable character U+FEFF`

### `software/common/hardware_map.py`

> Historical note: these UTF-8 BOM / U+FEFF parse errors were resolved by PR 103.
> They are retained here as pre-cleanup audit findings, not current failures.

- Parse status: `SyntaxError line 1: invalid non-printable character U+FEFF`

### `software/diagnostics/__init__.py`

> Historical note: these UTF-8 BOM / U+FEFF parse errors were resolved by PR 103.
> They are retained here as pre-cleanup audit findings, not current failures.

- Parse status: `SyntaxError line 1: invalid non-printable character U+FEFF`

### `software/diagnostics/read_acs37800_once.py`

- Appears directly runnable: `True`
- Module note: Safe ACS37800 diagnostic placeholder.
- Imports:
  - `from __future__`
  - `from pathlib`
  - `from software.common.hardware_map`
  - `sys`
- Classes: none found
- Standalone functions:
  - `main()` at line 21

### `software/diagnostics/read_adc_raw.py`

- Appears directly runnable: `True`
- Module note: Read raw MAX1238 ADC values from the current WH1 channel map.
- Imports:
  - `argparse`
  - `from __future__`
  - `from pathlib`
  - `from software.adc.max1238`
  - `from software.common.hardware_map`
  - `sys`
- Classes: none found
- Standalone functions:
  - `raw_to_voltage(raw)` at line 35
  - `main()` at line 39

### `software/diagnostics/valve_gpio_check.py`

- Appears directly runnable: `True`
- Module note: Dry-run-first GPIO17 valve relay diagnostic.
- Imports:
  - `RPi.GPIO`
  - `argparse`
  - `from __future__`
  - `from pathlib`
  - `from software.common.hardware_map`
  - `sys`
  - `time`
- Classes: none found
- Standalone functions:
  - `main()` at line 44

### `software/power_monitoring/__init__.py`

> Historical note: these UTF-8 BOM / U+FEFF parse errors were resolved by PR 103.
> They are retained here as pre-cleanup audit findings, not current failures.

- Parse status: `SyntaxError line 1: invalid non-printable character U+FEFF`

### `software/rs485_cta2045/__init__.py`

> Historical note: these UTF-8 BOM / U+FEFF parse errors were resolved by PR 103.
> They are retained here as pre-cleanup audit findings, not current failures.

- Parse status: `SyntaxError line 1: invalid non-printable character U+FEFF`

### `software/rs485_cta2045/gs10_modbus_test.py`

- Appears directly runnable: `True`
- Imports:
  - `argparse`
  - `from pymodbus.client`
  - `from pymodbus.exceptions`
  - `sys`
- Classes: none found
- Standalone functions:
  - `main()` at line 8

### `software/valve_control/__init__.py`

> Historical note: these UTF-8 BOM / U+FEFF parse errors were resolved by PR 103.
> They are retained here as pre-cleanup audit findings, not current failures.

- Parse status: `SyntaxError line 1: invalid non-printable character U+FEFF`

### `software/water_draw/__init__.py`

> Historical note: these UTF-8 BOM / U+FEFF parse errors were resolved by PR 103.
> They are retained here as pre-cleanup audit findings, not current failures.

- Parse status: `SyntaxError line 1: invalid non-printable character U+FEFF`

### `software/water_draw/whs.py`

- Appears directly runnable: `True`
- Module note: ADC-based WH1 water draw control for the current PCB-ribbon hardware.
- Imports:
  - `RPi.GPIO`
  - `argparse`
  - `atexit`
  - `from __future__`
  - `from pathlib`
  - `from software.adc.max1238`
  - `from software.common.hardware_map`
  - `from typing`
  - `signal`
  - `sys`
  - `time`
- Classes: none found
- Standalone functions:
  - `_load_gpio()` at line 43
  - `_fail_safe_close()` at line 55
  - `_signal_handler(signum, frame)` at line 67
  - `_raw_to_voltage(raw)` at line 77
  - `_volt_to_span(value_v, span_max, span_min)` at line 83
  - `read_voltage(adc, channel)` at line 91
  - `read_ambient_temp_c(adc)` at line 95
  - `read_external_temps_c(adc)` at line 99
  - `read_flow_gpm(adc)` at line 106
  - `draw_water(target_vol_gal)` at line 110
  - `main()` at line 188

---

# Source file: docs/audits/entrypoint_binning.md

# Entrypoint Binning Audit

Generated: 2026-07-07T16:20:08

Purpose: initial classification of runnable-looking Python entrypoints before refactoring.

## Scope

This audit bins entrypoint candidates only. It does not classify every helper module, class, method, or CSV/data path yet.

## Bins

- `ACTIVE_ENTRYPOINT`: expected active runtime command
- `DIAGNOSTIC_ENTRYPOINT`: diagnostic/check/test command
- `FUTURE_AGNOSTIC_ENTRYPOINT`: proposed future hardware-agnostic command
- `LEGACY_ENTRYPOINT`: runnable or script-like code in legacy/deprecated tree
- `DO_NOT_RUN_DIRECTLY`: import/helper file, not intended as a direct command
- `UNKNOWN_ENTRYPOINT`: runnable-looking file needing review

## Summary

- Python files scanned: 46
- Entrypoint candidates found: 33
- Parse errors found: 2

### Bin counts

- `DIAGNOSTIC_ENTRYPOINT`: 4
- `LEGACY_ENTRYPOINT`: 28
- `ACTIVE_ENTRYPOINT`: 1
- `UNKNOWN_ENTRYPOINT`: 0

## Entrypoint Candidates

### `legacy_deprecated/broken_or_incomplete/DrawController_FM_missing_24H_WDP.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/ds18b20_direct_pi_scripts/GetTemp.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: no/unknown
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/ds18b20_direct_pi_scripts/TempQuick.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: no/unknown
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/gpio6_flow_scripts/DrawController.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/gpio6_flow_scripts/FMTest.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/gpio6_flow_scripts/ValveControl_direct_gpio17.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/controller/DeltaTSchedule.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/controller/DrawController.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/controller/DrawController_Conformance.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/GetTemp.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: no/unknown
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/sample2/sample2/ReadCT.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/TempQuick.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: no/unknown
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/test.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: no/unknown
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/StartController.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: no/unknown
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/water_draw_scripts/FMTest.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/water_draw_scripts/ValveControl.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/acs37800_final_original_reference.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/sensor_test_duplicate_of_whs.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DeltaTSchedule.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController2.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController_Conformance.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController_FM.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/dcs/GetTemp.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: no/unknown
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/dcs/TempQuick.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: no/unknown
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/dcs/test.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: no/unknown
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/water_draw_scripts/FMTest.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/water_draw_scripts/ValveControl.py`

- Initial bin: `LEGACY_ENTRYPOINT`
- Evidence: `top_level_executable_statement`
- Hardware-coupled: yes
- Notes: Legacy/deprecated tree; keep for reference unless Blake promotes it.

### `software/diagnostics/read_acs37800_once.py`

- Initial bin: `DIAGNOSTIC_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: no/unknown
- Notes: Diagnostic script location. Module note: Safe ACS37800 diagnostic placeholder.

### `software/diagnostics/read_adc_raw.py`

- Initial bin: `DIAGNOSTIC_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: no/unknown
- Notes: Diagnostic script location. Module note: Read raw MAX1238 ADC values from the current WH1 channel map.

### `software/diagnostics/valve_gpio_check.py`

- Initial bin: `DIAGNOSTIC_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: yes
- Notes: Diagnostic script location. Module note: Dry-run-first GPIO17 valve relay diagnostic.

### `software/rs485_cta2045/gs10_modbus_test.py`

- Initial bin: `DIAGNOSTIC_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: no/unknown
- Notes: Name suggests diagnostic/test/check script; verify before treating as active.

### `software/water_draw/whs.py`

- Initial bin: `ACTIVE_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: yes
- Notes: Active WH1 water-draw runtime entrypoint for the current PCB-ribbon hardware. Dry-run-first CLI; requires `--enable-output` before opening ADC/GPIO and driving GPIO valve control. Refactor-later candidate for hardware-agnostic command shape.

## Parse Errors

These files could not be parsed as valid Python and should remain legacy/unknown unless recovered manually.

| Path | Error |
| --- | --- |
| `legacy_deprecated/broken_or_incomplete/CheckCurrent_cpp_saved_as_py.py` | `SyntaxError line 6: invalid syntax` |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/sample2/sample2/CheckCurrent.py` | `SyntaxError line 6: invalid syntax` |

## Review Questions for Next Pass

- Which `UNKNOWN_ENTRYPOINT` files are real active commands?
- Which diagnostic entrypoints are still useful on WH1/WH2/WH3/WH4?
- Which legacy entrypoints are reference-only versus candidates for salvage?
- Which active entrypoints should eventually become hardware-agnostic `python -m ...` commands?

---

# Source file: docs/audits/helper_module_binning.md

# Helper Module Binning Audit

## Purpose

Classify non-entrypoint Python files by role before any refactor, file moves, or import cleanup.

This is an audit-only document. It does not change runtime behavior.

## Scope

Included:

- Python files that are not primary CLI/runtime entrypoints.
- Active helper modules under `software/`.
- Package initialization files.
- Legacy helper-looking files, if present.

Excluded:

- Files already treated as entrypoints because they contain a main guard.
- Runtime edits.
- Import rewrites.
- File moves.

## Bin definitions

| Bin | Meaning |
| --- | --- |
| `HARDWARE_HELPER` | Talks directly to hardware, hardware buses, GPIO, ADC, sensors, power monitor chips, relays, RS-485, or board-specific interfaces. |
| `HARDWARE_AGNOSTIC_HELPER` | Pure logic/helper code that does not directly touch hardware or files. |
| `CONFIG_OR_CONSTANTS` | Pin maps, addresses, constants, channel maps, calibration constants, or other shared configuration. |
| `DATA_IO` | Reads/writes files, CSVs, logs, paths, or saved datasets. |
| `PLOTTING_ANALYSIS` | Analysis scripts/modules, plotting helpers, matplotlib/pandas/numpy post-processing. |
| `PACKAGE_INIT` | `__init__.py` package marker files. |
| `LEGACY_HELPER` | Helper-looking code under `legacy_deprecated/` or otherwise clearly deprecated. |
| `UNKNOWN_HELPER` | Role unclear from inspection; needs follow-up before refactor. |

## Summary counts

| Bin | Count |
| --- | ---: |
| `HARDWARE_HELPER` | 1 |
| `HARDWARE_AGNOSTIC_HELPER` | 0 |
| `CONFIG_OR_CONSTANTS` | 1 |
| `DATA_IO` | 0 |
| `PLOTTING_ANALYSIS` | 0 |
| `PACKAGE_INIT` | 8 |
| `LEGACY_HELPER` | 31 |
| `UNKNOWN_HELPER` | 0 |

## Helper module inventory

| File | Bin | Evidence / reason | Refactor notes |
| --- | --- | --- | --- |
| `legacy_deprecated/broken_or_incomplete/CheckCurrent_cpp_saved_as_py.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/broken_or_incomplete/DrawController_FM_missing_24H_WDP.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/ds18b20_direct_pi_scripts/GetTemp.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/ds18b20_direct_pi_scripts/TempQuick.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/gpio6_flow_scripts/DrawController.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/gpio6_flow_scripts/FMTest.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/gpio6_flow_scripts/ValveControl_direct_gpio17.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/StartController.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/controller/DeltaTSchedule.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/controller/DrawController.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/controller/DrawController_Conformance.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/GetTemp.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/TempQuick.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/sample2/sample2/CheckCurrent.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/sample2/sample2/ReadCT.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/dcs/test.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/water_draw_scripts/FMTest.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/midrar_testing/source_tree/water_heaters_testings/water_draw_scripts/ValveControl.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/acs37800_final_original_reference.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/max1238_root_duplicate.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/sensor_test_duplicate_of_whs.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DeltaTSchedule.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController2.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController_Conformance.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/controller/DrawController_FM.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/dcs/GetTemp.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/dcs/TempQuick.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/dcs/test.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/water_draw_scripts/FMTest.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `legacy_deprecated/old_duplicates/water_heaters_testings_source_tree/water_draw_scripts/ValveControl.py` | `LEGACY_HELPER` | Located in legacy/deprecated area. | Do not pull into active runtime without separate review. |
| `software/__init__.py` | `PACKAGE_INIT` | Package marker file. | Usually leave alone unless package layout changes. |
| `software/adc/__init__.py` | `PACKAGE_INIT` | Package marker file. | Usually leave alone unless package layout changes. |
| `software/adc/max1238.py` | `HARDWARE_HELPER` | Hardware-coupled terms found: adc, bus, i2c, max1238, smbus, smbus2. | Keep stable until hardware path is tested. |
| `software/common/__init__.py` | `PACKAGE_INIT` | Package marker file. | Usually leave alone unless package layout changes. |
| `software/common/hardware_map.py` | `CONFIG_OR_CONSTANTS` | Path/name suggests shared config, constants, pin map, or hardware map. | Good candidate for later canonical config review. |
| `software/diagnostics/__init__.py` | `PACKAGE_INIT` | Package marker file. | Usually leave alone unless package layout changes. |
| `software/power_monitoring/__init__.py` | `PACKAGE_INIT` | Package marker file. | Usually leave alone unless package layout changes. |
| `software/rs485_cta2045/__init__.py` | `PACKAGE_INIT` | Package marker file. | Usually leave alone unless package layout changes. |
| `software/valve_control/__init__.py` | `PACKAGE_INIT` | Package marker file. | Usually leave alone unless package layout changes. |
| `software/water_draw/__init__.py` | `PACKAGE_INIT` | Package marker file. | Usually leave alone unless package layout changes. |

## Excluded entrypoint-looking files

These files contain a main guard and should stay covered by `docs/audits/entrypoint_binning.md` unless manually reclassified.

- `software/diagnostics/read_acs37800_once.py`
- `software/diagnostics/read_adc_raw.py`
- `software/diagnostics/valve_gpio_check.py`
- `software/rs485_cta2045/gs10_modbus_test.py`
- `software/water_draw/whs.py`

## Manual review notes

- Review all `UNKNOWN_HELPER` rows.
- Review all `HARDWARE_HELPER` rows before any import or file move.
- Do not move active runtime code as part of this card.
- This audit is intentionally conservative; path/content clues should be manually checked before refactor work.

## Findings

- No active `software/power_monitoring/acs37800.py` helper module exists in the current tracked or working tree.
- Active ACS37800 access currently appears to be through `software/diagnostics/read_acs37800_once.py`, which is already classified as a diagnostic entrypoint.
- ACS37800 calibration/config data exists in `software/power_monitoring/acs37800_cal.json`.
- A legacy/reference ACS37800 implementation exists at `legacy_deprecated/old_duplicates/acs37800_final_original_reference.py`.
- The legacy ACS37800 reference contains useful register, calibration, I2C read, and CSV logging logic, but it should not be moved or imported during this audit.
- Future refactor candidate: extract reusable ACS37800 register/I2C/calibration logic into an active `software/power_monitoring/acs37800.py` helper.

---

# Source file: docs/audits/active_symbol_role_binning.md

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

---

# Source file: docs/audits/hardware_coupling_split.md

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
