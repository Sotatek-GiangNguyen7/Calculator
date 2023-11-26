import pyautogui
import uiautomation as automation


class Calculator(): 
    def get_windows(self):
        self.calculator_window = automation.WindowControl(searchDepth=2, Name="Calculator")
    def perform_calculation(self, operand1, operator, operand2):
        self.enter_first_number(operand1)
        self.enter_operator(operator)
        self.enter_second_number(operand2)
        self.get_result()

    def enter_first_number(self, operand1):
        for char in str(operand1):
            pyautogui.press(str(char))
            
    def enter_operator(self, operator):
        pyautogui.press(operator)
        
    def enter_second_number(self, operand2):
        for char in str(operand2):
            pyautogui.press(str(char))
            
    def get_result(self):
        pyautogui.press("=")

    def click_to_navigate(self):
        self.calculator_window.ButtonControl(Name ="Open Navigation").Click()
    def click_to_mode(self, mode):
        self.calculator_window.ListItemControl(Name = mode).Click()
    def click_to_display_values(self,display_values):
        self.calculator_window.TextControl(Name = display_values).Click()

    def get_calculator_result(self):
        result_control = self.calculator_window.PaneControl(automation ='TextContainer')
        return result_control.Name
    
    def enter_number(self, number):
        for char in str(number):
            pyautogui.press(char)
    def binary_format(self, num):
        binary_string = bin(num)[2:]
        remainder = len(binary_string) % 4
        if remainder == 1:
            num_str = '000' + str(binary_string)
        elif remainder == 2:
            num_str = '00' + str(binary_string)
        elif remainder == 3:
            num_str = '0' + str(binary_string)
        else:
            num_str = str(binary_string)

        return num_str
    def add_space(self,number_str):
        reversed_number = number_str[::-1]  
        result = " ".join(reversed_number[i:i+3] for i in range(0, len(reversed_number), 3))
        return result[::-1]  
