# Completed Verification Records

This folder stores dated WH1 verification records for checks that have been completed.

A record belongs here when the check has a clear result, date, and verifier.

Examples:

- Hardware identity checks
- GPIO and signal-mapping checks
- Relay or valve operation checks
- Sensor scaling checks
- Deployment-readiness checks

## Rule

Completed verification records should explain:

- What was checked
- How it was checked
- Who checked it
- When it was checked
- What result was observed
- What related review items remain open

Do not use this folder for unresolved tasks. Open items belong in `../review_pending/`.

When repository paths or normalized hardware-document names change, update the
affected record without changing its original verification date or claiming a
new physical verification. Add a dated repository-review note to distinguish the
documentation update from the original lab check.
