# GPIO6 Flow-Path Physical Inspection

Status: VERIFIED
Verified date: 2026-06-25
Verified by: Blake Ellis
Station: WH1
Record prepared: 2026-07-21 from recovered inspection notes

## Scope

Confirm whether WH1 retains a legacy pulse-flow setup using Raspberry Pi BCM
`GPIO6` (physical pin 31), or whether the installed flow transmitter uses only
the current custom-PCB and MAX1238 analog acquisition path.

## Verification method

Physical inspection performed while completing the WH1 wiring work. The
inspection covered the Raspberry Pi connection, flow-meter field wiring, custom
PCB path, and MAX1238 flow-input assignment. The result was later reconciled
with the Rev A station design, Gerber fabrication files, and active deployment
documentation.

No continuity or electrical-open test of the PCB-side GPIO6 trace was performed.

## Expected result

- No dedicated flow-meter wire or active pulse-flow function uses BCM `GPIO6`.
- No flow-meter wire bypasses the custom PCB.
- The installed flow transmitter reaches the MAX1238 through the PCB and is
  acquired on CH2.

## Observed result

- The 40-pin Raspberry Pi ribbon cable was installed.
- No dedicated wire or active function associated with physical pin 31 / BCM
  `GPIO6` was identified.
- No flow-meter wire bypassed the custom PCB.
- The flow transmitter was connected only through the custom PCB / MAX1238 CH2
  path.
- No inaccessible field wiring or other physical uncertainty was reported.
- No inspection photos were retained.
- Rev A top- and bottom-copper Gerber review found that the plated GPIO6 header
  pad has no departing trace, separate via, or copper-pour connection. The pad
  is isolated from the functional PCB circuitry.

## Result

PASS

No legacy GPIO6 pulse-flow setup was found installed or active on WH1. The
legacy `FMPIN = 6` scripts remain historical only and are not part of the active
deployment.

## Notes

This verification establishes the installed signal path and absence of a legacy
GPIO6 flow setup. The Gerbers establish that GPIO6 is intentionally unconnected
in the Rev A fabrication design. No continuity test was performed on the
as-built PCB, so the record does not independently certify the physical board as
electrically open.

The inspection date records when Blake Ellis completed the physical wiring
inspection. This document was prepared retrospectively on 2026-07-21 from the
recovered inspection details and repository evidence.

## Follow-up items

None for the legacy GPIO6 pulse-flow physical-presence review item.
