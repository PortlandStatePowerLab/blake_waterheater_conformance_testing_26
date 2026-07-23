# GS10 drive

## Purpose

Direct RS-485 Modbus RTU communication with the DURApulse GS10 AC drive.

## Contains

- `gs10_modbus_driver.py`: opens the serial connection and reads holding registers.

## Does not belong here

- CTA-2045 protocol code or generic station runtime behavior.

## Role rules

A driver directly communicates with a hardware device or low-level protocol.

## Usage

Operators run `bin/gs10-modbus-check`.

## Safety notes

The driver accesses a real RS-485 device associated with mains-powered equipment. Do not run it against an unidentified serial port.
