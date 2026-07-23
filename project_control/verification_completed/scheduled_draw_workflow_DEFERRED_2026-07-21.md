# Scheduled Draw Workflow Deployment Decision

Status: DEFERRED
Decision date: 2026-07-21
Decision by: Blake Ellis
Station: WH1

## Scope

Determine whether schedule CSVs and schedule-driven water-draw controllers must
be selected, tested, or restored for the current WH1 deployment.

## Decision

Scheduled CSV-driven water draws are deferred and are not required for the
current WH1 deployment. The legacy schedule controllers must not be restored or
silently reactivated during this cleanup.

## Current supported behavior

The supported operator path is one controlled draw per invocation through:

```bash
bin/wh-draw --target-gal <gallons>
```

Actual valve output additionally requires `--enable-output` and remains subject
to the open calibration and controlled-run verification gates.

## Deployment status

- Schedule CSVs are excluded from the active deployment.
- Legacy schedule-controller code is excluded from the active deployment.
- Existing schedule CSVs and controllers remain preserved as historical or
  reference material under `legacy_deprecated/`.
- No legacy schedule file or controller is deleted by this decision.

## Verification method

Repository and deployment-scope review confirmed that the active
`bin/wh-draw` interface accepts `--target-gal` and does not load a
schedule CSV. The deployment manifest excludes `legacy_deprecated/` from the
runtime payload.

## Result

NOT APPLICABLE - DEFERRED

No schedule-driven feature is being activated, so schedule selection or runtime
testing is not required to close this deployment review item.

## Future direction

If scheduled draws are added later, implement them as a separate, explicit
entrypoint or service that calls the same validated single-draw operation. Do
not revive the legacy schedule controller wholesale.

## Follow-up items

None for the current WH1 deployment. A future scheduled-draw feature must open
its own design, schedule-schema, validation, and controlled-run review items.
