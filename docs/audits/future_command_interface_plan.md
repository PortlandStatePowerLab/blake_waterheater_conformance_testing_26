# Future Command Interface Plan

## Purpose

Define the target operator command interface for future diagnostics, runtime tools, and laptop-testable analysis before refactoring active software.

This is a planning-only document. It does not change runtime behavior.

## Scope

Included:

- Current active runtime entrypoints.
- Current diagnostic entrypoints.
- Future repo-controlled `bin/` wrapper command style.
- Hardware-coupled versus laptop-testable command groups.
- Future-only command targets that do not exist yet.
- Future naming convention for raw versus processed sensor/data functions.

Excluded:

- Runtime code changes.
- File moves.
- Import rewrites.
- New modules.
- New wrapper scripts.
- Package restructuring.
- Shell startup changes.

## Current active command map

| Current file | Current role | Coupling | Notes |
| --- | --- | --- | --- |
| `software/water_draw/whs.py` | Active WH1 water-draw runtime | Mixed / hardware-coupled | Controls GPIO17 valve path, reads MAX1238 ADC channels, integrates flow into volume, and includes max-run / low-flow safety behavior. |
| `software/diagnostics/valve_gpio_check.py` | Diagnostic entrypoint | Hardware-coupled | Dry-run-first GPIO17 valve relay diagnostic. |
| `software/diagnostics/read_adc_raw.py` | Diagnostic entrypoint | Hardware-coupled | Reads raw MAX1238 ADC values from the current WH1 channel map. |
| `software/diagnostics/read_acs37800_once.py` | Diagnostic entrypoint | Hardware-coupled / placeholder | Safe ACS37800 diagnostic placeholder. |
| `software/rs485_cta2045/gs10_modbus_test.py` | Diagnostic entrypoint | Hardware-coupled | RS-485 / Modbus / CTA-2045 diagnostic-style command. |

## Operator interface decision

Use repo-controlled `bin/` wrapper scripts as the primary future operator interface.

The `bin/` directory is the front-panel command surface for the repo. It may contain many short commands, but those commands must stay thin.

Wrappers should:

- Find the repository root.
- Run the intended Python module or script.
- Forward all CLI arguments with `"$@"`.
- Stay small enough to inspect quickly.

Wrappers should not:

- Contain GPIO logic.
- Contain I2C/register logic.
- Contain sensor conversion math.
- Contain CSV parsing/writing logic.
- Duplicate runtime safety behavior.

Actual implementation stays under `software/` modules unless a future restructuring card changes that.

The preferred operator shape is:

- `./bin/wh-valve-check --dry-run`
- `./bin/wh-read-adc --channel hot_temp`
- `./bin/wh-read-power`
- `./bin/wh-draw --dry-run`
- `./bin/wh-draw --enable-output --target-vol-gal 5`

After deployment adds `bin/` to `PATH`, the same commands can be run without `./bin/`:

- `wh-valve-check --dry-run`
- `wh-read-adc --channel hot_temp`
- `wh-read-power`
- `wh-draw --dry-run`
- `wh-draw --enable-output --target-vol-gal 5`

This planning card does not create wrapper scripts or modify shell startup files.

## Wrapper naming plan

| Wrapper | Current or future target | Purpose |
| --- | --- | --- |
| `bin/wh-valve-check` | `software/diagnostics/valve_gpio_check.py` | Valve relay diagnostic. |
| `bin/wh-read-adc` | `software/diagnostics/read_adc_raw.py` | MAX1238 ADC diagnostic/read command. |
| `bin/wh-read-power` | `software/diagnostics/read_acs37800_once.py` | ACS37800 power-monitor read command. |
| `bin/wh-draw` | `software/water_draw/whs.py` | Controlled water draw runtime. |
| `bin/wh-modbus-test` | `software/rs485_cta2045/gs10_modbus_test.py` | RS-485 / Modbus / CTA-2045 diagnostic. |
| `bin/wh-plot-run` | Future-only | Plot saved run data. |
| `bin/wh-validate-csv` | Future-only | Validate CSV schema. |

## Wrapper behavior target

Each wrapper should be a small shell script with one job: call the real implementation.

Expected wrapper pattern:

- Resolve the repository root from the wrapper location.
- Change into the repository root.
- Execute the real Python module or script.
- Pass all user arguments through unchanged.
- Exit with the same status as the underlying command.

Example behavior, described without implementing it in this card:

- `bin/wh-read-adc --channel hot_temp` should call the active ADC diagnostic implementation.
- `bin/wh-valve-check --dry-run` should call the active valve diagnostic implementation.
- `bin/wh-draw --dry-run` should call the active WH1 draw runtime implementation.

Wrappers are convenience entrypoints, not implementation homes.

