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

The valve operator check at
`bin/valve-check` remains dry-run by default.
Hardware output still requires the explicit `--enable-output` flag.

This verification clears the relay-specific review gate. Full water-draw operation
still requires the consolidated calibration and controlled-run checks listed in
`project_control/review_pending/open_review_items.md`.

The matching relay and flyback-diode datasheets are now stored as
`hardware/datasheets/RL1_G5LE-1A4_DC24_valve_relay.pdf` and
`hardware/datasheets/D2_1N4007W_flyback_diode.pdf`. Repository paths reviewed and
updated 2026-07-20.

## Remaining related review items

- Verify temperature-transmitter scaling and plausible hot/cold readings during a
  controlled water-draw setup.

Repository review note, 2026-07-22: the flow-scaling operational-acceptance and
full water-draw stop-behavior gates are now closed by their separate completed
records. This note does not change the original relay verification date.
