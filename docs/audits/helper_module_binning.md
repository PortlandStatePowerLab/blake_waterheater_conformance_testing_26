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
