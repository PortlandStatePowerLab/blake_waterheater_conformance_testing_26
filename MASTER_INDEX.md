# WH1 Master Index

## Top-level files

- `README_FIRST.md`: read first; explains staging purpose and safety rules.
- `DEPLOY_MANIFEST.md`: exact files intended for Raspberry Pi copy.
- `REVIEW_REQUIRED.md`: remaining open review gates plus links to completed verification records.
- `CHANGELOG_STAGING.md`: staging changes, completed verification, and remaining verification.
- `MASTER_INDEX.md`: this index.

## Major folders

- `hardware/`: copied schematics, PCB fabrication/source files, BOM-related
  material if present, datasheets, and hardware map workspace.
- `software/`: active staged Python package. Current active constants live in
  `software/common/hardware_map.py`; first-run diagnostics live in
  `software/operator_checks/`.
- `deployment/`: operator notes for Pi setup, copy commands, and first test
  sequence. These files are procedures only.
- `project_control/`: review gates, verification records, templates, and
  archived project-control notes.
- `test_records/`: observed test results, pass/fail notes, command outputs, and
  verification evidence from lab testing.
- `docs/active/`: current high-level hardware/project documents copied from the
  hardware repository.
- `docs/wiring/`: wiring diagrams and PCB connection guides.
- `docs/audit_reports/`: audit reports plus crash recovery materials.
- `docs/reference_only/`: Word docs, old notes, and source references that are
  not active deployment instructions.
- `legacy_deprecated/`: historical scripts and generated material kept for
  reference only.
- `source_archive_index/`: audit indexes and search reports for remaining stale
  or review-required references.

## Where to look

- Active scripts: `software/`
- Manually invoked operator checks: `software/operator_checks/`
- Hardware schematics and PCB files: `hardware/schematics/` and `hardware/pcb/`
- Deployment order: `deployment/test_run_order/FIRST_PI_TEST_SEQUENCE.md`
- Open review gates: `REVIEW_REQUIRED.md` and `project_control/review_pending/`
- Completed verification records: `project_control/verification_completed/`
- Observed test results: `test_records/`
- Material not to run: `legacy_deprecated/` and `docs/reference_only/`
