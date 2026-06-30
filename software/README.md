# Software

Active staged software is organized by function:

- `common/hardware_map.py`: shared WH1 hardware constants.
- `adc/max1238.py`: MAX1238 I2C ADC driver copied from the active script dump.
- `water_draw/whs.py`: corrected ADC-based water draw controller. GPIO output is dry-run unless `--enable-output` is passed.
- `power_monitoring/`: ACS37800 calibration/reference workspace. Register reads still require review.
- `diagnostics/`: safe first-run diagnostics for ADC, ACS37800 review gating, and valve GPIO dry-run checks.
- `rs485_cta2045/`: Modbus/RS-485 diagnostic copied from the active script dump.

Legacy GPIO6 flow, direct DS18B20, generated, and duplicate scripts are not active here.
