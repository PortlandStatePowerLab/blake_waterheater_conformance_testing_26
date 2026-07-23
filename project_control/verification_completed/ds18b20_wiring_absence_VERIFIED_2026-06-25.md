# DS18B20 Wiring Physical Inspection

Status: VERIFIED
Verified date: 2026-06-25
Verified by: Blake Ellis
Station: WH1
Record prepared: 2026-07-21 from recovered inspection notes

## Scope

Confirm whether WH1 retains any legacy DS18B20 or other direct Raspberry Pi
One-Wire temperature-sensor wiring, and confirm the installed temperature-signal
paths used by the current station.

## Verification method

Physical wiring inspection performed while completing the WH1 wiring work. The
inspection covered the temperature sensors, Raspberry Pi header connections,
field wiring, custom PCB, and MAX1238 temperature-input assignments. The result
was later reconciled with the documented WH1 system architecture.

No dedicated One-Wire bus scan or conductor-by-conductor continuity test was
recorded.

## Expected result

- No DS18B20 probe or other direct One-Wire temperature sensor is installed.
- No temperature-sensor wiring connects directly to the Raspberry Pi or bypasses
  the custom PCB.
- The hot and cold temperature transmitters use MAX1238 CH0 and CH1.
- The PCB-mounted LM35 ambient sensor uses MAX1238 CH4.

## Observed result

- No DS18B20 probe or three-wire digital temperature sensor was found.
- No temperature sensor was wired directly to the Raspberry Pi header.
- No temperature-sensor wiring bypassed the custom PCB.
- The hot temperature transmitter was connected through the PCB to MAX1238
  AIN0 / CH0.
- The cold temperature transmitter was connected through the PCB to MAX1238
  AIN1 / CH1.
- The LM35 was mounted directly on the PCB and connected to MAX1238 AIN4 / CH4.
- No inaccessible field wiring or other physical uncertainty was reported.
- No inspection photos were retained.

## Result

PASS

No direct DS18B20 or Raspberry Pi One-Wire temperature-sensor wiring was found
installed on WH1. The legacy `/sys/bus/w1` scripts remain historical only and
are not part of the active deployment.

## Notes

This verification establishes the installed temperature-sensor architecture by
visual wiring inspection. It does not claim a negative One-Wire bus-scan result
or conductor-by-conductor continuity measurement.

The inspection date records when Blake Ellis completed the physical wiring
inspection. This document was prepared retrospectively on 2026-07-21 from the
recovered inspection details and repository evidence.

## Follow-up items

None for the direct DS18B20 wiring physical-presence review item.
