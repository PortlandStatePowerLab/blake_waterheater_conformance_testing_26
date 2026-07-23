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

## 5. Valve dry-run only

```bash
python3 bin/valve-check
```

This must report dry-run behavior and must not touch GPIO17.

Record observed output in `test_records/`.

## 6. Output checks only after review

Do not run either command until relay polarity, wiring, load safety, fail-safe behavior, ADC values, flow scaling, and stop behavior are physically reviewed for the real station.

```bash
python3 bin/valve-check --enable-output --state off
python3 bin/wh-draw --target-gal 0.1 --enable-output
```

## Reference records

Completed or observed test records should be stored under:

```text
test_records/
```

Current initial Pi diagnostic record:

```text
test_records/WH1_initial_pi_test_2026-06-29.md
```
