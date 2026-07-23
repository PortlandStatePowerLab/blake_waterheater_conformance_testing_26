# Project Control

This folder tracks review gates, verification records, and archived project-control notes for the staging repository.

Use this folder for project status documents, not runtime code.

- `review_pending/`: items that still need human, hardware, or software verification.
- `verification_completed/`: records of checks that were completed and verified.
- `verification_templates/`: reusable templates for future verification records.
- `archive/`: old project-control notes that are no longer active but should be preserved.

## Rule

If something is still blocking deployment or hardware actuation, keep it in 'review_pending/'.

If something has been checked, tested, and recorded with a date/result, move or copy the record into `verification_completed/`.

## Repository naming boundaries

- `measurement_data/` contains measured or source datasets.
- `runtime_logs/` contains generated operational logs.
- `generated_results/` contains derived plots, processed data, and reports.
- `software/commands/` contains user-invoked Python entrypoints.
- Reusable diagnostics live with their subsystem under `software/`.
- `tests/` contains laptop-safe automated verification.
- `software/runtime/` contains station workflows and coordination.
- `bin/` contains human-facing shell commands that call `software.commands`.

Deferred decisions belong in `review_pending/open_review_items.md`; do not guess
hardware identities, BOM contents, or the role of an unclear archived file.
