# Open Review Items

Status: ACTIVE
Last updated: 2026-07-01

This file tracks WH1 review items that are still open after the completed hardware identity,
    GPIO signal mapping, and valve relay operation verification records were added.

## Hardware physical-presence checks

- [ ] Confirm whether any legacy `GPIO6` pulse-flow setup still exists physically.
- [ ] Confirm whether any direct `/sys/bus/w1` DS18B20 sensor wiring still exists physically.

## Software and data checks

- [ ] Confirm correct schedule CSVs before re-enabling any scheduled draw workflow.
- [ ] Confirm flow transmitter calibration and gallons-per-minute scaling.
- [ ] Confirm temperature transmitter scaling and cold/hot channel readings on CH1 and CH0.
- [ ] Verify ACS37800 register map, scaling, and usable software reads before replacing
    the safe placeholder diagnostic.
- [ ] Keep ADC channel constants sourced from `software/common/hardware_map.py`.

## Controlled-output checks

- [ ] Confirm ADC values are plausible during real water-draw setup.
- [ ] Confirm flow scaling during real water-draw setup.
- [ ] Confirm temperature scaling during real water-draw setup.
- [ ] Confirm `software/water_draw/whs.py --enable-output` stop behavior before routine use.

## Document cleanup checks

- [ ] Resolve, supersede, or archive stale source document or CAD metadata that still names `MAX1239`.
- [ ] Keep Word documents in `docs/reference_only/` treated as historical unless no better source exists.
- [ ] Keep audit reports and crash recovery notes from being used as deployment instructions.

## Completion rule

When an item is completed, create a dated verification record in:

```text
project_control/verification_completed/
```

Then update this file by checking off the item or moving it into a completed verification
    record.
