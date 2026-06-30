# blake_waterheater_conformance_testing_26
Water heater conformance testing repo for PSU Power Lab: Raspberry Pi diagnostics, sensor/relay validation, CSV logging, wiring notes, test procedures, and analysis workflows for the smart water heater test station.

Water heater conformance testing, diagnostics, documentation, and analysis support for the PSU Power Lab smart water heater test station.

This repo is for practical lab-use work connected to the hybrid heat-pump water heater research platform: Raspberry Pi control scripts, sensor checks, valve/relay diagnostics, CSV logging, wiring notes, calibration notes, test procedures, troubleshooting, and analysis workflows.

The hardware platform includes four water heater stations, each paired with its own plumbing, sensors, per-unit control enclosure, custom PCB, and Raspberry Pi controller. Existing project documentation covers the full station design, PCB hardware, electrical installation, sensor integration, validation testing, and troubleshooting. [link to forked repo: "embedded..."]

---

## Purpose

This repo is intended to hold the repeatable work needed to prove that the water heater test station is wired, sensed, controlled, logged, and analyzed correctly before and during experimental runs.

In plain lab terms: this repo is the checklist, toolbox, and evidence trail for making sure the station behaves the way we think it behaves.

---

## Scope

This repo may include:

- Raspberry Pi setup notes and command sequences
- GPIO relay/valve diagnostics
- ADC and I2C checks
- 4–20 mA sensor validation notes
- Flow, temperature, voltage, current, and power logging scripts
- CSV log formats and example datasets
- Calibration notes and unit conversions
- Wiring and connector references
- Valve and plumbing test notes
- Test procedures for each water heater station
- Troubleshooting notes
- Analysis scripts and plots

---

## Hardware Context

The test station includes:

- Four water heater units: WH1, WH2, WH3, WH4 - (unit brand and models)
- Raspberry Pi controllers - (model, revision, date: printed on each pi)
- Custom PCB hardware for control, data acquisition, and AC monitoring - (data sheets for components?)
- 4–20 mA temperature and flow transmitters - (data sheet?)
- 120 VAC solenoid valves - (data sheet?)
- Manual flow-adjustment valves - (data sheet?)
- ACS37800-based AC power monitoring 
- MAX1238 ADC-based analog measurement
- RS-485 communication hardware
- 24 VDC sensor/PCB power
- 5 VDC Raspberry Pi power

The station wiring guide identifies high-voltage AC terminals, 4–20 mA transmitter terminals, RS-485 terminals, low-voltage connections, status LEDs, pipe order, power-down procedure, and critical safety notes. [link to wiring guide in forked repo: "embedded..."]

---

## Important Safety Notes

Before opening or changing any enclosure wiring:

1. De-energize the required AC source.
2. Verify 0 VAC with a meter.
3. Disconnect 24 VDC sensor/PCB power.
4. Disconnect Raspberry Pi USB-C power.
5. Do not assume a water heater breaker also de-energizes valve wiring.

The wiring guide specifically notes that valve L1 is wired upstream of the water heater breaker and may remain energized even when the water heater breaker is off. [link to document stating L1 energization, in forked repo: "embedded..."]

---

## Current / Completed Work

This repo may include work already completed during bring-up and conformance testing, including:

- Lab PC to Raspberry Pi SSH workflow - maybe with ssh keygen process, and EXCLUDING private keys or any other personal/private information.
- Raspberry Pi file transfer workflow - yes this will be in here
- GPIO17 valve relay check workflow - I2C test?
- Dry-run-first valve GPIO diagnostic script - yes this will be in here
- Backup/versioning workflow for diagnostic scripts - using commits?
- Python compile/test workflow on the Pi - probably
- Hardware notes from valve, relay, ADC, and sensor investigation - probably
- Wiring notes for power/signal separation and labeling - maybe
- Sensor conversion notes for 4–20 mA signals - mabye
- Flow/GPM conversion planning - maybe
- CSV logging and analysis planning - maybe

---

## Suggested Repo Layout (which may change depending on final file structure, also missing deployment folder) 

```text
.
├── README.md
├── docs/
│   ├── safety/
│   ├── wiring/
│   ├── plumbing/
│   ├── test-procedures/
│   ├── troubleshooting/
│   └── decisions/
├── software/
│   ├── diagnostics/
│   ├── logging/
│   ├── analysis/
│   └── common/
├── data/
│   ├── raw/
│   ├── processed/
│   └── examples/
├── plots/
├── references/
└── archive/
