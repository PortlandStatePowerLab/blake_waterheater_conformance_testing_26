# Open Review Items

Status: ACTIVE
Last updated: 2026-07-20

This file contains only checks that still require physical inspection, station
data, hardware documentation, or a controlled lab run. Completed repository and
documentation checks are recorded at the end of this file.

## Hardware identity and physical-presence checks

- [ ] Confirm whether any legacy `GPIO6` pulse-flow setup still exists physically.
- [ ] Confirm whether any direct `/sys/bus/w1` DS18B20 sensor wiring still exists physically.

## Software, calibration, and controlled-run checks

- [ ] Confirm the correct schedule CSVs before re-enabling a scheduled draw workflow.
- [ ] Verify flow-transmitter calibration, gallons-per-minute scaling, and
  plausible ADC values during a controlled water-draw setup.
- [ ] Verify temperature-transmitter scaling and plausible hot/cold readings on
  CH0 and CH1 during a controlled water-draw setup.
- [ ] Verify the ACS37800 register map, scaling, and usable software reads before
  replacing the safe placeholder operator check.
- [ ] Verify `software/water_draw/whs.py --enable-output` stop behavior during a
  controlled lab run before routine use.

## Closed during repository cleanup

Closed 2026-07-20 by repository inspection and documentation review; these are
not new physical hardware verifications.

- [x] ADC channel constants use `software/common/hardware_map.py` as their active
  software source of truth.
- [x] The stale U11 `MAX1239` EasyEDA library metadata is explicitly superseded
  by the displayed MAX1238 identity and the completed hardware identity record.
- [x] The stale U13 `030B3` EasyEDA library metadata is explicitly superseded by
  the displayed and verified `090B3` identity.
- [x] Word documents under `docs/reference_only/` are identified as historical,
  non-runtime references in the active repository index and deployment guidance.
- [x] Audit and crash-recovery documents are isolated from deployment/runtime
  instructions and identified as potentially stale.
- [x] The valve relay output, polarity, fail-safe behavior, and GPIO17 mapping are
  covered by completed verification records. The remaining controlled-run items
  above concern the full water-draw workflow, not the relay-specific gate.
- [x] Purchasing BOM exports resolve Q1 as MMBT3904, U14 as RAPC722BKZ, and T1 as
  BV302S12015; their datasheets now use those order-backed identities. The raw
  source exports remain outside the repository as requested.

## Completion rule

When a remaining item is physically or operationally verified, create or update
a dated record in `project_control/verification_completed/`, then remove it from
the open sections and add a concise checked entry above with the evidence path.
