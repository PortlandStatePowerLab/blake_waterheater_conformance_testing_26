# Copy To Pi Commands

These commands are examples for a PowerShell terminal on the staging workstation.
They are not run as part of staging.

Set the target:

```powershell
$STAGE = "C:\Users\Blake\Documents\Projects\WH1-master-staging"
$PI = "pi@raspberrypi.local"
$DEST = "/home/pi/wh1"
```

Create the destination:

```powershell
ssh $PI "mkdir -p $DEST"
```

Create runtime subdirectories:

```powershell
ssh $PI "mkdir -p $DEST/software/common $DEST/software/adc $DEST/software/diagnostics $DEST/software/water_draw"
```

Copy only the deploy manifest runtime payload:

```powershell
scp "$STAGE\software\__init__.py" "${PI}:$DEST/software/"
scp "$STAGE\software\requirements.txt" "${PI}:$DEST/software/"
scp "$STAGE\software\common\__init__.py" "${PI}:$DEST/software/common/"
scp "$STAGE\software\common\hardware_map.py" "${PI}:$DEST/software/common/"
scp "$STAGE\software\adc\__init__.py" "${PI}:$DEST/software/adc/"
scp "$STAGE\software\adc\max1238.py" "${PI}:$DEST/software/adc/"
scp "$STAGE\software\diagnostics\__init__.py" "${PI}:$DEST/software/diagnostics/"
scp "$STAGE\software\diagnostics\read_adc_raw.py" "${PI}:$DEST/software/diagnostics/"
scp "$STAGE\software\diagnostics\read_acs37800_once.py" "${PI}:$DEST/software/diagnostics/"
scp "$STAGE\software\diagnostics\valve_gpio_check.py" "${PI}:$DEST/software/diagnostics/"
scp "$STAGE\software\water_draw\__init__.py" "${PI}:$DEST/software/water_draw/"
scp "$STAGE\software\water_draw\whs.py" "${PI}:$DEST/software/water_draw/"
scp "$STAGE\DEPLOY_MANIFEST.md" "${PI}:$DEST/"
scp "$STAGE\REVIEW_REQUIRED.md" "${PI}:$DEST/"
scp "$STAGE\README_FIRST.md" "${PI}:$DEST/"
```

Do not copy these as runtime payload:

- `legacy_deprecated/`
- `docs/`
- `hardware/`
- `source_archive_index/`
- generated `__pycache__/` directories

After copying, log into the Pi and run the first test sequence.
