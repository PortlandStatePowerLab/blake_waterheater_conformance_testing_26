# Helpers

Small reusable support code such as path resolution, timestamp creation,
formatting, and input validation.

Helpers do not:

- own hardware
- parse a complete CLI
- write complete run records
- coordinate lab workflows
- serve as a miscellaneous holding area

## NOTICE

Project code may import helpers; helpers do not import entrypoints or operator checks.
