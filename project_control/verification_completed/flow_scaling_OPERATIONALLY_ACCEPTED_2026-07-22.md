# Flow Scaling Operational Acceptance

Status: VERIFIED WITH ACCEPTED LIMITATION
Verified date: 2026-07-22
Verified by: Blake Ellis
Station: WH1

## Scope

Determine whether the installed SBN234 flow signal and current nominal software
scaling are plausible and acceptable for current WH1 controlled operation.

## Verification method

A 2.500-gallon controlled draw compared the software flow and integrated volume
against the SBN234 local display and an approximate bucket-level observation.
The device identification and nominal 0.2-to-10.0-GPM transfer function were
established in the pre-test record.

## Observed result

- Software steady-state flow: approximately 3.33 to 3.38 GPM
- SBN234 display after hydraulic transient: approximately 3.2 GPM
- Software/display difference: approximately 0.15 GPM, software high
- Software-reported final volume: 2.501 gal for a 2.500-gal target
- Bucket level: approximately the expected 2.5-gallon level
- No CH2 raw-count series was retained

## Result

PASS - OPERATIONALLY ACCEPTED

The flow path and nominal scaling are accepted for current WH1 use. This is an
operational acceptance, not an independent precision calibration.

## Limitations

- The local display and analog output share the same SBN234 sensing element.
- The bucket was not a precise volumetric or mass reference.
- No external calibrated reference meter was used.
- No slope or intercept correction is justified by this run.

## Evidence

- `../../test_records/sensor_scaling_checks/WH1_SBN234_flow_transmitter_pretest_2026-07-21.md`
- `../../test_records/sensor_scaling_checks/WH1_controlled_draw_2.5gal_2026-07-22.md`

## Follow-up items

Precision calibration is deferred. Before changing flow calibration values,
repeat the test using a precisely marked or weighed 2.5-gallon reference.
