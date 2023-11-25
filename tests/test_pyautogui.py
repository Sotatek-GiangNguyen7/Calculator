import unittest
import pyautogui
import uiautomation as automation
import time
from calculator import Calculator

calculator_object = Calculator()
class CalculatorAutomationTest(unittest.TestCase):

    def setUp(self):
        # Open Windows Calculator
        pyautogui.press('win')
        pyautogui.write('Calculator')
        pyautogui.press('enter')

        # Wait for the Calculator to open
        time.sleep(2)
        calculator_object.get_windows()

    def tearDown(self):
        # Close the Calculator window
        pyautogui.hotkey('alt', 'f4')

    def test_addition(self):
        calculator_object.click_to_navigate()
        calculator_object.click_to_mode('Standard Calculator')
        a = 5
        b = 3  
        calculator_object.perform_calculation(a, "+", b, a + b)
        # Verify result
        self.assertEqual(str(a + b), calculator_object.get_calculator_result() ,"Test Addition Failed")

    def test_programmer_mode(self):
        calculator_object.click_to_navigate()
        calculator_object.click_to_mode('Programmer Calculator')

    def test_subtraction(self):
        calculator_object.click_to_navigate()
        calculator_object.click_to_mode('Standard Calculator')
        a = 8 
        b = 3
        calculator_object.perform_calculation(a, "-", b, a - b, "Test Subtraction Failed")
        # Verify result
        self.assertEqual(str(a - b), calculator_object.get_calculator_result())

if __name__ == '__main__':
    unittest.main()
