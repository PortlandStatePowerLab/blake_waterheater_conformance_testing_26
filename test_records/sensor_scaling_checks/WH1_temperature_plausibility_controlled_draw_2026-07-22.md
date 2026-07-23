# WH1 Temperature Plausibility Controlled-Draw Record

Status: PASS
Test date: 2026-07-22 (report date; exact run date was not separately provided)
Tested by: Blake Ellis
Station: WH1

## Scope

Record hot, cold, and ambient temperature behavior during a controlled
2.500-gallon draw and determine whether the reported channel values are stable,
ordered correctly, and physically plausible.

## Command

```bash
python3 whs.py \
  --target-gal 2.5 \
  --max-run-minutes 2 \
  --enable-output
```

The command was run from the station's `software/water_draw` directory.

## Observed result

- Hot-water temperature increased smoothly from approximately 39.1 degC to
  47.7 degC over the complete controlled draw.
- Cold-water temperature remained approximately 23.1 to 24.4 degC.
- Ambient temperature remained approximately 21.3 to 23.1 degC.
- Independent room-temperature observation: 72 °F, equivalent to approximately
  22.2 °C.
- The software ambient value bracketed and closely agreed with the independent
  room-temperature observation.
- Hot remained consistently warmer than cold.
- No discontinuities, impossible values, channel reversals, or obvious sensor
  dropouts were observed in the supplied output.
- CH0 and CH1 raw counts were not retained in the supplied run log.
- No independent hot-water or cold-water reference thermometer reading was
  supplied.
- Physical nameplate inspection identified both installed temperature
  transmitters as Hasman HSM-100 devices with 4-20 mA output, 24 VDC supply,
  and a -50 to +150 degC engineering range.
- nameplate accuracy: 0.2%.

## Result

PASS

The observed CH0 hot, CH1 cold, and CH4 ambient behavior is stable and physically
plausible for the controlled draw. The ambient channel also agrees with the
independent 72 °F room observation. The physically inspected HSM-100 range
exactly matches the active nominal software endpoints: 4 mA = -50 degC and
20 mA = +150 degC. The corresponding linear slope is 12.5 degC per mA.

## Limitation

This record verifies the installed engineering range and operational scaling.
It does not claim independent accuracy calibration. An independent calibrated
thermometer would be required for a separate accuracy-calibration claim.

## Follow-up items

None for the engineering-range/scaling review item. Do not change temperature
slope or intercept from this operational verification.
