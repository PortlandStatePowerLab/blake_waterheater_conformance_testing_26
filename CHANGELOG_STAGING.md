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

## Flagged

- Stale ADC part-name references in copied source material.
- ACS37800 DIO GPIO mapping requires schematic/board review.
- Valve relay polarity and fail-safe behavior require physical verification.
- Schedule CSV expectations require review before scheduled operation.

## Still required before Pi actuation

- Run only the safe Pi sequence in
  `deployment/test_run_order/FIRST_PI_TEST_SEQUENCE.md`.
- Verify I2C device presence before any sensor read.
- Verify relay polarity with a meter/load-safe setup before enabling GPIO17.
