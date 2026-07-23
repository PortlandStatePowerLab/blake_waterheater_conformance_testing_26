# Water-Draw Stop Behavior Verification

Status: VERIFIED
Verified date: 2026-07-22
Verified by: Blake Ellis
Station: WH1

## Scope

Verify target-volume stop behavior and valve closure during one controlled use
of the active `bin/wh-draw` single-draw path.

## Verification method

Run a controlled draw with a 2.500-gallon target while observing software volume
integration and physical valve behavior at the target.

## Expected result

- Valve opens cleanly after the explicit output-enabled command.
- Software stops the draw at the requested target.
- Valve command clears immediately when the draw ends.

## Observed result

- Target volume: 2.500 gal
- Software-reported final volume: 2.501 gal
- Valve opened cleanly.
- Valve cutoff was immediate at the target.
- The bucket reached approximately the expected 2.5-gallon level.

## Result

PASS

Functional target-volume control and fail-safe valve closure were verified for
the reported controlled draw.

## Evidence

`../../test_records/sensor_scaling_checks/WH1_controlled_draw_2.5gal_2026-07-22.md`

## Follow-up items

None for the controlled target-stop review gate. Flow precision calibration
remains a documented future improvement rather than a current deployment gate.
