import pyautogui
import uiautomation as automation

class Calculator(): 
    def get_windows(self):
        self.calculator_window = automation.WindowControl(searchDepth=1, Name="Calculator")

    def perform_calculation(self, operand1, operator, operand2, result):
        pyautogui.press(str(operand1))
        pyautogui.press(operator)
        pyautogui.press(str(operand2))
        pyautogui.press("=")  

    def click_to_navigate(self):
        self.calculator_window.ButtonControl(Name ="Open Navigation").Click()
    def click_to_mode(self, mode):
        self.calculator_window.ListItemControl(Name = mode).Click()

    def get_calculator_result(self):
        result_control = self.calculator_window.PaneControl(automation ='TextContainer')
        return result_control.Name
    
    def enter_number(self, number):
        for char in str(number):
            pyautogui.press(char)


    def get_calculator_hex_result(self, number):
        result_control = self.calculator_window.PaneControl(automation ='TextContainer')
        return result_control.Name