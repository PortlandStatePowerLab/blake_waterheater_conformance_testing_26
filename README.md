# blake_waterheater_conformance_testing_26

## Contributors

- Blake Ellis — PSU Power Lab undergraduate research contributor
- Prof. Robert Bass — PSU Power Engineering Lab supervisor
- PSU Power Lab / Smart Grid Research & Simulation Platform contributors
- Nawaf Altalhi — original Smart Water Heater Test Station hardware design and bring-up documentation

## Description

This repository is a staged conformance-testing workspace for the PSU Power Lab smart water heater test station.

It holds cleaned and organized material for WH1 Raspberry Pi deployment, hardware diagnostics, wiring references, review notes, and legacy script isolation. 
The repo was built from the existing `WH1-master-staging` structure and is intended to support safe testing before copying runtime files to the Raspberry Pi.

Main focus areas:

- WH1 Raspberry Pi deployment preparation
- GPIO17 valve relay diagnostics
- MAX1238 ADC diagnostics
- ACS37800 power monitor review/testing
- hardware map cleanup
- wiring and PCB reference preservation
- safe first-test procedures
- review-required issue tracking
- deprecated script isolation

Only files listed in `DEPLOY_MANIFEST.md` are intended to be copied to the Raspberry Pi runtime location.

## Repository Contents

```text
.
├── CHANGELOG_STAGING.md
├── DEPLOY_MANIFEST.md
├── MASTER_INDEX.md
├── README.md
├── README_FIRST.md
├── REVIEW_REQUIRED.md
├── deployment/
│   ├── copy_to_pi/
│   ├── pi_setup/
│   ├── systemd_services/
│   └── test_run_order/
├── docs/
│   ├── active/
│   ├── audit_reports/
│   ├── reference_only/
│   ├── testing_procedures/
│   └── wiring/
├── hardware/
│   ├── bom/
│   ├── datasheets/
│   ├── hardware_map/
│   ├── pcb/
│   └── schematics/
├── legacy_deprecated/
│   ├── broken_or_incomplete/
│   ├── ds18b20_direct_pi_scripts/
│   ├── generated_files/
│   ├── gpio6_flow_scripts/
│   ├── midrar_testing/
│   └── old_duplicates/
├── software/
│   ├── adc/
│   ├── common/
│   ├── diagnostics/
│   ├── power_monitoring/
│   ├── rs485_cta2045/
│   ├── valve_control/
│   └── water_draw/
└── source_archive_index/
```
## Folder Summary

- deployment/ -- Copy to Pi notes, Pi setup notes, systemd service notes, and first test-run order.
- docs/ -- active project documents, wiring notes, testing procedures, audit reports, and reference-only documents
- hardware/ -- BOM material, datasheets, hardware maps, PCB files, and schematics
- software/ -- active staged Python code for ADC, diagnostics, valve control, power monitoring, RS-485/CTA-2045, and water draw control
- legacy_deprecated/ -- old, duplicate, generated, broken, or deprecated scripts kept only for reference.
- source_archive_index/ -- sourced indexes, audit indexes, and search/reference tracking

## Top-level files:
README_FIRST.md -- first-read staging overview
MASTER_INDEX.md -- repo map and where to look guide
DEPLOY_MANIFEST.md -- allow-list of runtime files intended for Raspberry Pi copy.
REVIEW_REQUIRED.md -- unresolved checks requiring review
CHANGELOG_STAGING.md -- staging change notes

## Important Links
- [First-Read staging overview](./README_FIRST.md)
- [Master repo index](./MASTER_INDEX.md)
- [Depoloyment Manifest](./DEPLOY_MANIFEST.md)
- [Review Required List](./REVIEW_REQUIRED.md)
- [Staging Changelog](./CHANGELOG_STAGING.md)
- [Deployment Notes](./deployment/)
- [Software](./software/)
- [Diagnostics](./software/diagnostics/)
- [Hardware References](./hardware/)
- [Wiring Documentation](./docs/wiring/)
- [Testing Procedures](./docs/testing_procedures/)
- [Legacy deprecated material](./legacy_deprecated/)
