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
- Confirm flow transmitter calibration and gallons-per-minute scaling.
- Confirm temperature transmitter scaling and cold/hot channel readings on CH1 and CH0.
- Keep ADC channel constants sourced from `software/common/hardware_map.py`.
- Verify ACS37800 register map, scaling, and usable software reads before replacing the safe placeholder diagnostic.

### Controlled-output checks

- `software/diagnostics/valve_gpio_check.py --enable-output` may be used only after confirming the completed valve relay verification record.
- `software/water_draw/whs.py --enable-output` still requires ADC values, flow scaling, temperature scaling, and stop behavior to be reviewed on the real station before routine use.

## Documents

- Treat Word documents in `docs/reference_only/` as historical unless no better source exists.
- Audit reports and crash recovery notes may mention stale script behavior; do not use them as deployment instructions.
- Resolve, supersede, or archive any stale source document or CAD metadata that still names `MAX1239`.
