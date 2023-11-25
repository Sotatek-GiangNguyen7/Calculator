import unittest
import pyautogui
import uiautomation as automation
import time


class CalculatorAutomationTest(unittest.TestCase):

    def setUp(self):
        # Open Windows Calculator
        pyautogui.press('win')
        pyautogui.write('Calculator')
        pyautogui.press('enter')

        # Wait for the Calculator to open
        time.sleep(2)

        # Get the Calculator window
        self.calculator_window = automation.WindowControl(searchDepth=1, Name="Calculator")
    def tearDown(self):
        # Close the Calculator window
        pyautogui.hotkey('alt', 'f4')

    def test_addition(self):
        # Perform addition operation (5 + 3)
        self.perform_calculation('5', '+', '3', '8')

    def test_subtraction(self):
        # Perform subtraction operation (8 - 3)
        self.perform_calculation('8', '-', '3', '5')

    def test_multiplication(self):
        # Perform multiplication operation (2 * 4)
        self.perform_calculation('2', '*', '4', '8')

    def test_division(self):
        # Perform division operation (9 / 3)
        self.perform_calculation('9', '/', '3', '3')

    def perform_calculation(self, operand1, operator, operand2, result):
        # Find and click the calculator buttons
        self.click_calculator_button(operand1)
        self.click_calculator_button(operator)
        self.click_calculator_button(operand2)
        self.click_calculator_button('=')

        # Get the result from the calculator
        result_text = self.get_calculator_result()

        # Assert the result
        self.assertEqual(result_text, result)

    def click_calculator_button(self, button_text):
        button = self.calculator_window.ButtonControl(Name=button_text)
        button.Click()

    def get_calculator_result(self):
        result_control = self.calculator_window.TextControl(ClassName='CalculatorResults')
        return result_control.Name

if __name__ == '__main__':
    unittest.main()
