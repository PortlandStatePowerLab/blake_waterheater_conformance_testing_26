# WH1 Review Required

These items need human or hardware verification before Pi deployment moves past
read-only diagnostics.

## Hardware identity

- Confirm actual board marking for U11. Staging treats U11 as MAX1238EEE+.               done
- Resolve any source document or CAD metadata that still names MAX1239.                  depricated
- Confirm U12 is the TXS0104E level shifter path between Pi-side I2C and the
  MAX1238 side.                                                                          done
- Confirm U13 is ACS37800 and the usable part variant/register map.                      done

## GPIO and signal mapping

- Confirm valve relay output behavior, including active polarity and fail-safe
  state, before any `--enable-output` valve test.                                        done
- Confirm ACS37800 DIO_0 maps to GPIO18.                                                 done
- Confirm ACS37800 DIO_1 maps to GPIO26.                                                 done
- Confirm whether any legacy GPIO6 pulse-flow setup still exists physically.
- Confirm whether any direct `/sys/bus/w1` DS18B20 sensor wiring still exists
  physically.

## Software and data

- Confirm correct schedule CSVs before re-enabling any scheduled draw workflow.
- Confirm flow transmitter calibration and gallons-per-minute scaling.
- Confirm temperature transmitter scaling and cold/hot channel readings on CH1
  and CH0.
- Keep ADC channel constants sourced from `software/common/hardware_map.py`.

## Documents

- Treat Word documents in `docs/reference_only/` as historical unless no better
  source exists.
- Audit reports and crash recovery notes may mention stale script behavior; do
  not use them as deployment instructions.
