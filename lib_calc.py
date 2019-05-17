"""lib_calc.py: Robot Framework Library for Calculator"""


import time
from logging import debug, error, info, warn
import atomacos
from var_calc import *


class OPERATOR:
    """
    Define basic operators.
    """
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'


class lib_calc:
    """
    A helper library for calc robot.
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        info('Initialzed the lib_calc.')

    def get_result(self):
        """
        Get the result in the display of the calculator.

        :return: str, the number of result
        """
        debug('Getting display result.')
        result = self.main_display.AXValue
        info('Succeeded to get display result: {}.'.format(result))
        return result

    def start_calc(self):
        """
        Start the calculator app by bundle id.

        :return: None
        """
        debug('Starting calculator.app.')
        atomacos.launchAppByBundleId(CALC_BUNDLE_ID)
        time.sleep(1)
        info('Succeeded to start calculator.app.')
        self.get_ui_elements()

    def get_ui_elements(self):
        """
        Get the some interesting UI element references, and save them to the instance variables.

        :return: None
        """
        debug('Getting the UI element references.')
        calculator = atomacos.getAppRefByBundleId('com.apple.calculator')
        calc_window = calculator.AXMainWindow
        ns_box = calc_window.AXChildren[0]
    
        self.calc_box = calc_window.AXChildren[1]
        self.main_display = ns_box.AXChildren[0]
        
        self.button_clear = self.get_button(LABEL_CLEAR)
        self.button_add = self.get_button(LABEL_ADD)
        self.button_substract = self.get_button(LABEL_SUBSTRACT)
        self.button_multiply = self.get_button(LABEL_MULTIPLY)
        self.button_divide = self.get_button(LABEL_DIVIDE)
        self.button_equals = self.get_button(LABEL_EQUALS)
        self.button_negate = self.get_button(LABEL_NEGATE)
        info('Succeeded to get the UI element references.')

    def stop_calc(self):
        """
        Stop the calculator app by bundle id.

        :return: None
        """
        debug('Stopping calculator.app.')
        atomacos.terminateAppByBundleId(CALC_BUNDLE_ID)
        info('Succeeded to stop calculator.app.')

    def get_button(self,button_name):
        """
        Get the button reference by button label name.

        :param button_name: str, label of the button
        :return: obj, button reference
        """
        debug('Getting button reference for button {}.'.format(button_name))
        button = self.calc_box.findFirst(AXRole='AXButton', AXDescription=button_name)
        info('Succeeded to get button reference for button {}.'.format(button_name))
        return button

    def press_button(self, button):
        """
        Perform button press.

        :param button: obj, button reference
        :return: None
        """
        button_name = button.AXDescription
        debug('Performing the {} button press.'.format(button_name))
        button.Press()
        info('Succeeded to performing the {} button press.'.format(button_name))

    def clear_all(self):
        """
        Perform clear button press to clear the result.

        :return: None
        """
        debug('Clear all.')
        self.press_button(self.button_clear)
        info('Succeeded to clear all.')

    def get_number_button(self, number):
        """
        Get button reference of a number.

        :param number: int, number 0-9
        :return: obj, button reference
        """
        return self.get_button(NUMBERS[number])

    def press_number_button(self, number):
        """
        Perform a number button press.

        :param number: int, number 0-9
        :return: None
        """
        self.press_button(self.get_number_button(number))

    def check_result(self, expected_number):
        """
        Checks the current display result with the expected number.

        :return: None
        """
        debug('Checking the result with expected number {}.'.format(expected_number))
        result = self.get_result()
        assert result == str(expected_number), \
        'Failed, expected result {}, result {}.'.format(expected_number, result)
        info('Succeeded to check the result with expected number {}.'.format(expected_number))

    def check_number(self, number):
        """
        Check number button press functionality by comparing with the display result.

        :param number: int, number 0-9
        :return: None
        """
        debug('Checking number button {} press.'.format(number))
        button = self.get_number_button(number)
        self.press_button(button)
        self.check_result(number)
        info('Succeeded to check number button {} press.'.format(number))

    def input_digits(self, number):
        """
        Input a integer number by performing number button presses for the digits.

        :param number: int, number 0-9
        :return: None
        """
        for digit in str(abs(number)):
            self.press_number_button(int(digit))

    def check_binary_calc(self, a, operator, b, expected_result):
        """
        Checks binary calculation by comparing the expected result with the display result.

        :param a: str, number 0-9
        :param operator: str,  basic operators containing +, -, *, /
        :param b: str, number 0-9
        :param expected_result: str, number 0-9
        :return: None
        """
        debug('Checking calculation: {} {} {} = {}.'.format(a, operator, b, expected_result))
        a = int(a)
        b = int(b)
        self.input_digits(a)
        if a < 0:
            self.press_button(self.button_negate)
    
        if operator == OPERATOR.ADD:
            self.press_button(self.button_add)
        elif operator == OPERATOR.SUB:
            self.press_button(self.button_substract)
        elif operator == OPERATOR.MUL:
            self.press_button(self.button_multiply)
        elif operator == OPERATOR.DIV:
            self.press_button(self.button_divide)
        else:
            raise Exception('Not supported operator.')

        self.input_digits(b)
        if b < 0:
            self.press_button(self.button_negate)

        self.press_button(self.button_equals)
        self.check_result(expected_result)
        info('Succeeded to check calculation: {} {} {} = {}.'.format(a, operator, b, expected_result))


if __name__ == "__main__":
    # Basic test
    calc = lib_calc()
    calc.start_calc()

    calc.check_binary_calc(1, '+', 1, 2)

    calc.stop_calc()