'''This is a plugin that exits the program when called.'''
import logging
from app.commands import Command
from decimal import Decimal, InvalidOperation
from calculator import Calculator

class MultiplyCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method exits the program when called'''
        logging.info('Multiply command called')
        try:
            a = input("Enter first number: ").strip()
            b = input("Enter second number: ").strip()
            logging.info(f"Multiply command called with arguments: {a}, {b}")
            a_decimal, b_decimal = map(Decimal, [a, b])
            result = Calculator.multiply(a_decimal, b_decimal)
            print(f"{a} x {b} = {result}")
        except InvalidOperation:
            print(f"Invalid number input: {a} or {b} is not a valid number.")
