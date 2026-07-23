# Legacy

This directory preserves historical, deprecated, superseded, original, and
reference implementations for traceability.

These files are not the current operator interface and are not included in the
normal deployment manifest or automated test execution. They may contain
obsolete imports, paths, assumptions, dependencies, hardware mappings, or
unsafe behavior. Do not run them on station hardware without a separate review.

Active implementations live under:

- `software/` for current drivers, builders, interfaces, readers, diagnostics,
  commands, and runtime workflows;
- `bin/` for the current human-facing operator commands.

## Preserved groups

- `pre_role_cleanup_2026-07-23/software/` contains byte-for-byte copies restored
  from `HEAD` for files superseded by the role-based software reorganization.
- `deprecated/` contains the repository's previously collected deprecated,
  broken, generated, duplicate, and reference-only source material.
