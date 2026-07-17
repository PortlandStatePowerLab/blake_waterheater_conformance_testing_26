<!-- markdownlint-configure-file { "MD046": { "style": "fenced" } } -->

# Diagnostic Tests for the 40-Count Delta on MAX1238 CH2

---
MAX1238’s repeat-selected-channel scan mode:

- The chip performs scan conversions successively using an 800 ns track/hold acquisition interval and a 22 pF input capacitance, then returns results FIFO

---

```python
import time

from software.adc.max1238_builder import build_max1238
from software.adc.max1238 import InputMode, ScanMode
from software.common.hardware_map import CH_FLOW

adc = build_max1238()

try:
    for sample_number in range(1, 11):
        single_before_counts = adc.read_single(CH_FLOW)

        config_byte = adc._build_config_byte(
            ScanMode.RepeatSelect8x,
            CH_FLOW,
            InputMode.SingleEnded,
        )

        raw_bytes = adc._xfer(config_byte, 16)

        repeated_counts = [
            ((raw_bytes[index] & 0x0F) << 8) | raw_bytes[index + 1]
            for index in range(0, 16, 2)
        ]

        single_after_counts = adc.read_single(CH_FLOW)

        print(
            f"sample={sample_number:02d} "
            f"single_before={single_before_counts} "
            f"repeat8={repeated_counts} "
            f"single_after={single_after_counts}"
        )
        time.sleep(0.10)
finally:
    adc.close()
```

## Repeat-Selected-Channel Scan Outputs

```text
sample=01 single_before=480 repeat8=[477, 492, 496, 494, 490, 491, 492, 492] single_after=483
sample=02 single_before=481 repeat8=[479, 495, 495, 491, 490, 493, 493, 491] single_after=478
sample=03 single_before=480 repeat8=[478, 490, 494, 494, 493, 490, 492, 494] single_after=483
sample=04 single_before=480 repeat8=[482, 493, 490, 491, 493, 493, 492, 493] single_after=481
sample=05 single_before=482 repeat8=[479, 490, 494, 493, 490, 492, 496, 493] single_after=481
sample=06 single_before=480 repeat8=[480, 495, 494, 488, 493, 495, 492, 490] single_after=480
sample=07 single_before=481 repeat8=[480, 492, 496, 494, 490, 493, 495, 492] single_after=482
sample=08 single_before=480 repeat8=[477, 495, 494, 489, 492, 495, 494, 490] single_after=477
sample=09 single_before=479 repeat8=[481, 494, 492, 491, 493, 493, 494, 491] single_after=482
sample=10 single_before=476 repeat8=[478, 495, 494, 490, 492, 496, 492, 491] single_after=476
```

Interpretation:

- First repeat low, later repeats recover toward 480: track/hold or input-settling behavior.
- All eight repeats near 480: likely interaction from scanning CH0 → CH1 → CH2.
- All eight repeats near 440: likely a broader scan-mode or transaction behavior.

## Determine When CH2 Goes Low

Next, determine whether CH2 goes low:

- whenever scanning AIN0 → AIN2,
- or only when the scan continues through AIN3.

---

```python
import time

from software.adc.max1238_builder import build_max1238
from software.common.hardware_map import (
    CH_AMBIENT,
    CH_FLOW,
    CH_HOT,
)

adc = build_max1238()

try:
    for sample_number in range(1, 11):
        if sample_number % 2:
            scan_to_flow = adc.read_range(CH_HOT, CH_FLOW)
            scan_to_ambient = adc.read_range(CH_HOT, CH_AMBIENT)
        else:
            scan_to_ambient = adc.read_range(CH_HOT, CH_AMBIENT)
            scan_to_flow = adc.read_range(CH_HOT, CH_FLOW)

        single_flow_counts = adc.read_single(CH_FLOW)

        scan_0_to_2_counts = scan_to_flow[CH_FLOW]
        scan_0_to_3_counts = scan_to_ambient[CH_FLOW]

        print(
            f"sample={sample_number:02d} "
            f"scan_0_to_2_flow={scan_0_to_2_counts} "
            f"scan_0_to_3_flow={scan_0_to_3_counts} "
            f"single_flow={single_flow_counts} "
            f"delta_single_minus_0_to_2="
            f"{single_flow_counts - scan_0_to_2_counts} "
            f"delta_single_minus_0_to_3="
            f"{single_flow_counts - scan_0_to_3_counts}"
        )

        time.sleep(0.10)
finally:
    adc.close()
```

## CH2-Low Outputs

