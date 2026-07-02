# GPIO Signal Mapping Verification

Status: VERIFIED
Verified date: 2026-07-01
Verified by: Blake Ellis

## Scope

This record captures completed GPIO and signal-mapping checks from the WH1 staging review.

## Verified items

- Valve relay control path uses `GPIO17`.
- ACS37800 `DIO_0` maps to `GPIO18`.
- ACS37800 `DIO_1` maps to `GPIO26`.

## Notes

GPIO17 is the valve relay control path through the ribbon cable.

The ACS37800 physical DIO-to-GPIO mapping is verified, but ACS37800 register-map use,
    scaling, and software reads remain pending until separately reviewed.

## Remaining related review items

- Confirm whether any legacy `GPIO6` pulse-flow setup still exists physically.
- Confirm whether any direct `/sys/bus/w1` DS18B20 sensor wiring still exists physically.
