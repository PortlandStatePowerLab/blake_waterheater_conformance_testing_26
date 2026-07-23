# Power

## Purpose

WH1 ACS37800 calibration evidence and the current non-actuating ownership diagnostic.

## Contains

- `acs37800_cal.json`: WH1 calibration data.
- `power_monitor_diagnostic.py`: reports the verified external implementation boundary.

## Does not belong here

- Jeff's unmerged ACS37800 driver or guessed register access.

## Role rules

A diagnostic verifies or reports subsystem status; it is not a hardware driver.

## Usage

Operators run `bin/power-monitor-check`.

## Safety notes

The current diagnostic performs no I2C access and is laptop-safe. Future power drivers will interact with mains-connected measurement hardware and require explicit safety documentation.
