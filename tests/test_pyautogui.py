import unittest
import pyautogui
import uiautomation as automation
import time
from calculator import Calculator

class CalculatorAutomationTest(unittest.TestCase):

    def setUp(self):
        # Open Windows Calculator
        pyautogui.press('win')
        pyautogui.write('Calculator')
        pyautogui.press('enter')

        # Wait for the Calculator to open
        time.sleep(2)


    def tearDown(self):
        # Close the Calculator window
        pyautogui.hotkey('alt', 'f4')

    def test_operation(self):
        calculator_object = Calculator()
        a = 1
        b = 2
        calculator_object.perform_calculation(a, "+", b, a + b)
        # Verify result
        self.assertEqual(str(a + b), calculator_object.get_calculator_result())
if __name__ == '__main__':
    unittest.main()
