# Valve Relay Operation Verification

Status: VERIFIED
Verified date: 2026-07-01
Verified by: Blake Ellis

## Scope

This record captures completed verification for the WH1 valve relay GPIO output path.

## Verified items

- Valve relay output behavior was physically checked.
- Valve relay active polarity was reviewed.
- Valve fail-safe behavior was reviewed.
- `GPIO17` is the valve relay control path.

## Notes

The valve GPIO diagnostic remains dry-run by default. Hardware output still requires the explicit `--enable-output` flag.

This verification clears the relay-specific review gate, but full water-draw operation still requires ADC values, flow scaling, temperature scaling, and stop behavior to be reviewed on the real station.

## Remaining related review items

- Confirm ADC values are plausible during real water-draw setup.
- Confirm flow transmitter calibration and gallons-per-minute scaling.
- Confirm temperature transmitter scaling and hot/cold channel readings.
- Confirm `software/water_draw/whs.py --enable-output` stop behavior before routine use.
