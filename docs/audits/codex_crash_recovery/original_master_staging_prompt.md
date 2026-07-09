You are working with two source folders and one new staged master folder.

SOURCE FOLDER 1 — active Pi script dump / runnable source material:
C:\Users\Blake\Documents\Projects\wh1-scripts

SOURCE FOLDER 2 — GitHub hardware/documentation repo:
C:\Users\Blake\Documents\Projects\Embedded-Water-Heater-Monitoring-and-Control-System

NEW OUTPUT FOLDER TO CREATE:
C:\Users\Blake\Documents\Projects\WH1-master-staging

Important workflow rules:

* Do not create a Git branch.
* Do not edit either original source folder.
* Do not delete source files.
* Do not push to GitHub.
* Do not push to the Raspberry Pi.
* Do not run hardware-actuating scripts.
* Write only into WH1-master-staging.
* The goal is a clean, organized, fixed, documented master staging folder that I can inspect manually before anything is copied to the Pi or pushed to GitHub.

Overall goal:
Create a complete sorted project folder containing:

* corrected active software
* deployment-ready scripts
* safe diagnostics
* hardware schematics
* PCB documents
* README files
* audit reports
* datasheets/reference documents
* wiring maps
* hardware/software traceability docs
* deprecated legacy scripts clearly separated and labeled
* review-required flags wherever human verification is still needed

This is not just a runtime folder. This should be a cleaned, modularized master project folder.

Create this folder structure:

WH1-master-staging/
README_FIRST.md
MASTER_INDEX.md
DEPLOY_MANIFEST.md
REVIEW_REQUIRED.md
CHANGELOG_STAGING.md

hardware/
README.md
schematics/
pcb/
bom/
datasheets/
hardware_map/
HARDWARE_MAP.md
SIGNAL_TRACEABILITY_TABLE.md
RIBBON_CABLE_MAP.md
ADC_CHANNEL_MAP.md
GPIO_MAP.md

software/
README.md
common/
adc/
water_draw/
power_monitoring/
valve_control/
rs485_cta2045/
diagnostics/

deployment/
README.md
pi_setup/
copy_to_pi/
systemd_services/
test_run_order/

docs/
README.md
active/
audit_reports/
wiring/
testing_procedures/
reference_only/

legacy_deprecated/
README.md
gpio6_flow_scripts/
ds18b20_direct_pi_scripts/
midrar_testing/
broken_or_incomplete/
generated_files/
old_duplicates/

source_archive_index/
ORIGINAL_SOURCE_INDEX.md
FILE_ORIGIN_MAP.md
DUPLICATE_FILE_REPORT.md

Hardware truth:

* The field wiring goes to the custom PCB.
* The Raspberry Pi connects to the PCB through the ribbon cable.
* U11 on the schematic is MAX1238EEE+.
* U12 is TXS0104E level shifter between Pi 3.3 V I2C and MAX1238 5 V I2C.
* U13 is ACS37800 power-monitoring IC.
* MAX1239 references are probably stale documentation unless a BOM, schematic, or actual board marking proves otherwise.
* ADC_VREF = 4.096 is correct for MAX1238.
* CHx values are MAX1238 ADC channels, not Raspberry Pi GPIO pins.

Expected current PCB channel map:

* Hot temperature transmitter: MAX1238 AIN0 / CH0
* Cold temperature transmitter: MAX1238 AIN1 / CH1
* Flow transmitter: MAX1238 AIN2 / CH2
* Future-use input: MAX1238 AIN3 / CH3
* LM35 ambient temperature: MAX1238 AIN4 / CH4
* Valve relay control: GPIO17 over ribbon
* ACS37800 I2C address: 0x60
* ACS37800 DIO_0: GPIO18, but double-check against schematic
* ACS37800 DIO_1: GPIO26, but double-check against schematic

Source-of-truth priority:

