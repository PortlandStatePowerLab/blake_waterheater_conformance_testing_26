# Entrypoints

Startup boundaries for operators or external callers.

An entrypoint may:

- parse arguments
- load configuration
- call subsystem builders
- construct dependencies
- invoke services
- format terminal output
- choose exit codes

Entrypoints should contain minimal business logic and no duplicated hardware-control
workflow.

## NOTICE

Reusable workflows belong in `software/services/`. Operator shell wrappers in
`bin/` should call entrypoints and locate the repository __without__ assuming the
shell's current working directory.
