# Project Control

This folder tracks review gates, verification records, and archived project-control notes for the staging repository.

Use this folder for project status documents, not runtime code.

- 'review_pending/': items that sitll need human, hardware, or software verification
- 'verification_completed/': records of checks that were completed and verified.
- 'verification_templates/': reusable templates for future verification records.
- 'archive/': old project-control notes that are no longer active but should be preserved.

## Rule

If something is still blocking deployment or hardware actuation, keep it in 'review_pending/'.

If something has been checked, tested, and recorded with a date/result, move or copy the record into 'verification_completed/'.
