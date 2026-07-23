"""Direct Raspberry Pi GPIO driver for the WH1 valve relay."""

from __future__ import annotations

from types import ModuleType


class GpioValveDriver:
    """Drive one valve-relay GPIO and return it LOW during cleanup."""

    def __init__(self, gpio: ModuleType, pin: int) -> None:
        self._gpio = gpio
        self._pin = pin
        self._closed = False

    def open(self) -> None:
        self._gpio.output(self._pin, self._gpio.HIGH)

    def close(self) -> None:
        self._gpio.output(self._pin, self._gpio.LOW)

    def cleanup(self) -> None:
        if self._closed:
            return
        try:
            self.close()
        finally:
            self._gpio.cleanup(self._pin)
            self._closed = True

    def __enter__(self) -> "GpioValveDriver":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.cleanup()
