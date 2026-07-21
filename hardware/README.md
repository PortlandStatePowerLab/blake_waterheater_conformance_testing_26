# hardware

Hardware reference material for the WH1 water heater test station.

## Belongs here

- Bills of materials
- Datasheets
- Human-readable wiring and mapping references
- PCB files
- Schematics

## Does not belong here

- Generated test data
- Python runtime files
- Temporary downloads that have not been reviewed
- Active station-control scripts

Hardware documents are reviewed reference inputs for lab students and operators;
they are not generated runtime output. The software source of truth for GPIO pins,
ADC channels, I2C addresses, and permanent assignments is
`software/common/hardware_map.py`. Do not create a second hardware-map document
that duplicates those constants.
