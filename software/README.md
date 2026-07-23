# Software

## Purpose

Active WH1 Python code, organized so folders identify the subsystem and filenames identify the role.

## Contains

- `station/`: physical station assignments.
- `adc/`, `sensors/`, `valve/`, `power/`, `gs10_drive/`: subsystem code.
- `runtime/`: coordinated station procedures.
- `commands/`: user-invoked Python entrypoints.

## Does not belong here

- Historical scripts, generated measurements, or hardware drawings.

## Role rules

Drivers communicate with hardware; builders construct dependencies; interfaces define required operations; readers process measurements; diagnostics verify behavior; commands are user entrypoints; workflows are finite lab procedures.

## Usage

Import modules as `software.<subsystem>.<role_file>` or use a command under `bin/`.
