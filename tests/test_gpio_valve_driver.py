"""Laptop-safe tests for the Raspberry Pi GPIO valve driver"""

import unittest
from types import ModuleType

from software.valve.gpio_valve_driver import GpioValveDriver

class FakeGpio(ModuleType):
    """Record GPIO output and cleanup calls without touching real hardware"""

    HIGH = 1
    LOW = 0

    def __init__(self)->None:
        """Initialize an empty fake GPIO call history"""
        super().__init__("fake_gpio")
        self.output_calls: list[tuple[int, int]] = []
        self.cleanup_calls: list[int] = []

    def output(self, pin: int, state: int)->None:
        """Record one requested GPIO output state"""
        self.output_calls.append((pin, state))

    def cleanup(self, pin: int)->None:
        """Record cleanup of one GPIO pin"""
        self.cleanup_calls.append(pin)


class GpioValveDriverTest(unittest.TestCase):
    """Verify valve GPIO commands and resource-lifecycle behavior"""

    def setUp(self)->None:
        """Create a fresh fake GPIO module and valve driver for each test"""
        self.gpio = FakeGpio()
        self.pin = 17
        self.valve = GpioValveDriver(self.gpio, self.pin)

    def test_open_writes_gpio_high(self)->None:
        """Opening the valve should assert the relay output HIGH"""
        self.valve.open()

        self.assertEqual(self.gpio.output_calls, [(self.pin, self.gpio.HIGH)])

    def test_close_writes_gpio_low(self)->None:
        """Closing the valve should return the relay output to LOW"""
        self.valve.close()

        self.assertEqual(self.gpio.output_calls, [(self.pin, self.gpio.LOW)])

    def test_cleanup_forces_low_and_releases_pin_once(self)->None:
        """Cleanup should force LOW and remain safe when called repeatedly"""
        self.valve.cleanup()
        self.valve.cleanup()

        self.assertEqual(self.gpio.output_calls, [(self.pin, self.gpio.LOW)])
        self.assertEqual(self.gpio.cleanup_calls, [self.pin])

    def test_open_afer_cleanup_raises_runtime_error(self)->None:
        """A cleaned-up driver must not issue another GPIO HIGH command"""
        self.valve.cleanup()
        output_call_count = len(self.gpio.output_calls)

        with self.assertRaises(RuntimeError):
            self.valve.open()

        self.assertEqual(len(self.gpio.output_calls), output_call_count)

    def test_close_after_cleanup_raises_runtime_error(self)->None:
        """A cleaned-up driver must not issue another GPIO LOW command"""
        self.valve.cleanup()
        output_call_count = len(self.gpio.output_calls)

        with self.assertRaises(RuntimeError):
            self.valve.close()

        self.assertEqual(len(self.gpio.output_calls), output_call_count)


if __name__=="__main__":
    unittest.main()
