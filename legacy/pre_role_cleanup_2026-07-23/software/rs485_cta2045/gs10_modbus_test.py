#!/usr/bin/env python3

import argparse
import sys
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default="/dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=9600)
    parser.add_argument("--parity", default="N", choices=["N", "E", "O"])
    parser.add_argument("--stopbits", type=int, default=1, choices=[1,2])
    parser.add_argument("--bytesize", type=int, default=8, choices=[7,8])
    parser.add_argument("--slave", type=int, default=1)
    parser.add_argument("--reg", type=int, default=0x2000)#holding register
    parser.add_argument("--count", type=int, default=1)
    parser.add_argument("--timeout", type=float, default=0.5)
    args = parser.parse_args()

    client = ModbusSerialClient (
            port=args.port,
            baudrate=args.baud,
            parity=args.parity,
            stopbits=args.stopbits,
            bytesize=args.bytesize,
            timeout=args.timeout,
            retries=5,
            #strict=False,
            framer="rtu",
            )

    if not client.connect():
        print(f"ERROR: could not open serial port {args.port}")
        return 2

    try:
        resp = client.read_holding_registers (address=args.reg,
                count=args.count,slave=args.slave)

        if resp.isError():
            print(f"Modbus error: {resp}")
            return 1

        print(f"OK, client={args.slave} reg=0x{args.reg:04X} ({args.reg})->{resp.registers}")
        return 0

    except (ModbusException, OSError) as e:
        print(f"Exception: {e}")
        return 1

    finally:
        client.close()

if __name__=="__main__":
    sys.exit(main())


