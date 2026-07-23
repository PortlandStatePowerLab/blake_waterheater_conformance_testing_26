# WH1 Deployment Manifest

This manifest is the allow-list for Raspberry Pi copy. Do not copy legacy,
documentation, hardware-source, cache, or audit folders as runtime payload.

Scheduled CSV-driven draws remain unsupported. The supported operator path is
one draw per invocation of `bin/wh-draw --target-gal ...`.

Suggested Pi destination: `/home/pi/wh1`

## Runtime files to copy

- `software/__init__.py`
- `software/requirements.txt`
- `software/station/__init__.py`
- `software/station/station_hardware_map.py`
- `software/adc/__init__.py`
- `software/adc/adc_interface.py`
- `software/adc/max1238_driver.py`
- `software/adc/max1238_builder.py`
- `software/adc/adc_raw_diagnostic.py`
- `software/adc/adc_acquisition_diagnostic.py`
- `software/sensors/__init__.py`
- `software/sensors/sensor_conversion_math.py`
- `software/sensors/sensor_configuration_loader.py`
- `software/sensors/sensor_reader.py`
- `software/sensors/sensor_diagnostic.py`
- `software/valve/__init__.py`
- `software/valve/valve_interface.py`
- `software/valve/gpio_valve_driver.py`
- `software/valve/gpio_valve_builder.py`
- `software/valve/valve_diagnostic.py`
- `software/power/__init__.py`
- `software/power/power_monitor_diagnostic.py`
- `software/runtime/__init__.py`
- `software/runtime/controlled_water_draw_workflow.py`
- `software/commands/__init__.py`
- `software/commands/check_adc_raw_command.py`
- `software/commands/check_adc_acquisition_command.py`
- `software/commands/check_sensors_command.py`
- `software/commands/check_valve_command.py`
- `software/commands/check_power_monitor_command.py`
- `software/commands/run_water_draw_command.py`
- `bin/adc-raw`
- `bin/adc-acquisition-compare`
- `bin/sensor-check`
- `bin/valve-check`
- `bin/power-monitor-check`
- `bin/wh-draw`

The GS10 drive files are excluded from the normal WH1 runtime payload until
that separate RS-485 device is part of an approved station procedure.

## First safe Pi commands

Run from `/home/pi/wh1`:

```bash
python3 -m pip install -r software/requirements.txt
python3 -m compileall software
i2cdetect -y 1
bin/adc-raw
bin/power-monitor-check
bin/valve-check
bin/wh-draw --target-gal 0.1
```

The last two commands operate the validated valve and water-draw hardware.

## Controlled output commands

The completed valve, sensor, flow, temperature, and target-stop verification
records permit controlled WH1 use:

```bash
bin/valve-check --state off
bin/wh-draw --target-gal 0.1
```

## Do not run

- Anything under `legacy_deprecated/`.
- Direct DS18B20 or GPIO6 flow-count scripts from legacy material.
- `bin/gs10-modbus-check` without an approved GS10 serial-device procedure.