```text
sample=01 scan_0_to_2_flow=450 scan_0_to_3_flow=444 single_flow=477 delta_single_minus_0_to_2=27 delta_single_minus_0_to_3=33
sample=02 scan_0_to_2_flow=445 scan_0_to_3_flow=443 single_flow=481 delta_single_minus_0_to_2=36 delta_single_minus_0_to_3=38
sample=03 scan_0_to_2_flow=445 scan_0_to_3_flow=443 single_flow=477 delta_single_minus_0_to_2=32 delta_single_minus_0_to_3=34
sample=04 scan_0_to_2_flow=443 scan_0_to_3_flow=444 single_flow=481 delta_single_minus_0_to_2=38 delta_single_minus_0_to_3=37
sample=05 scan_0_to_2_flow=447 scan_0_to_3_flow=447 single_flow=477 delta_single_minus_0_to_2=30 delta_single_minus_0_to_3=30
sample=06 scan_0_to_2_flow=445 scan_0_to_3_flow=445 single_flow=483 delta_single_minus_0_to_2=38 delta_single_minus_0_to_3=38
sample=07 scan_0_to_2_flow=446 scan_0_to_3_flow=443 single_flow=481 delta_single_minus_0_to_2=35 delta_single_minus_0_to_3=38
sample=08 scan_0_to_2_flow=445 scan_0_to_3_flow=440 single_flow=483 delta_single_minus_0_to_2=38 delta_single_minus_0_to_3=43
sample=09 scan_0_to_2_flow=445 scan_0_to_3_flow=442 single_flow=478 delta_single_minus_0_to_2=33 delta_single_minus_0_to_3=36
sample=10 scan_0_to_2_flow=449 scan_0_to_3_flow=440 single_flow=481 delta_single_minus_0_to_2=32 delta_single_minus_0_to_3=41
```

Interpretation:

- Both scans read near 440: the problem happens during the AIN0 → AIN1 → AIN2 transition.
- 0→2 reads near 480 but 0→3 reads near 440: including or reading AIN3 is affecting CH2,pointing toward scan-memory/read-length handling rather than basic CH2 acquisition.
- Both read near 480: the earlier test sequence itself exposed another state-dependent interaction.

## Internal Clock vs. External Clock Timing

Next, check the internal-clock scan versus the external-clock scan.

---

```python
import time

from software.adc.max1238_builder import build_max1238
from software.adc.max1238 import (
    ClockType,
    Polarity,
    ReferenceVoltage,
    ResetMode,
)
from software.common.hardware_map import CH_FLOW, CH_HOT

adc = build_max1238()

try:
    adc.setup_adc(
        referenceVoltage=ReferenceVoltage.InternalRef_AlwaysON_AnalogIn,
        clock=ClockType.External,
        polarity=Polarity.Unipolar,
        reset=ResetMode.NoAction,
    )
```

## Clock-Timing Outputs

```text
sample=01 external_grouped_flow=481 external_single_flow=476 delta_single_minus_grouped=-5
sample=02 external_grouped_flow=476 external_single_flow=475 delta_single_minus_grouped=-1
sample=03 external_grouped_flow=479 external_single_flow=479 delta_single_minus_grouped=0
sample=04 external_grouped_flow=479 external_single_flow=482 delta_single_minus_grouped=3
sample=05 external_grouped_flow=479 external_single_flow=484 delta_single_minus_grouped=5
sample=06 external_grouped_flow=475 external_single_flow=484 delta_single_minus_grouped=9
sample=07 external_grouped_flow=484 external_single_flow=478 delta_single_minus_grouped=-6
sample=08 external_grouped_flow=477 external_single_flow=479 delta_single_minus_grouped=2
sample=09 external_grouped_flow=476 external_single_flow=477 delta_single_minus_grouped=1
sample=10 external_grouped_flow=476 external_single_flow=481 delta_single_minus_grouped=5
```

Interpretation:

Grouped CH2 recovers near 480: internal-clock scan settling/timing is the leading cause.
Grouped CH2 remains near 440: the issue is not fixed by slower SCL-driven acquisition,
next inspect the analog buffer/node behavior during mux scanning.

## Initial Findings

Known:

- the bad CH2 result is caused by the MAX1238’s internal-clock multichannel acquisition behavior on this installed analog front end.

Leading explanation:

- CH2 is not settling sufficiently before the internal-clock scan captures it. The MAX1238 uses an input mux and track/hold capacitor, lists an 800 ns acquisition time and 22 pF input capacitance, while external-clock mode makes SCL the conversion clock.

Still unknown:

