# Smart Water Heater Test Station - Rev A

## Overview

This repository contains the Rev A documentation and supporting project files for the **Smart Water Heater Test Station** developed in the **Power Engineering Lab at Portland State University**.

The station is an embedded monitoring and control platform for smart-grid water heater research. It integrates four residential electric water heater units with custom PCB hardware, Raspberry Pi controllers, industrial sensors, AC power monitoring, relay-based valve control, and data acquisition software.

This project was designed, built, documented, and validated by **Nawaf Altalhi** as an Undergraduate Research Assistant in the PSU Power Engineering Lab under the supervision of **Prof. Robert Bass**.

## Project Purpose

The purpose of this project is to support automated testing and long-term evaluation of residential electric water heaters in a smart-grid research environment.

The system provides:

* Real-time temperature monitoring
* Flow-rate monitoring
* AC voltage and current measurement
* Power and energy monitoring
* Relay-controlled water draw operation
* Raspberry Pi-based data acquisition
* RS-485 / CTA-2045 communication support
* Per-unit embedded control and monitoring hardware

## Repository Contents

```text
Smart Water Heater Test Station/
│
├── Smart Water Heater Test Station - Hardware Design and System Integration - Rev A.pdf
│
├── Schematics/
│   └── Schematic exports and reference schematic files
│
├── System Diagrams/
│   └── System architecture and AC wiring diagrams
│
├── PCB Gerber Fabrication Files/
│   └── Gerber files for PCB fabrication
│
├── Water Heater Test Station - Schematic and PCB EasyEDA Source - Rev A/
│   └── EasyEDA schematic and PCB source files
│
├── Wiring and Connection Guide/
│   └── Wall-mounted wiring and connection guide files
│
└── Water Heater Control and Monitoring Software/
    └── ADC readings, power monitoring, and control software documents
```

## Main Documentation

The primary technical reference is:

**Smart Water Heater Test Station - Hardware Design and System Integration - Rev A.pdf**

This document covers:

* Project overview
* System architecture
* Hardware design
* PCB schematic and layout
* Sensor interface and signal conditioning
* ADC and I2C communication
* Relay and valve control
* RS-485 communication interface
* ACS37800 AC power monitoring
* Electrical installation
* AC panel wiring
* Plumbing and sensor installation
* Calculations
* Testing and validation
* Troubleshooting
* Future operator notes
* Bill of materials

## Hardware Summary

Each water heater unit includes:

* One custom PCB
* One Raspberry Pi controller
* 4–20 mA temperature and flow sensor inputs
* MAX1238 12-bit I2C ADC
* LM324 signal-conditioning stages
* TXS0104E I2C level shifter
* ACS37800 power monitoring IC
* Relay driver for solenoid valve control
* RS-485 / CTA-2045 communication support
* 24 VDC sensor supply interface
* AC monitoring and valve-control terminals

## PCB Design

The PCB was designed in **EasyEDA** and fabricated as a 2-layer board. The design separates low-voltage analog/digital circuitry from high-voltage AC monitoring and switching sections using physical layout partitioning, isolation cutouts, and spacing.

The repository includes both:

* EasyEDA schematic and PCB source files
* Gerber fabrication files

## Safety Notice

This project includes AC power wiring and high-voltage monitoring circuitry. Only trained personnel should work on the station hardware or wiring.

Before opening any enclosure or touching wiring, follow the power-down procedure documented in the wiring and connection guide.

Turning off the panel breakers may not de-energize every part of the station. Always verify 0 V at AC terminals before working on the system.

## Revision

| Revision | Date      | Description                |
| -------- | --------- | -------------------------- |
| Rev A    | June 2026 | Initial documented release |

## Author

**Nawaf Altalhi**
Hardware System Designer & Project Bring-Up
Undergraduate Research Assistant
Power Engineering Lab
Portland State University

## Supervisor

**Prof. Robert Bass**
Power Engineering Lab
Portland State University

## Notes for Future Users

Future students and lab users should begin with the main hardware documentation PDF, then refer to the wiring guide, schematics, source files, and Gerber files as needed.

Any future design changes should update:

* Hardware documentation
* Wiring and connection guide
* EasyEDA source files
* Gerber fabrication files
* Revision history
* README file
