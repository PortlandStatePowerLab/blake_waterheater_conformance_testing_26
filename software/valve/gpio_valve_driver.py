"""Direct Raspberry Pi GPIO driver for the WH1 valve relay."""

from __future__ import annotations

from types import ModuleType


class GpioValveDriver:
    """Drive one valve-relay GPIO and safely manage its lifecycle"""

    def __init__(self, gpio: ModuleType, pin: int) -> None:
        """Store the GPIO module and BCM pin used by the valve relay

        Args:
            gpio: Imported GPIO-compatible module
            pin: BCM GPIO pin number controlling the valve relay

        Safety:
            The builder must intialize the output LOW before constructing this driver
        """
        self._gpio = gpio
        self._pin = pin
        self._cleaned_up = False

    def _require_active(self)->None:
        """Reject GPIO commands after this driver has released its pin"""
        if self._cleaned_up:
            raise RuntimeError("valve GPIO drier has already been cleaned up")

    def open(self) -> None:
        """Assert the relay output HIGH to command the valve open"""
        self._require_active()
        self._gpio.output(self._pin, self._gpio.HIGH)

    def close(self) -> None:
        """Return the relay output LOW to command the valve closed"""
        self._require_active()
        self._gpio.output(self._pin, self._gpio.LOW)

    def cleanup(self) -> None:
        """Force the valve command LOW and release the GPIO pin once

        Safety:
            Cleanup is idempotent. Repeated calls do nothing. Once cleanup completes,
            further open or close commands raise RuntimeError
            """
        if self._cleaned_up:
            return

        try:
            self.close()
        finally:
            try:
                self._gpio.cleanup(self._pin)
            finally:
                self._cleaned_up = True

    def __enter__(self) -> "GpioValveDriver":
        """Return this activedriver for context-mamanger use"""
        self._require_active()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Force LOW and release the GPIO pin when leaving the context"""
        self.cleanup()
