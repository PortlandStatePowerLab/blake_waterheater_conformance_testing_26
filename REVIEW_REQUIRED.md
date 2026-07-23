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
- GPIO6 flow-path physical inspection:
  `project_control/verification_completed/gpio6_flow_path_VERIFIED_2026-06-25.md`
- DS18B20 wiring physical inspection:
  `project_control/verification_completed/ds18b20_wiring_absence_VERIFIED_2026-06-25.md`
- Scheduled draw workflow deployment decision:
  `project_control/verification_completed/scheduled_draw_workflow_DEFERRED_2026-07-21.md`
- Flow scaling operational acceptance:
  `project_control/verification_completed/flow_scaling_OPERATIONALLY_ACCEPTED_2026-07-22.md`
- Water-draw stop behavior verification:
  `project_control/verification_completed/water_draw_stop_behavior_VERIFIED_2026-07-22.md`
- Temperature engineering-range and operational-scaling verification:
  `project_control/verification_completed/WH1_temperature_plausibility_controlled_draw_2026-07-22.md`
- ACS37800 power-path verification:
  `project_control/verification_completed/acs37800_power_path_VERIFIED_2026-07-22.md`

## Still pending from this cleanup

None.

Sensor/power path unification remains separate integration work and is not an
open hardware-verification gate.