## Developer command layer

Long module commands may still be useful for development and debugging because they map directly to Python modules.

Current module command examples:

| Developer command | Current source | Notes |
| --- | --- | --- |
| `python -m software.diagnostics.valve_gpio_check --dry-run` | `software/diagnostics/valve_gpio_check.py` | Current module-style valve diagnostic. |
| `python -m software.diagnostics.read_adc_raw --channel hot_temp` | `software/diagnostics/read_adc_raw.py` | Current module-style ADC diagnostic. |
| `python -m software.diagnostics.read_acs37800_once` | `software/diagnostics/read_acs37800_once.py` | Current module-style ACS37800 diagnostic placeholder. |
| `python -m software.rs485_cta2045.gs10_modbus_test --port /dev/ttyUSB0` | `software/rs485_cta2045/gs10_modbus_test.py` | Current module-style RS-485 / Modbus diagnostic target. |
| `python -m software.water_draw.whs --dry-run` | `software/water_draw/whs.py` | Current module-style water draw runtime target. |

The operator-facing interface should still prefer `bin/` wrappers because they are shorter, more stable, and easier for station use.

## Proposed hardware-coupled diagnostic wrappers

These commands require the Raspberry Pi, station hardware, GPIO, I2C bus, RS-485 adapter, or connected devices.

### Valve GPIO dry-run

Wrapper: `bin/wh-valve-check --dry-run`

Current source: `software/diagnostics/valve_gpio_check.py`

Status: Target existing module

Notes: Must preserve dry-run-first behavior.

### Valve GPIO enabled pulse

Wrapper: `bin/wh-valve-check --enable-output --pulse-s 1`

Current source: `software/diagnostics/valve_gpio_check.py`

Status: Target existing module

Notes: Must require explicit output enable before driving GPIO17.

### Read ADC raw hot-temp channel

Wrapper: `bin/wh-read-adc --channel hot_temp`

Current source: `software/diagnostics/read_adc_raw.py`

Status: Target existing module

Notes: Channel names should eventually come from `software/common/hardware_map.py`.

### Read ADC raw flow channel

Wrapper: `bin/wh-read-adc --channel flow`

Current source: `software/diagnostics/read_adc_raw.py`

Status: Target existing module

Notes: Reads the MAX1238 ADC path.

### Read ACS37800 once

Wrapper: `bin/wh-read-power`

Current source: `software/diagnostics/read_acs37800_once.py`

Status: Target existing module

Notes: Current active ACS37800 path is diagnostic/placeholder, not a reusable helper yet.

### GS10 Modbus / RS-485 test

Wrapper: `bin/wh-modbus-test --port /dev/ttyUSB0`

Current source: `software/rs485_cta2045/gs10_modbus_test.py`

Status: Target existing module

Notes: Exact options should be verified before implementation.

## Proposed mixed runtime wrappers

These commands orchestrate hardware access, safety behavior, logging, and runtime sequencing.

### WHS dry-run

Wrapper: `bin/wh-draw --dry-run`

Current source: `software/water_draw/whs.py`

Status: Target existing module

Notes: Should remain safe by default.

### WHS enabled draw

Wrapper: `bin/wh-draw --enable-output --target-vol-gal 5`

Current source: `software/water_draw/whs.py`

Status: Target existing module

Notes: Must preserve explicit output enable requirement.

### WHS enabled draw with max runtime

Wrapper: `bin/wh-draw --enable-output --target-vol-gal 5 --max-run-s 300`

Current source: `software/water_draw/whs.py`

Status: Target existing module

Notes: Runtime safety limits must remain visible in CLI options.

## Proposed laptop-testable analysis wrappers

These commands should be able to run on a normal laptop using sample data files.

### Validate CSV schema

Wrapper: `bin/wh-validate-csv --input data/raw/example.csv`

Current source: None yet

Status: Future-only

Notes: Intended for CSV schema validation.

### Plot run data

Wrapper: `bin/wh-plot-run --input data/raw/example.csv --output outputs/example_plot.png`

Current source: None yet

Status: Future-only

Notes: Intended for laptop-side plot generation.

### Summarize run

Wrapper: `bin/wh-summarize-run --input data/raw/example.csv`

Current source: None yet

Status: Future-only

Notes: Intended for run summary metrics.

### Check timestamps

Wrapper: `bin/wh-check-timestamps --input data/raw/example.csv`

Current source: None yet

Status: Future-only

Notes: Intended for timestamp cadence checks.

## Proposed reusable helper targets

These are not command entrypoints. They are future module boundaries that commands may import later.

### ACS37800 helper

Future helper: `software.power_monitoring.acs37800`

Status: Future-only

