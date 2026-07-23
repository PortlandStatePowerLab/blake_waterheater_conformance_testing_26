# WH1 2.5-Gallon Controlled Draw Record

Status: PASS WITH CALIBRATION LIMITATION
Test date: 2026-07-22 (report date; exact run date was not separately provided)
Tested by: Blake Ellis
Station: WH1

## Scope

Record one controlled draw using the active single-draw software path and assess
functional volume integration, SBN234-to-software flow agreement, target-stop
behavior, and fail-safe valve closure.

## Test configuration

- Requested target: 2.500 gal
- Active operator path: `software/water_draw/whs.py --target-gal`
- Installed flow transmitter: ifm electronic SBN234
- Nominal transmitter range: 0.2 to 10.0 GPM
- Independent reference: approximate bucket level only; no precisely marked
  vessel, weighing scale, or external calibrated flow meter was used

## Observed result

- Software-reported final volume: 2.501 gal
- Software steady-state flow: approximately 3.33 to 3.38 GPM
- SBN234 local display after the hydraulic transient: approximately 3.2 GPM
- Observed instantaneous difference: software approximately 0.15 GPM high
- Hot-water temperature in supplied output: approximately 39.1 to 43.8 °C
- Cold-water temperature in supplied output: approximately 23.1 to 23.8 °C
- Ambient temperature in supplied output: approximately 21.3 to 23.0 °C
- Independent room observation: 72 °F, approximately 22.2 °C
- Physical observation: bucket reached approximately the expected 2.5-gallon
  level
- Valve behavior: clean opening and immediate cutoff at the target
- No CH2 raw-count series was retained with the reported result

## Result

PASS WITH CALIBRATION LIMITATION

The run verifies functional volume control, plausible operational flow scaling,
and immediate valve cutoff at the requested target. Blake Ellis accepts the
installed SBN234 factory calibration and present nominal software scaling for
current WH1 operational use.

This run is not an independent precision calibration. The SBN234 display and
4-20 mA output originate from the same sensor, and the bucket level was only an
approximate physical check.

## Calibration decision

Do not derive or apply a slope, intercept, or other correction from this single
run. Repeat with a precisely marked 2.5-gallon reference or collected-water mass
before changing calibration values.

## Follow-up items

- Precision calibration is deferred and is not a current deployment gate.
- Open a new calibration task before changing the flow slope or intercept.
