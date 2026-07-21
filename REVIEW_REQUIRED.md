# WH1 Review Required

This file tracks remaining human, hardware, software, and documentation checks
before WH1 deployment moves past read-only diagnostics or controlled test runs.

Completed checks should be recorded as dated verification records under:

```text
project_control/verification_completed/
```

## Completed verification records

The following review gates have been completed and moved into verification records:

- Hardware identity verification:
  `project_control/verification_completed/hardware_identity_VERIFIED_2026-07-01.md`
- GPIO signal mapping verification:
  `project_control/verification_completed/gpio_signal_mapping_VERIFIED_2026-07-01.md`
- Valve relay operation verification:
  `project_control/verification_completed/valve_relay_operation_VERIFIED_2026-07-01.md`

## Still pending before full water-draw operation

### Hardware physical-presence checks

- Confirm whether any legacy `GPIO6` pulse-flow setup still exists physically.
- Confirm whether any direct `/sys/bus/w1` DS18B20 sensor wiring still exists physically.

### Software and data checks

- Confirm correct schedule CSVs before re-enabling any scheduled draw workflow.
- Confirm flow-transmitter calibration, gallons-per-minute scaling, and plausible
  ADC values during a controlled water-draw setup.
- Confirm temperature-transmitter scaling and plausible hot/cold readings on CH0
  and CH1 during a controlled water-draw setup.
- Verify ACS37800 register map, scaling, and usable software reads before replacing
  the safe placeholder operator check.

### Controlled-output check

- Verify `software/water_draw/whs.py --enable-output` stop behavior during a
  controlled lab run before routine use. The relay-specific verification gate is
  already complete.