Reason: No active reusable ACS37800 helper exists yet. Current ACS37800 access is diagnostic plus legacy/reference implementation.

### Conversion helpers

Future helper: `software.analysis.conversions`

Status: Future-only

Reason: Candidate home for laptop-testable ADC/current/temp/flow conversion math.

### CSV schema helpers

Future helper: `software.analysis.csv_schema`

Status: Future-only

Reason: Candidate home for CSV row/schema validation.

### Plotting helpers

Future helper: `software.analysis.plotting`

Status: Future-only

Reason: Candidate home for plot generation helpers.

## CLI option naming rules

Use explicit option names with units when practical.

- `--dry-run`: default-safe mode that prints intended behavior without driving hardware.
- `--enable-output`: required before any GPIO, relay, valve, or other output action.
- `--channel`: named sensor/channel selection from hardware map.
- `--target-vol-gal`: target draw volume in gallons.
- `--max-run-s`: maximum runtime in seconds.
- `--pulse-s`: relay/valve pulse duration in seconds.
- `--input`: input file path for laptop-testable commands.
- `--output`: output file path for generated artifacts.

## Future function naming convention

Use paired raw/processed function names when separating hardware reads from converted values.

Pattern:

- `get_<thing>_raw()` returns the raw hardware, register, sensor, or ADC value.
- `get_<thing>()` returns the processed engineering value when the unit is obvious from context.
- `get_<thing>_<unit>()` returns the processed engineering value when the unit should be explicit.

Examples:

| Raw function | Processed function | Meaning |
| --- | --- | --- |
| `get_adc_raw()` | `get_adc_voltage_v()` | Raw ADC code versus converted ADC voltage. |
| `get_hot_temp_raw()` | `get_hot_temp_f()` | Raw sensor/ADC value versus hot temperature in degrees F. |
| `get_cold_temp_raw()` | `get_cold_temp_f()` | Raw sensor/ADC value versus cold temperature in degrees F. |
| `get_flow_raw()` | `get_flow_gpm()` | Raw flow signal versus flow in GPM. |
| `get_power_raw()` | `get_power_w()` | Raw ACS37800 register data versus processed power in watts. |
| `get_volume_raw()` | `get_volume_gal()` | Raw/count/integrated source value versus processed volume in gallons. |

Use descriptive units in processed names when helpful, such as `_v`, `_ma`, `_f`, `_c`, `_gpm`, `_gal`, `_w`, or `_s`.

This naming convention is a future refactor target. This planning card does not rename existing functions.

## Safety rules for future commands

- Hardware output commands must stay dry-run-first.
- GPIO, relay, and valve commands must require `--enable-output`.
- Hardware-coupled commands should fail clearly when run on a laptop without Pi hardware.
- Laptop-testable commands must not import `RPi.GPIO`, `smbus2`, serial hardware libraries, or station-only dependencies at import time.
- Runtime commands must keep max-run, low-flow, interrupt, and cleanup behavior visible and testable.
- Refactors should preserve existing station behavior before improving structure.

## Deployment notes

The team org repository should become the canonical structure first.

The Raspberry Pi deployment should then be arranged around the team repo structure.

Future deployment should make operator commands available by either:

- Running wrappers from the repo root as `./bin/<command>`.
- Adding the repo `bin/` directory to `PATH`.
- Installing repo-controlled wrapper scripts through a deployment step.

Shell aliases may still be useful, but aliases should be convenience sugar only. The repo-controlled `bin/` wrappers should be the stable operator interface.

## Current reality notes

- `software/adc/max1238.py` is the active MAX1238 helper module.
- `software/common/hardware_map.py` is the active hardware map/config target.
- `software/power_monitoring/acs37800.py` does not currently exist as an active helper.
- ACS37800 reusable helper extraction should be a separate future card.
- `software/water_draw/whs.py` is active hardware-coupled runtime code and should not be moved casually.
- Active package/config files currently have UTF-8 BOM parse errors in existing audits; cleanup should be a separate card.

## Done when

- We have a target operator command style before refactoring.
- Existing active scripts are mapped to future wrapper commands.
- Future-only commands are clearly marked as not currently implemented.
- Hardware-coupled, laptop-testable, and mixed runtime commands are separated.
- Future refactor candidates are identified without changing runtime code.
- The `bin/` wrapper policy is documented.
- The raw/processed function naming convention is documented.

## Next action

Choose one small future refactor-prep card.

Recommended next card:

- Clean UTF-8 BOM parse errors from active package/config files.

Alternative future cards:

- Add initial `bin/` wrappers for existing active commands.
- Extract laptop-testable conversion helpers.
- Extract ACS37800 reusable helper module.
- Add sample CSV schema validation command.
- Add command smoke-test documentation.
