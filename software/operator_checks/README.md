# Operator checks

Manually invoked live-hardware inspection tools.

These answer questions such as whether the ADC responds, what raw values sensors produce,
whether ACS37800 setup is ready for review, or whether the valve relay path operates.

These modules may:

- construct fake station hardware objects
- parse a small inspection CLI
- format operator output

Reusable workflows belong in `software/services/`, and laptop-safe assertion tests
belong in `tests/`.

## NOTE

`valve_gpio_check.py` is dry-run by default but can actuate GPIO only when the operator
explicitly passes `--enable-output`. The other current checks do not drive station outputs.
