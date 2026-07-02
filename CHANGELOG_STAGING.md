# WH1 Staging Changelog

Date: 2026-06-25

## Copied or preserved

- Hardware schematics, PCB source/fabrication material, wiring diagrams, and
  datasheets are staged under `hardware/` and `docs/wiring/`.
- Audit reports and crash recovery files are staged under `docs/audit_reports/`.
- Historical scripts, generated files, old duplicates, GPIO6 flow scripts, and
  direct DS18B20 scripts are kept under `legacy_deprecated/`.
- Active shared constants are in `software/common/hardware_map.py`.
- The MAX1238 ADC driver is staged in `software/adc/max1238.py`.

## Fixed or completed

- Active ADC constants preserve ADC_VREF 4.096, cold on CH1, flow on CH2, and
  valve control on GPIO17.
- New top-level staging documents define deployable files, review items, and
  safe first-test order.
- New diagnostics are dry-run or read-only by default.
- Water draw control is dry-run unless `--enable-output` is explicitly passed.

## Moved to legacy

- GPIO6 flow-count scripts.
- Direct DS18B20 scripts.
- Generated caches/logs and old duplicate source copies.
- Broken or incomplete historical experiments.

## Verification records added

- Hardware identity verification was recorded in:
  `project_control/verification_completed/hardware_identity_VERIFIED_2026-07-01.md`
- GPIO signal mapping verification was recorded in:
  `project_control/verification_completed/gpio_signal_mapping_VERIFIED_2026-07-01.md`
- Valve relay operation verification was recorded in:
  `project_control/verification_completed/valve_relay_operation_VERIFIED_2026-07-01.md`

## Still flagged or pending

- Stale ADC part-name references may remain in copied source material or CAD metadata.
- Schedule CSV expectations require review before scheduled operation.
- Legacy GPIO6 pulse-flow wiring requires physical-presence review.
- Legacy direct DS18B20 wiring requires physical-presence review.
- Flow transmitter calibration and gallons-per-minute scaling require review.
- Temperature transmitter scaling and hot/cold channel readings require review.
- ACS37800 register map, scaling, and usable software reads require review before replacing the safe placeholder diagnostic.

## Still required before full Pi actuation

- Run only the safe Pi sequence in
  `deployment/test_run_order/FIRST_PI_TEST_SEQUENCE.md`.
- Verify I2C device presence before any sensor read.
- Confirm completed valve relay verification record before using valve GPIO output checks.
- Verify ADC values, flow scaling, temperature scaling, and stop behavior before routine `software/water_draw/whs.py --enable-output` use.
