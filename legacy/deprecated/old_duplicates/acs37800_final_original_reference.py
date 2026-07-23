#!/usr/bin/env python3
from smbus2 import SMBus
import time, json, os
from datetime import datetime

# -----------------------------
# User setup (your confirmed)
# -----------------------------
ADDR = 0x60
BUS  = 1

# 32-bit little-endian registers
REG_RMS   = 0x20   # [15:0]=VRMS(u16), [31:16]=IRMS(s16)
REG_PQ    = 0x21   # [15:0]=PACTIVE(s16), [31:16]=PIMAG(u16)
REG_SPF   = 0x22   # [15:0]=PAPP(u16), [26:16]=PF(11b signed), bit27 posangle, bit28 pospf

# Folder/file locations
FOLDER   = os.path.expanduser("./")
CAL_FILE = os.path.join(FOLDER, "acs37800_cal.json")

# Noise floors (tune if needed)
# These prevent "ghost" readings when VINP/inputs float (chip powered but mains/load removed)
NOISE_FLOOR_VRMS_CODES = 300    # raw codes near baseline treated as 0V
NOISE_FLOOR_IRMS_CODES = 80     # raw codes near baseline treated as 0A
NOISE_FLOOR_V_VOLTS    = 5.0    # Vrms below this -> show 0.0
NOISE_FLOOR_I_AMPS     = 0.20   # Irms below this -> show 0.0

# Power sign handling:
# If you want consumed power always positive, keep POWER_ABS=True
POWER_ABS = True


# -----------------------------
# Helpers
# -----------------------------
def u16(x): return x & 0xFFFF

def s16(x):
    x &= 0xFFFF
    return x - 0x10000 if (x & 0x8000) else x

def read32_le(bus, reg):
    # Returns None on I2C error
    try:
        b = bus.read_i2c_block_data(ADDR, reg, 4)
    except Exception:
        return None
    return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)

def pf_from_11bit(pf11):
    # Signed 11-bit with 10 fractional bits (range about -1..+1)
    pf11 &= 0x7FF
    if pf11 & 0x400:
        pf11 -= 0x800
    return pf11 / (2**10)

def load_cal():
    cal = {
        # scales convert (raw - offset) -> engineering units
        "vrms_scale": None,     # V per code
        "irms_scale": None,     # A per code
        # offsets are captured raw baselines
        "vrms_offset": 0,       # VRMS_raw at 0V (mains/transformer off but chip powered)
        "irms_offset": 0,       # IRMS_raw at 0A (voltage present but no load)
        # saved metadata
        "last_cal_time": None,
        "line_vrms_used": None,
        "clamp_irms_used": None
    }
    if os.path.exists(CAL_FILE):
        try:
            with open(CAL_FILE, "r") as f:
                cal.update(json.load(f))
        except Exception:
            pass
    return cal

def save_cal(cal):
    os.makedirs(FOLDER, exist_ok=True)
    with open(CAL_FILE, "w") as f:
        json.dump(cal, f, indent=2)

def get_values(bus, cal):
    r20 = read32_le(bus, REG_RMS)
    r21 = read32_le(bus, REG_PQ)
    r22 = read32_le(bus, REG_SPF)

    if (r20 is None) or (r21 is None) or (r22 is None):
        return None

    vrms_raw = u16(r20)
    irms_raw = s16(r20 >> 16)

    pactive_raw = s16(u16(r21))
    pimag_raw   = u16(r21 >> 16)

    papparent_raw = u16(r22)
    pf11 = (r22 >> 16) & 0x7FF
    pf = pf_from_11bit(pf11)

    # ---------- Raw-domain clamping (prevents floating-input ghosts) ----------
    vr0 = int(cal.get("vrms_offset", 0))
    ir0 = int(cal.get("irms_offset", 0))

    if abs(vrms_raw - vr0) < NOISE_FLOOR_VRMS_CODES:
        vrms_raw = vr0

    if abs(irms_raw - ir0) < NOISE_FLOOR_IRMS_CODES:
        irms_raw = ir0
    # ------------------------------------------------------------------------

    vrms = None
    if cal["vrms_scale"] is not None:
        vrms = (vrms_raw - vr0) * float(cal["vrms_scale"])

    irms = None
    if cal["irms_scale"] is not None:
        irms = (irms_raw - ir0) * float(cal["irms_scale"])

    # Engineering-domain clamping
    if vrms is not None and vrms < NOISE_FLOOR_V_VOLTS:
        vrms = 0.0
    if irms is not None and abs(irms) < NOISE_FLOOR_I_AMPS:
        irms = 0.0

    # Power estimate using PF from chip
    p_est = None
    if (vrms is not None) and (irms is not None):
        p_est = vrms * irms * pf
        if POWER_ABS:
            p_est = abs(p_est)

    return {
        "vrms_raw": vrms_raw,
        "irms_raw": irms_raw,
        "pactive_raw": pactive_raw,
        "pimag_raw": pimag_raw,
        "papparent_raw": papparent_raw,
        "pf": pf,
        "vrms": vrms,
        "irms": irms,
        "p_est": p_est,
    }

