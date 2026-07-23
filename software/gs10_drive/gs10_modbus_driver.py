"""Direct RS-485 Modbus RTU access for a DURApulse GS10 AC drive."""

from __future__ import annotations


def read_holding_registers(
    *,
    port: str,
    baud: int,
    parity: str,
    stopbits: int,
    bytesize: int,
    slave: int,
    register: int,
    count: int,
    timeout: float,
) -> list[int]:
    """Open the GS10 serial connection and read holding registers."""
    from pymodbus.client import ModbusSerialClient
    from pymodbus.exceptions import ModbusException

    client = ModbusSerialClient(
        port=port,
        baudrate=baud,
        parity=parity,
        stopbits=stopbits,
        bytesize=bytesize,
        timeout=timeout,
        retries=5,
        framer="rtu",
    )
    if not client.connect():
        raise ConnectionError(f"could not open serial port {port}")

    try:
        response = client.read_holding_registers(
            address=register,
            count=count,
            slave=slave,
        )
        if response.isError():
            raise RuntimeError(f"Modbus error: {response}")
        return list(response.registers)
    except (ModbusException, OSError) as error:
        raise RuntimeError(f"GS10 Modbus read failed: {error}") from error
    finally:
        client.close()
