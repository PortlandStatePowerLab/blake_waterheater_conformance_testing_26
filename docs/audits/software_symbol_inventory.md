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
