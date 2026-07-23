# Bin

## Purpose

Short human-facing shell commands that locate the repository and invoke `software.commands` modules.

## Contains

- `adc-raw`, `adc-acquisition-compare`, `sensor-check`: read-only station checks.
- `valve-check`, `power-monitor-check`, `gs10-modbus-check`: subsystem checks.
- `wh-draw`: one controlled water draw.

## Does not belong here

- Python business logic, drivers, or copied implementations.

## Role rules

A shell command delegates to one Python command entrypoint.

## Usage

Run from any directory, for example `bin/sensor-check`.

## Safety notes

These wrappers can reach real hardware. Valve actuation and water draws require `--enable-output`; inspect GS10 serial-port arguments before use.
