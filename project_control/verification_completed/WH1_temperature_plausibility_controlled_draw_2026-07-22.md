# WH1 Temperature Engineering-Range and Operational-Scaling Verification

Status: VERIFIED
Verified date: 2026-07-22
Verified by: Blake Ellis
Station: WH1

## Scope

Verify the installed hot/cold temperature-transmitter engineering range and
confirm plausible CH0/CH1 temperature behavior during a controlled water draw.

## Installed devices

Physical nameplate inspection confirmed:

- Manufacturer: Hasman
- Model: HSM-100
- Output: 4-20 mA
- Supply: 24 VDC
- Engineering range: -50 to +150 degC
- nameplate accuracy: 0.2%.

The accuracy statement is recorded exactly as shown. It is not converted to an
absolute temperature tolerance because no HSM-100 datasheet basis for the
percentage was reviewed.

## Nominal conversion

- 4 mA = -50 degC
- 20 mA = +150 degC
- Engineering span = 200 degC
- Current span = 16 mA
- Linear slope = 12.5 degC per mA

These endpoints exactly match the active nominal configuration in
`software/sensors/sensor_conversion_math.py`.

## Controlled-draw observations

- Hot CH0: approximately 39.1 to 47.7 degC, rising smoothly
- Cold CH1: approximately 23.1 to 24.4 degC, stable
- Ambient CH4: approximately 21.3 to 23.1 degC
- Independent ambient observation: 72 degF, approximately 22.2 degC
- No channel reversals, dropouts, saturation, or implausible values were
  reported

## Result

PASS - VERIFIED

The installed HSM-100 engineering range matches the active software conversion,
and the controlled-draw values demonstrate plausible operational scaling.

## Limitation

This verification is not an independent accuracy calibration. A calibrated
reference thermometer would be required only for a separate accuracy claim.

## Evidence

`../../test_records/sensor_scaling_checks/WH1_temperature_plausibility_controlled_draw_2026-07-22.md`

## Follow-up items

None for the temperature engineering-range/scaling review item.
