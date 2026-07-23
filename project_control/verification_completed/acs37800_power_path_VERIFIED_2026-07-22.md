# ACS37800 Power Path Verification — WH1

Status: VERIFIED — INTEGRATION DEFERRED

- Verification date: 2026-07-22
- Verified by: Blake Ellis
- Station: WH1

## Scope and ownership boundary

This repository currently owns the WH1 sensor and controlled-water-draw path.
The team repository `power_scripts` branch owns the active ACS37800 reader,
calibration, and power-monitoring implementation. The two pathing systems have
not yet been unified. That integration work is deferred and is not a hardware
or scaling review failure. No team power files were copied into this repository.

## Verification method

The installed device was checked with read-only Linux I2C tools, and the full
team `power_scripts` branch at commit
`b30e53432d52829d22251d3de4d60621e280cefc` was inspected. No ACS configuration,
shadow, EEPROM, GPIO, relay, or other output write was performed.

## Station observations

- `i2cdetect -y 1` found the ACS37800 at address `0x60` and the MAX1238 at
  address `0x35`.
- Five reads of register `0x2A` returned changing voltage codes and small
  current codes, demonstrating usable live register communication.
- Register `0x20` returned VRMS raw `27682` and IRMS raw `80`.
- Register `0x25` returned `NUMPTSOUT = 525`.
- Register `0x2D` had the undervoltage status bit set, consistent with the
  existing team diagnostics.
- The water heater was in heat-pump mode; no resistive-heating event was
  intentionally forced for this review.

## Scaling and implementation evidence

The team branch contains an implemented ACS37800 register reader and WH1
calibration dated 2026-07-14:

- VRMS scale: `0.008658798283261802`
- IRMS scale: `0.0005444751783374581`
- VRMS offset: `5`
- IRMS offset: `57`
- Calibration references: `242.1 V` and `18.7 A`

Applying that implementation to the observed register `0x20` value produces
approximately `239.65 V`. The observed IRMS raw delta is below the configured
noise floor and therefore reports `0.0 A`, which is plausible without an
observed active heating event. Eight committed WH1 diagnostic records on the
team branch contain no recorded I2C errors; the latest also records matching
EEPROM and shadow configuration.

## Result

PASS — the ACS37800 address, usable register reads, register interpretation,
WH1 scaling, and active power-code ownership are verified. The previous open
review gate is closed.

Path unification and merging the sensor and power implementations remain a
separate integration task. This repository's local operator check remains
non-actuating and does not duplicate the team reader.
