# Datasheets

Reviewed component and field-device datasheets for the WH1 station.

PCB component filenames use
`<REFDES>_<FULL_COMPONENT_ID>_<common_name_or_purpose>.pdf`. Field devices use a
clear `FIELD_<ROLE>` identifier rather than an invented PCB reference designator.
The station water heater uses `WH1`. A `REFERENCE_` prefix is reserved for related
material that cannot be tied to an exact installed or purchased component.

Datasheets are hardware reference documents, not the software source of truth
for live pin, channel, or address assignments. Those assignments remain in
`software/station/station_hardware_map.py`. Confirm uncertain part numbers and reference
designators against the schematic or BOM before renaming a file.

## BOM reconciliation

Power Lab purchasing exports from 2025 Spring through 2026 Spring resolve three
schematic-library conflicts:

- Q1 was purchased as MMBT3904 (`4878-MMBT3904CT-ND`).
- U14 was purchased as RAPC722BKZ (`SC3832-ND`).
- T1 was purchased as BV302S12015 (`3388-BV302S12015-ND`).

Their datasheets therefore use the actual BOM identities. The older EasyEDA
library names remain documented as stale metadata in the hardware identity
verification record.
