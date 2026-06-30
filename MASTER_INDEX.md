# WH1 Master Index

## Top-level files

- `README_FIRST.md`: read first; explains staging purpose and safety rules.
- `DEPLOY_MANIFEST.md`: exact files intended for Raspberry Pi copy.
- `REVIEW_REQUIRED.md`: unresolved hardware, software, and document checks.
- `CHANGELOG_STAGING.md`: staging changes and remaining verification.
- `MASTER_INDEX.md`: this index.

## Major folders

- `hardware/`: copied schematics, PCB fabrication/source files, BOM-related
  material if present, datasheets, and hardware map workspace.
- `software/`: active staged Python package. Current active constants live in
  `software/common/hardware_map.py`; first-run diagnostics live in
  `software/diagnostics/`.
- `deployment/`: operator notes for Pi setup, copy commands, and first test
  sequence. These files are instructions only.
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
- Safe first diagnostics: `software/diagnostics/`
- Hardware schematics and PCB files: `hardware/schematics/` and `hardware/pcb/`
- Deployment order: `deployment/test_run_order/FIRST_PI_TEST_SEQUENCE.md`
- Material not to run: `legacy_deprecated/` and `docs/reference_only/`
