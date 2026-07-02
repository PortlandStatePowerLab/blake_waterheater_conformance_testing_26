# Hardware Identity Verification

Status: VERIFIED
Verified date: 2026-07-01
Verified by: Blake Ellis

## Scope

This record captures completed hardware identity checks from the WH1 staging review.

## Verified items

- U11 is treated as `MAX1238EEE+` unless future physical board marking proves otherwise.
- U12 is confirmed as the `TXS0104E` level shifter path between Pi-side I2C and the MAX1238 side.
- U13 is confirmed as `ACS37800`.

## Notes

The ACS37800 physical identity is verified, but ACS37800 register-map use, scaling,
    and software reads remain pending until separately reviewed.

## Remaining related review items

- Resolve or archive any stale source document/CAD metadata that still names `MAX1239`.
- Verify ACS37800 register map and scaling before implementing real ACS37800 reads.
