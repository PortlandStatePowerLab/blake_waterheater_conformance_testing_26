# First Pi Test Sequence

Run from `/home/pi/wh1` on the Raspberry Pi after copying the manifest-listed runtime files.

This file is a procedure. Observed test results belong in `test_records/`.

## 1. Static checks

```bash
python3 -m compileall software
python3 -m pip install -r software/requirements.txt
```

Stop if Python compilation fails or dependencies cannot be installed.

## 2. I2C visibility

```bash
ls -l /dev/i2c-1
i2cdetect -y 1
```

Expected review targets:

- MAX1238 ADC at `0x35`
- ACS37800 at `0x60`

Stop if expected devices are absent.

## 3. Read-only ADC check

```bash
python3 bin/adc-raw
```

Confirm channels print plausible raw counts and voltages for CH0, CH1, CH2, CH3, and CH4.

Expected channel map:

- CH0: hot temperature transmitter
- CH1: cold temperature transmitter
- CH2: flow transmitter
- CH3: future input
- CH4: ambient LM35

Stop if reads fail or values are saturated unexpectedly.

Record observed output in `test_records/`.

## 4. ACS37800 review-required check

```bash
python3 bin/power-monitor-check
```

This script is intentionally a safe stub until the usable ACS37800 register map is verified.

It should report:

```text
STATUS=REVIEW_REQUIRED
```

Do not add ACS37800 register reads until the datasheet, active part variant, register map, and scaling are reviewed.

Record observed output in `test_records/`.

## 5. Controlled valve pulse

```bash
python3 bin/valve-check
```

This performs the default 0.25-second open pulse and then returns GPIO17 LOW.

Record observed output in `test_records/`.

## 6. Controlled output checks

```bash
python3 bin/valve-check --state off
python3 bin/wh-draw --target-gal 0.1
```

The valve command above is close-only. The water-draw command constructs the
station ADC and valve, runs one controlled 0.1-gallon draw, and releases both
hardware resources.

## Reference records

Completed or observed test records should be stored under:

```text
test_records/
```

Current initial Pi diagnostic record:

```text
test_records/WH1_initial_pi_test_2026-06-29.md
```
