# I2C Check Commands

Run these on the Raspberry Pi, not on the staging workstation.

```bash
sudo raspi-config nonint do_i2c 0
sudo reboot
```

After reboot:

```bash
ls -l /dev/i2c-1
which i2cdetect || sudo apt-get update
which i2cdetect || sudo apt-get install -y i2c-tools
i2cdetect -y 1
```

Expected review targets:

- MAX1238 ADC address from the staged driver: `0x35`
- ACS37800 address from `software/common/hardware_map.py`: `0x60`

If either address is absent, stop and review power, ribbon cable orientation,
level-shifter power rails, pullups, and PCB assembly before running Python
diagnostics.
