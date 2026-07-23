# Open Review Items

Status: CLOSED
Last updated: 2026-07-22

All review items identified during this cleanup are closed. Completed checks
and their evidence records are listed below.

## Software, calibration, and controlled-run checks

None.

## Closed review items

### Closed by physical verification

- [x] The WH1 physical wiring inspection found no installed or active legacy
  `GPIO6` pulse-flow setup. Flow is routed through the custom PCB to MAX1238 CH2.
  See
  `../verification_completed/gpio6_flow_path_VERIFIED_2026-06-25.md`.
- [x] The WH1 physical wiring inspection found no installed direct DS18B20 or
  Raspberry Pi One-Wire temperature-sensor path. Hot, cold, and ambient
  temperature signals use the custom PCB and MAX1238 CH0, CH1, and CH4. See
  `../verification_completed/ds18b20_wiring_absence_VERIFIED_2026-06-25.md`.
- [x] Scheduled CSV-driven draws are deferred and are not required for the
  current WH1 deployment. The supported operator path is one draw per invocation
  through `bin/wh-draw --target-gal`; schedule CSVs and legacy
  controllers remain excluded under `legacy_deprecated/`. No schedule testing is
  required because no schedule-driven feature is being activated. Any future
  scheduler must be a separate entrypoint or service that calls the validated
  single-draw operation. See
  `../verification_completed/scheduled_draw_workflow_DEFERRED_2026-07-21.md`.
- [x] The installed SBN234 flow path and nominal 0.2-to-10.0-GPM scaling are
  accepted for current operational use based on a controlled draw, local-display
  comparison, and approximate 2.5-gallon bucket check. Precision calibration is
  deferred; no slope or intercept correction was applied. See
  `../verification_completed/flow_scaling_OPERATIONALLY_ACCEPTED_2026-07-22.md`.
- [x] The active single-draw path stopped at 2.501 gal for a 2.500-gal target,
  with clean valve opening and immediate cutoff. See
  `../verification_completed/water_draw_stop_behavior_VERIFIED_2026-07-22.md`.
- [x] Physical nameplate inspection confirmed Hasman HSM-100 hot/cold
  transmitters with a -50 to +150 degC, 4-20 mA range, exactly matching the
  active software endpoints and 12.5 degC-per-mA slope. Controlled-draw CH0/CH1
  values were stable and plausible. See
  `../verification_completed/WH1_temperature_plausibility_controlled_draw_2026-07-22.md`.
- [x] The ACS37800 at `0x60`, usable register reads, register interpretation,
  and WH1 scaling are verified against read-only station observations and the
  team `power_scripts` implementation. Sensor/power path unification remains a
  separate integration task. See
  `../verification_completed/acs37800_power_path_VERIFIED_2026-07-22.md`.

### Closed during repository cleanup

Closed 2026-07-20 by repository inspection and documentation review; these are
not new physical hardware verifications.

- [x] ADC channel constants use `software/station/station_hardware_map.py` as their active
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

New review gates, if identified, must receive a dated record in
`project_control/verification_completed/` before they are considered closed.
