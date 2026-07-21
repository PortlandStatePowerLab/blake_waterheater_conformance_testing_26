# Software

Active software is organized by component role:

- `common/hardware_map.py`: shared WH1 hardware constants.
- `adc/`: the MAX1238 driver, its builder, and the hardware-agnostic ADC interface.
- `operator_checks/`: manually invoked live-hardware inspection tools; these are not automated tests.
- `helpers/`: documented boundary for small reusable support functions.
- `services/`: documented boundary for reusable lab workflows.
- `entrypoints/`: documented boundary for operator or external startup code.
- `water_draw/whs.py`: corrected ADC-based water draw controller. GPIO output is dry-run unless `--enable-output` is passed.
- `power_monitoring/`: ACS37800 calibration/reference workspace. Register reads still require review.
- `rs485_cta2045/`: Modbus/RS-485 diagnostic copied from the active script dump.

Operator-facing shell commands belong in `../bin/` as thin wrappers. Automated,
laptop-safe assertions belong in `../tests/`. Builders and interfaces stay with
the subsystem they construct or describe.

Legacy GPIO6 flow, direct DS18B20, generated, and duplicate scripts are not active here.
