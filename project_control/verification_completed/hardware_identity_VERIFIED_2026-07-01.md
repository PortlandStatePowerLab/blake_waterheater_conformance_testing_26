# Hardware Identity Verification

Status: VERIFIED
Verified date: 2026-07-01
Verified by: Blake Ellis

## Scope

This record captures completed hardware identity checks from the WH1 staging review.

## Verified items

- U11 is treated as `MAX1238EEE+` unless future physical board marking proves otherwise.
- U12 is confirmed as `TXS0104EQPWRQ1`, the level-shifter path between Pi-side I2C and the MAX1238 side.
- U13 is confirmed as `ACS37800KMACTR-090B3-I2C`.
- U9 and U10 are identified as `LM324ANSR` sensor-buffer op amps.
- U17 is identified as `LM35DMX/NOPB`, the ambient-temperature sensor.
- U18 is identified as `MOV-14D431K`, the surge-protection varistor.
- D2 is identified as `1N4007W`, the valve-relay flyback diode.
- RL1 is identified as `G5LE-1A4 DC24`, the valve relay.
- Q1 is identified by the purchasing BOM as `MMBT3904`.
- U14 is identified by the purchasing BOM as `RAPC722BKZ`.
- T1 is identified by the purchasing BOM as `BV302S12015`.

## Notes

The ACS37800 physical identity is verified, but ACS37800 register-map use, scaling,
    and software reads remain pending until separately reviewed.

The normalized matching datasheets are:

- `hardware/datasheets/U11_MAX1238EEE+_adc.pdf`
- `hardware/datasheets/U12_TXS0104EQPWRQ1_i2c_level_shifter.pdf`
- `hardware/datasheets/U13_ACS37800KMACTR-090B3-I2C_power_monitor.pdf`
- `hardware/datasheets/U9_U10_LM324ANSR_sensor_buffer_opamp.pdf`
- `hardware/datasheets/U17_LM35DMX-NOPB_ambient_temperature_sensor.pdf`
- `hardware/datasheets/U18_MOV-14D431K_surge_protection_varistor.pdf`
- `hardware/datasheets/D2_1N4007W_flyback_diode.pdf`
- `hardware/datasheets/RL1_G5LE-1A4_DC24_valve_relay.pdf`
- `hardware/datasheets/Q1_MMBT3904_npn_transistor.pdf`
- `hardware/datasheets/U14_RAPC722BKZ_locking_dc_power_jack.pdf`
- `hardware/datasheets/T1_BV302S12015_1.5VA_step_down_transformer.pdf`

## Repository identity review update

Updated 2026-07-20 during datasheet and purchasing-BOM normalization. The Power
Lab purchasing exports for 2025 Spring, 2025 Summer, 2025 Fall, and 2026 Spring
were reviewed as source evidence without copying the unedited exports into this
repository. The purchasing records resolve Q1 as MMBT3904, U14 as RAPC722BKZ,
and T1 as BV302S12015.

The EasyEDA source retains conflicting library metadata for U11 (`MAX1239`) and
U13 (`ACS37800KMACTR-030B3-I2C`). For repository documentation and datasheet
naming, that stale library metadata is superseded by the displayed schematic
labels, purchasing records, and this completed verification record. The same
library-source mismatch applies to Q1, U14, and T1; the purchasing BOM identities
supersede those stale library names for repository documentation and datasheets.

## Remaining related review items

- Verify ACS37800 register map and scaling before implementing real ACS37800 reads.