- Exactly which board-level detail makes CH2 the sensitive one—LM324 settling, mux charge transfer, source impedance, capacitance, or some combination.
- We do not need that final microscopic explanation before fixing software configuration because the clock-mode A/B test is extremely clean.

Follow up ruleset:

We should not change the builder yet until the complete grouped SensorReader snapshot
is proven under external clock

## External-Clock Snapshot

Next, check the grouped snapshot under external clock.

---

```python
import time

from software.adc.max1238_builder import build_max1238
from software.adc.max1238 import (
    ClockType,
    Polarity,
    ReferenceVoltage,
    ResetMode,
)
from software.sensor_ops import SensorReader

adc = build_max1238()

try:
    adc.setup_adc(
        referenceVoltage=ReferenceVoltage.InternalRef_AlwaysON_AnalogIn,
        clock=ClockType.External,
        polarity=Polarity.Unipolar,
        reset=ResetMode.NoAction,
    )

    time.sleep(0.010)

    sensor_reader = SensorReader(adc)

    for sample_number in range(1, 11):
        snapshot = sensor_reader.get_sensor_snapshot()

        print(
            f"sample={sample_number:02d} "
            f"hot_raw={snapshot.hot_raw_counts} "
            f"cold_raw={snapshot.cold_raw_counts} "
            f"flow_raw={snapshot.flow_raw_counts} "
            f"ambient_raw={snapshot.ambient_raw_counts} "
            f"hot_c={snapshot.hot_temp_c:.2f} "
            f"cold_c={snapshot.cold_temp_c:.2f} "
            f"flow_gpm={snapshot.flow_gpm:.3f} "
            f"ambient_c={snapshot.ambient_temp_c:.2f}"
        )

        time.sleep(0.10)

finally:
    adc.close()
```

## External-Clock Snapshot Outputs

```text
sample=01 hot_raw=1142 cold_raw=1149 flow_raw=481 ambient_raw=224 hot_c=18.96 cold_c=19.69 flow_gpm=0.005 ambient_c=22.40
sample=02 hot_raw=1144 cold_raw=1145 flow_raw=480 ambient_raw=228 hot_c=19.17 cold_c=19.27 flow_gpm=0.000 ambient_c=22.80
sample=03 hot_raw=1140 cold_raw=1148 flow_raw=482 ambient_raw=229 hot_c=18.75 cold_c=19.58 flow_gpm=0.010 ambient_c=22.90
sample=04 hot_raw=1143 cold_raw=1145 flow_raw=479 ambient_raw=229 hot_c=19.06 cold_c=19.27 flow_gpm=-0.005 ambient_c=22.90
sample=05 hot_raw=1146 cold_raw=1145 flow_raw=477 ambient_raw=225 hot_c=19.38 cold_c=19.27 flow_gpm=-0.016 ambient_c=22.50
sample=06 hot_raw=1143 cold_raw=1145 flow_raw=482 ambient_raw=227 hot_c=19.06 cold_c=19.27 flow_gpm=0.010 ambient_c=22.70
sample=07 hot_raw=1138 cold_raw=1147 flow_raw=476 ambient_raw=226 hot_c=18.54 cold_c=19.48 flow_gpm=-0.021 ambient_c=22.60
sample=08 hot_raw=1140 cold_raw=1148 flow_raw=482 ambient_raw=228 hot_c=18.75 cold_c=19.58 flow_gpm=0.010 ambient_c=22.80
sample=09 hot_raw=1142 cold_raw=1147 flow_raw=480 ambient_raw=231 hot_c=18.96 cold_c=19.48 flow_gpm=0.000 ambient_c=23.10
sample=10 hot_raw=1149 cold_raw=1145 flow_raw=481 ambient_raw=230 hot_c=19.69 cold_c=19.27 flow_gpm=0.005 ambient_c=23.00
```

Expected result:

- CH2 should stay around 0.475–0.485 V / 475–485 counts and the grouped flow should land close to 0 GPM instead of roughly −0.22 GPM.

## Secondary Findings

With external clock:

- Grouped CH2: 476–482 counts
- Equivalent input: 0.476–0.482 V
- Converted flow: −0.021 to +0.010 GPM
- Hot, cold, and ambient remained plausible
- The former grouped result around 440 counts / −0.22 GPM is gone

## Proven Thus Far

- Internal-clock multichannel scanning produces the CH2 error on this board.
- External-clock operation removes it.
- This is not a calibration offset.
- We still do not clamp the tiny near-zero negative flow readings.

## Resulting Action

Promoting external clock operation into the station MAX1238 builder to make
acquisition diagnostic more accurate
