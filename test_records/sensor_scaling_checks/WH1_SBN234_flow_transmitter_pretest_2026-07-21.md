# WH1 SBN234 Flow-Transmitter Pre-Test Record

Status: PRE-TEST COMPLETE / CALIBRATION PENDING
Evidence reviewed: 2026-07-21
Evidence provided by: Blake Ellis
Station: WH1

## Scope

Identify the installed WH1 flow transmitter, document its nominal transfer
function and wiring, and establish the expected values for a later controlled
flow-calibration test.

## Identification evidence

Physical nameplate and installed-device photographs identify the device as an
ifm electronic SBN234 mechatronic flow meter.

- Published flow range: 0.2 to 10.0 GPM (10 to 600 GPH)
- Process connection: 3/4-inch NPT female
- Supply: 18 to 30 VDC; WH1 provides nominal 24 VDC
- Local process-value display and configuration buttons
- IO-Link 1.1, UL, CE, and IP65/IP67 markings visible
- No serial-number-specific calibration certificate, calibration date, seal, or
  calibration sticker was identified in the supplied photographs

## Installed signal path

- Brown / BN: +24 VDC
- Blue / BU: GND / L-
- White / WH: 4-20 mA signal, M12 pin 2 / OUT2
- White analog output routes through the custom PCB to MAX1238 CH2
- Black / BK, M12 pin 4 / OUT1, is not part of the documented PCB analog
  measurement path and remains unused unless separately physically verified

## Nominal conversion basis

The installed SBN234 range establishes:

- 4.00 mA = 0.2 GPM
- 20.00 mA = 10.0 GPM

```text
flow_gpm = 0.2 + ((loop_current_ma - 4.0) / 16.0) * 9.8
```

Across the nominal 120-ohm PCB shunt:

- 4.00 mA = 0.480 V, approximately 480 MAX1238 counts
- 20.00 mA = 2.400 V, approximately 2400 MAX1238 counts

The count estimates use a 4.096 V reference and 4096 conversion steps.

## Independent reference method

Use a graduated container and stopwatch, or preferably collected water mass and
elapsed time when a suitable scale is available. Compare:

1. Collected-volume or collected-mass reference GPM
2. SBN234 local displayed GPM
3. MAX1238 CH2/software-calculated GPM

The SBN234 display is not an independent calibration reference because its
display and 4-20 mA output originate from the same sensor.

## Result

PRE-TEST COMPLETE

The installed device and correct nominal transfer function are confirmed. This
record does not close flow calibration: no controlled collection test, error
calculation, or calibration acceptance decision has yet been recorded.

## Follow-up items

- [ ] Run a controlled collected-volume or collected-mass flow test.
- [ ] Record elapsed time, reference GPM, SBN234 display, CH2 raw counts, and
  software-calculated GPM.
- [ ] Define and apply an acceptance tolerance before assigning PASS or FAIL.
