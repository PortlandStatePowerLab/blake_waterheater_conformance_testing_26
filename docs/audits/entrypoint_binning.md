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
- `UNKNOWN_ENTRYPOINT`: 1

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

- Initial bin: `UNKNOWN_ENTRYPOINT`
- Evidence: `main_guard`
- Hardware-coupled: yes
- Notes: Hardware-coupled runnable candidate outside diagnostics/legacy; needs review. Module note: ADC-based WH1 water draw control for the current PCB-ribbon hardware.

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
