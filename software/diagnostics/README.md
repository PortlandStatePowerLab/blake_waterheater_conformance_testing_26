# Diagnostics

These scripts are intended for first bring-up and verification on the Raspberry Pi. The ADC and ACS37800 diagnostics read I2C devices only. `valve_gpio_check.py` is dry-run by default and does not drive GPIO17 unless `--enable-output` is present.
