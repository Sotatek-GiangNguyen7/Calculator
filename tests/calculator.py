import pyautogui
import uiautomation as automation

class Calculator(): 
    def perform_calculation(self, operand1, operator, operand2, result):
        # Get the Calculator window
        self.calculator_window = automation.WindowControl(searchDepth=1, Name="Calculator")
        pyautogui.press(str(operand1))
        pyautogui.press(operator)
        pyautogui.press(str(operand2))
        pyautogui.press("=")  


    def get_calculator_result(self):
        result_control = self.calculator_window.PaneControl(automation ='TextContainer')
        return result_control.Name