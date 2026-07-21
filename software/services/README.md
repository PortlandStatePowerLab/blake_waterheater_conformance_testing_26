# Services

Reusable project operations and workflows that coordinate lower-level components.

A service may:

- validate workflow inputs
- collect initial sensor readings
- control a water draw through an injected valve boundary
- accumulate flow
- record a result

## NOTICE

Services do not parse command-line arguments or own terminal formatting.
Entrypoints, automated tests, scheduled processes, or future GUIs may call them.