1. Current schematic, README, and BOM from the GitHub hardware repo
2. Active runnable scripts from wh1-scripts
3. Word documents are reference only unless no real source file exists
4. Old notes are lower priority if they conflict with schematic, README, or BOM

Documentation handling:

* Copy useful documentation from the GitHub repo into the appropriate docs/ or hardware/ folders.
* Copy schematic exports into hardware/schematics/.
* Copy PCB files, layout exports, or board-related files into hardware/pcb/.
* Copy BOM files into hardware/bom/.
* Copy datasheets into hardware/datasheets/.
* Copy audit reports into docs/audit_reports/.
* Copy active/current instructions into docs/active/.
* Copy old or uncertain Word documents into docs/reference_only/ unless they are clearly current.
* Do not leave code only embedded inside Word documents if a real .py file exists or can be reconstructed.
* Where a document contains stale information, do not silently overwrite it. Add a STALE_OR_CONFLICTING_NOTE.md beside it explaining what conflicts with the current hardware truth.

Software handling:

* Copy active runnable scripts from wh1-scripts into software/ under the appropriate module.
* Fix only the staged copies in WH1-master-staging.
* Keep active software modular and import shared constants from software/common/hardware_map.py.
* Do not keep deployable scripts mixed with legacy, generated, or broken scripts.

In software/common/, create hardware_map.py containing:

ADC_PART = "MAX1238EEE+"
ADC_VREF = 4.096

CH_HOT = 0
CH_COLD = 1
CH_FLOW = 2
CH_FUTURE = 3
CH_AMBIENT = 4

VALVE_PIN = 17
ACS37800_I2C_ADDR = 0x60
ACS_DIO0_GPIO = 18
ACS_DIO1_GPIO = 26

Include comments explaining:

* CHx values are MAX1238 ADC channels, not Pi GPIO pins.
* The Pi reaches the MAX1238 over I2C through the TXS0104E level shifter.
* GPIO17 is a Pi GPIO carried through the ribbon cable to the relay driver.
* ACS37800 is on the PCB and communicates over Pi-side I2C.

Must-fix active software items:

* CH_COLD must be 1, not 3.
* CH_FLOW must be 2, not 1.
* Keep ADC_VREF = 4.096 for MAX1238.
* Replace stale MAX1239 comments/docs in active staged files with MAX1238.
* Fix data.close to data.close().
* Keep GPIO17 valve control, but make any valve test dry-run by default unless the user explicitly passes --enable-output.
* Isolate ACS37800 code into software/power_monitoring/ or software/diagnostics/.
* Do not make GPIO6 flow-count scripts active unless you find proof that current hardware routes flow to GPIO6.
* Do not make direct /sys/bus/w1 temperature scripts active unless you find proof that DS18B20 sensors are part of the current WH1 PCB-ribbon setup.

Greyed-out / deprecated treatment:
Do not delete historical scripts.
Anything not intended for current WH1 PCB-ribbon deployment should go under legacy_deprecated/ and have either:

* a DEPRECATED_REASON.md file, or
* a clear header comment explaining why it is not part of the current deploy candidate.

Treat these as deprecated unless proven current:

* GPIO6 pulse-flow scripts
* direct DS18B20 /sys/bus/w1 temperature scripts
* duplicate midrar_testing copies
* scripts requiring missing CSV files
* generated logs
* **pycache**
* .pyc files
* generated PDFs
* C++ code saved as .py
* Word-document code snippets when real .py source exists

Add safe diagnostics:

* software/diagnostics/read_adc_raw.py

  * Reads and prints raw MAX1238 channels 0, 1, 2, 3, and 4.
  * Does not move valves.
  * Does not write outputs.

* software/diagnostics/read_acs37800_once.py

  * Reads ACS37800 once.
  * Does not change outputs.

* software/diagnostics/valve_gpio_check.py

  * Dry-run by default.
  * Requires --enable-output to actually toggle GPIO17.

