# Copy To Pi Commands

These PowerShell examples copy only the allow-listed runtime folders. Review
`DEPLOY_MANIFEST.md` before use.

```powershell
$STAGE = "C:\Users\Blake\Documents\Projects\blake_water_heater_conformance_testing_26"
$PI = "pi@raspberrypi.local"
$DEST = "/home/pi/wh1"

ssh $PI "mkdir -p $DEST/software $DEST/bin"

ssh $PI "mkdir -p $DEST/software/station $DEST/software/adc $DEST/software/sensors $DEST/software/valve $DEST/software/power $DEST/software/runtime $DEST/software/commands"

scp "$STAGE\software\station\*.py" "${PI}:$DEST/software/station/"
scp "$STAGE\software\adc\*.py" "${PI}:$DEST/software/adc/"
scp "$STAGE\software\sensors\*.py" "${PI}:$DEST/software/sensors/"
scp "$STAGE\software\valve\*.py" "${PI}:$DEST/software/valve/"
scp "$STAGE\software\power\__init__.py" "${PI}:$DEST/software/power/"
scp "$STAGE\software\power\power_monitor_diagnostic.py" "${PI}:$DEST/software/power/"
scp "$STAGE\software\runtime\*.py" "${PI}:$DEST/software/runtime/"
scp "$STAGE\software\commands\__init__.py" "${PI}:$DEST/software/commands/"
scp "$STAGE\software\commands\check_adc_raw_command.py" "${PI}:$DEST/software/commands/"
scp "$STAGE\software\commands\check_adc_acquisition_command.py" "${PI}:$DEST/software/commands/"
scp "$STAGE\software\commands\check_sensors_command.py" "${PI}:$DEST/software/commands/"
scp "$STAGE\software\commands\check_valve_command.py" "${PI}:$DEST/software/commands/"
scp "$STAGE\software\commands\check_power_monitor_command.py" "${PI}:$DEST/software/commands/"
scp "$STAGE\software\commands\run_water_draw_command.py" "${PI}:$DEST/software/commands/"
scp "$STAGE\software\__init__.py" "${PI}:$DEST/software/"
scp "$STAGE\software\requirements.txt" "${PI}:$DEST/software/"
scp "$STAGE\bin\adc-raw" "${PI}:$DEST/bin/"
scp "$STAGE\bin\adc-acquisition-compare" "${PI}:$DEST/bin/"
scp "$STAGE\bin\sensor-check" "${PI}:$DEST/bin/"
scp "$STAGE\bin\valve-check" "${PI}:$DEST/bin/"
scp "$STAGE\bin\power-monitor-check" "${PI}:$DEST/bin/"
scp "$STAGE\bin\wh-draw" "${PI}:$DEST/bin/"
scp "$STAGE\DEPLOY_MANIFEST.md" "${PI}:$DEST/"

ssh $PI "find $DEST/bin -type f -exec chmod +x {} +"
```

Do not copy `software/gs10_drive/` as part of the normal WH1 payload. Do not
copy `legacy_deprecated/`, documentation, hardware-source folders, caches, or
generated results.