def calibrate(bus, cal):
    print("\n=== Calibration (Aligned to your setup) ===")
    print("NOTE: Your chip is powered by separate supply.")
    print("We will capture TWO baselines:")
    print("  A) VRMS offset at 0V (mains/transformer OFF, chip still powered)")
    print("  B) IRMS offset at 0A (voltage present, heater OFF / no load)")
    print("Then we capture two scales (240V and clamp current).\n")

    # A) Capture VRMS offset at 0V
    print("A) VRMS offset (0V): Turn OFF mains/transformer so VINP should be ~0V.")
    input("Press Enter to capture VRMS_raw offset (0V)...")
    vals = get_values(bus, cal)
    if vals is None:
        print("I2C read failed. Check wiring/address.")
        return
    cal["vrms_offset"] = int(vals["vrms_raw"])
    print(f"Captured VRMS offset = {cal['vrms_offset']} raw codes")

    # B) Capture IRMS offset at 0A with voltage present
    print("\nB) IRMS offset (0A): Turn ON mains (voltage present), but ensure NO LOAD (heater OFF).")
    input("Press Enter to capture IRMS_raw offset (0A)...")
    vals = get_values(bus, cal)
    if vals is None:
        print("I2C read failed. Check wiring/address.")
        return
    cal["irms_offset"] = int(vals["irms_raw"])
    print(f"Captured IRMS offset = {cal['irms_offset']} raw codes")

    # Voltage scale
    print("\nC) Voltage scale: keep mains ON (normal operation).")
    v_known = float(input("Enter TRUE line voltage Vrms (e.g., 240): ").strip())
    input("Press Enter to capture VRMS_raw for scaling...")
    vals = get_values(bus, cal)
    if vals is None:
        print("I2C read failed. Check wiring/address.")
        return
    vr = int(vals["vrms_raw"])
    denom_v = float(vr - cal["vrms_offset"])
    if abs(denom_v) < 10:
        print("VRMS_raw - vrms_offset is too small. Is mains really ON? Is VINP driven?")
        return
    cal["vrms_scale"] = v_known / denom_v
    cal["line_vrms_used"] = v_known
    print(f"VRMS_raw={vr} => vrms_scale={cal['vrms_scale']:.10f} V/code")

    # Current scale
    print("\nD) Current scale: turn ON heater so current flows. Use clamp meter.")
    i_known = float(input("Enter TRUE current Irms from clamp (e.g., 18.7): ").strip())
    input("Press Enter to capture IRMS_raw under load...")
    vals = get_values(bus, cal)
    if vals is None:
        print("I2C read failed. Check wiring/address.")
        return
    ir = int(vals["irms_raw"])
    denom_i = float(ir - cal["irms_offset"])
    if abs(denom_i) < 10:
        print("IRMS_raw - irms_offset is too small. Increase load and try again.")
        return
    cal["irms_scale"] = i_known / denom_i
    cal["clamp_irms_used"] = i_known
    print(f"IRMS_raw={ir} => irms_scale={cal['irms_scale']:.10f} A/code")

    cal["last_cal_time"] = datetime.now().isoformat(timespec="seconds")
    save_cal(cal)
    print(f"\nSaved calibration to: {CAL_FILE}\n")


def main():
    os.makedirs(FOLDER, exist_ok=True)
    cal = load_cal()

    csv_name = datetime.now().strftime("acs37800_%Y%m%d_%H%M%S.csv")
    csv_path = os.path.join(FOLDER, csv_name)

    with SMBus(BUS) as bus, open(csv_path, "w") as f:
        f.write("time,vrms,irms,p_est,pf,vrms_raw,irms_raw,pactive_raw,pimag_raw,papparent_raw\n")
        print(f"Logging to: {csv_path}")
        print("Commands:")
        print("  c  -> full calibration (recommended)")
        print("  Enter -> start using saved calibration\n")
        cmd = input("> ").strip().lower()
        if cmd == "c":
            calibrate(bus, cal)

        cal = load_cal()

        while True:
            t = datetime.now().isoformat(timespec="seconds")
            vals = get_values(bus, cal)

            if vals is None:
                print(f"{t}  I2C READ ERROR")
                time.sleep(1)
                continue

            vrms = vals["vrms"]
            irms = vals["irms"]
            p_est = vals["p_est"]
            pf = vals["pf"]

            vrms_s = "None" if vrms is None else f"{vrms:.2f}"
            irms_s = "None" if irms is None else f"{irms:.2f}"
            p_s    = "None" if p_est is None else f"{p_est:.1f}"

            print(f"{t}  Vrms={vrms_s}  Irms={irms_s}  P={p_s} W  PF={pf:+.3f}  "
                  f"(raw vr={vals['vrms_raw']} ir={vals['irms_raw']})")

            f.write(f"{t},{vrms if vrms is not None else ''},{irms if irms is not None else ''},"
                    f"{p_est if p_est is not None else ''},{pf},"
                    f"{vals['vrms_raw']},{vals['irms_raw']},{vals['pactive_raw']},"
                    f"{vals['pimag_raw']},{vals['papparent_raw']}\n")
            f.flush()

            time.sleep(1)


if __name__ == "__main__":
    main()