* deployment/test_run_order/FIRST_PI_TEST_SEQUENCE.md

  * Gives the safest test order for the Pi.
  * Starts with non-actuating checks before any valve control.

* deployment/pi_setup/I2C_CHECK_COMMANDS.md

  * Include Pi commands for checking I2C devices.
  * Do not execute them locally.

Documentation file requirements:

README_FIRST.md:

* Explain that WH1-master-staging is a staged clean master folder.
* Explain that original folders were not edited.
* Explain that only files listed in DEPLOY_MANIFEST.md are intended to be copied to the Pi.
* Explain that legacy_deprecated is historical/reference only.

MASTER_INDEX.md:

* List every major folder and what belongs there.
* Explain where to find active scripts, hardware docs, deployment scripts, and deprecated material.

HARDWARE_MAP.md:

* Explain the physical system model:
  field wiring -> custom PCB -> ICs / circuits -> ribbon cable -> Raspberry Pi -> Python code.
* Clearly state that ADC CHx does not mean Raspberry Pi GPIOx.

SIGNAL_TRACEABILITY_TABLE.md:
Include a table with:
Field signal -> PCB connector/net -> PCB IC/circuit -> ADC channel or GPIO -> Pi interface -> Python constant -> verification status.

ADC_CHANNEL_MAP.md:
Include:
CH0 = Hot temp transmitter
CH1 = Cold temp transmitter
CH2 = Flow transmitter
CH3 = Future use
CH4 = LM35 ambient temp

GPIO_MAP.md:
Include:
GPIO17 = valve relay driver
GPIO18 = ACS37800 DIO_0, pending verification
GPIO26 = ACS37800 DIO_1, pending verification
Also include any display pins or other GPIOs found in the schematic/docs, marked active or review-required.

DEPLOY_MANIFEST.md:

* List exact files intended to copy to the Pi.
* List exact destination suggestion on the Pi.
* List first safe diagnostic commands to run.
* List files not to run yet.
* Exclude docs, old code, generated files, and legacy files from deployment.

REVIEW_REQUIRED.md:
List every uncertainty, especially:

* actual board marking for U11
* ACS37800 DIO GPIO mapping
* valve relay output behavior
* correct schedule CSVs
* whether any legacy GPIO6 flow setup still exists physically
* whether any direct DS18B20 sensor wiring still exists physically
* any mismatch between schematic, README, notes, and code
* any document that says MAX1239

CHANGELOG_STAGING.md:
List:

* what was copied
* what was fixed
* what was moved to legacy
* what docs were flagged
* what still needs physical verification

ORIGINAL_SOURCE_INDEX.md:
For each source folder, list major files/folders discovered and what they were used for.

FILE_ORIGIN_MAP.md:
For every active staged file, identify where it came from:

* wh1-scripts
* GitHub repo
* reconstructed from Word doc
* newly created staging doc
* newly created diagnostic script

DUPLICATE_FILE_REPORT.md:
List duplicates found between the two source folders and say which version was used.

Final checks:
After creating WH1-master-staging, search inside it for:

* MAX1239
* CH_COLD = 3
* CH_FLOW = 1
* FMPIN = 6
* GPIO6
* /sys/bus/w1
* data.close without parentheses
* references to missing CSV files

For every remaining hit, classify it as:

* ACTIVE_FIXED
* ACTIVE_NEEDS_REVIEW
* LEGACY_DEPRECATED
* DOC_REFERENCE_ONLY

Run only static checks:

* python -m compileall WH1-master-staging/software
* Do not run GPIO, I2C, valve, relay, ACS37800, or hardware scripts locally unless they are explicitly dry-run safe.

Final response must include:

1. New master staging folder created
2. Hardware documents copied and where they went
3. Active software files created or copied and where they went
4. Deployment files created and where they went
5. Legacy/deprecated material moved and why
6. Bugs fixed
7. Documents flagged as stale or conflicting
8. Remaining review items before Pi testing
9. Exact safe first commands to run on the Pi
