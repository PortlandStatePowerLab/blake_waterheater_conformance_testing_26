# First Pi Test Sequence

Run from `/home/pi/wh1` on the Raspberry Pi after copying the manifest-listed
runtime files.

## 1. Static checks

```bash
python3 -m compileall software
python3 -m pip install -r software/requirements.txt
```

## 2. I2C visibility

```bash
ls -l /dev/i2c-1
    crw-rw---- 1 root i2c 89, 1 Jun 29 11:17
i2cdetect -y 1
```

Expected review targets:

- MAX1238 ADC at `0x35`
- ACS37800 at `0x60`

Stop if expected devices are absent.

## 3. Read-only ADC check

```bash
python3 software/diagnostics/read_adc_raw.py
```

Confirm channels print plausible raw counts and voltages for CH0, CH1, CH2, CH3,
and CH4. Stop if reads fail or values are saturated unexpectedly.

initial Test: PASS
    ADC part: MAX1238EEE+
    12C bus: 1
    12C address: 0x35
    ADC_VREF: 4.096V
    CH0 hot_temp_transmitter: raw=1192 voltage=1.923 V
    CH1 cold_temp_transmitter: raw=1157 voltage=1.1573 V
    CH2 flow_transmitter: raw= 480 voltage=0.4801 V
    CH3 future input: raw=   1 voltage=0.0010 V  <-why 3 spaces here?
    CH4 ambient_lm35: raw= 225 voltage=0.2251 V  <- why 2 spaces here?

## 4. ACS37800 review-required check

```bash
python3 software/diagnostics/read_acs37800_once.py
```

This script is intentionally a safe stub until the usable ACS37800 register map
is verified. Do not add register reads until the datasheet and active part
variant are reviewed.

inital test: PASS
    STATUS=REVIEW_REQUIRED
    ACS37800 expected I2C address: 0x60
    no I2C register read was attempted.
    Verify ACS37800 part variant, register map, and scaling before adding reads.

## 5. Valve dry-run only

```bash
python3 software/diagnostics/valve_gpio_check.py
```

This must report dry-run behavior and must not touch GPIO17.

## 6. Output checks only after review

Do not run either command until relay polarity, wiring, load safety, and
fail-safe behavior are physically verified:

```bash
python3 software/diagnostics/valve_gpio_check.py --enable-output --state off
python3 software/water_draw/whs.py --target-gal 0.1 --enable-output
```

## Reference Records

Completed or observed test records should be stored under:

```text
test_records/
```

Current initial Pi diagnostic record:

```text
test_records/WH1_initial_pi_test_2026-06-29.md
```
