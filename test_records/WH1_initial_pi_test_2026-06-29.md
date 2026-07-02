# WH1 Initial Pi Diagnostic Test

Status: PASS
Test date: 2026-06-29
Tested by: Blake Ellis
Station: WH1 / Raspberry Pi staging target

## Scope

This record captures observed output from the first safe Pi diagnostic sequence.

The matching procedure lives in:

`deployment/test_run_order/FIRST_PI_TEST_SEQUENCE.md`

## ADC raw read diagnostic

Command:

```bash
python3 software/diagnostics/read_adc_raw.py
```

Observed Results:
    ADC part: MAX1238eee+
    I2C bus: 1
    I2C address: 0x35
    ADC_VREF: 4.096 V
    CH0 hot_temp_transmitter: raw=1192 voltage=1.9230 V
    CH1 cold_temp_transmitter: raw=1157 voltage=1.1573 V
    CH2 flow_transmitter: raw= 480 voltage=0.4801 V
    CH3 future_input: raw=  1 voltage=0.0010 V
    CH4 ambient_lm35: raw= 225 voltage=0.2251 V

Command:

```bash
python3 software/diagnostics/read_acs37800_once.py
```

Observed Results:
    Initial test: PASS
    STATUS=REVIEW_REQUIRED
    ACS37800 expected I2C address: 0x60
    No I2C register read was attempted.
    Verify the ACS37800 part variant, register map, and scaling before adding reads.

## Notes

The ADC diagnostic successfully read the MAX1238 at 0x35

The ACS37800 diagnostic intentionally did not perform register reads. The ACS37800
    register-map use, scaling, and software reads remain pending.

The extra spaces in some raw= values are expected because the diagnostic prints raw
    ADC counts using fixed-width formatting.
