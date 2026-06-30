# Remaining Search Hits

Search date: 2026-06-25

Scope searched:

- Top-level staging Markdown files
- `software/`
- `deployment/`
- `hardware/`
- `docs/active/`
- `docs/wiring/`

Scope intentionally excluded:

- `legacy_deprecated/`
- `docs/reference_only/`
- `docs/audit_reports/`
- generated `__pycache__/` files

## Summary

No remaining active-code hits were found for:

- `CH_COLD = 3`
- `CH_FLOW = 1`
- `FMPIN = 6`
- `data.close`

Remaining hits are documentation, review gates, or copied CAD metadata.

## Classified Hits

| Classification | File | Pattern | Lines | Notes |
|---|---|---:|---|---|
| DOC_REFERENCE_ONLY | `CHANGELOG_STAGING.md` | `GPIO6` | 10, 26 | Historical/deprecated material summary only. |
| DOC_REFERENCE_ONLY | `DEPLOY_MANIFEST.md` | `GPIO6` | 46 | Safety note saying not to run legacy GPIO6 flow scripts. |
| ACTIVE_NEEDS_REVIEW | `hardware/pcb/WH_Test_Station_PCB_RevA.json` | `MAX1239` | 1 | Copied EasyEDA PCB metadata still contains stale ADC part text. Do not treat as software truth until board marking/BOM is verified. |
| ACTIVE_NEEDS_REVIEW | `hardware/schematics/Schematic_Power_Lab_project.svg` | `MAX1239` | 5 | Copied schematic export contains stale ADC part text. |
| ACTIVE_NEEDS_REVIEW | `hardware/schematics/Schematic_Power_Lab_project.svg` | `GPIO6` | 5 | Full Raspberry Pi header label appears in CAD export; not evidence of active flow routing. |
| ACTIVE_NEEDS_REVIEW | `hardware/schematics/WH_Test_Station_Schematic_RevA.json` | `MAX1239` | 1 | Copied EasyEDA schematic metadata still contains stale ADC part text. Current staging truth remains U11 = MAX1238EEE+. |
| ACTIVE_NEEDS_REVIEW | `hardware/schematics/WH_Test_Station_Schematic_RevA.json` | `GPIO6` | 1 | Full Raspberry Pi header label appears in CAD source; not evidence of active flow routing. |
| ACTIVE_NEEDS_REVIEW | `REVIEW_REQUIRED.md` | `MAX1239` | 9 | Intentional review item. |
| ACTIVE_NEEDS_REVIEW | `REVIEW_REQUIRED.md` | `GPIO6` | 20 | Intentional physical review item for legacy flow setup. |
| ACTIVE_NEEDS_REVIEW | `REVIEW_REQUIRED.md` | `/sys/bus/w1` | 21 | Intentional physical review item for legacy direct DS18B20 wiring. |
| DOC_REFERENCE_ONLY | `software/README.md` | `GPIO6` | 12 | States legacy GPIO6 flow scripts are not active. |

## Classification Notes

- `ACTIVE_FIXED`: no remaining active-code rows in this search.
- `ACTIVE_NEEDS_REVIEW`: copied active source material or review gates that need
  human confirmation before actuation.
- `LEGACY_DEPRECATED`: not searched in this active-area pass by instruction.
- `DOC_REFERENCE_ONLY`: documentation-only safety/history references, not active
  runtime behavior.
