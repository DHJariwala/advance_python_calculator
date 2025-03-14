'''This is a plugin that calculates the mean of a list of numbers.'''
import logging
from app.commands import Command
from decimal import InvalidOperation, Decimal
from calculator import Calculator

class ModeCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method calculates the mode of a list of numbers.'''
        logging.info('Mode command called')
        try:
            n = input("Enter a list of numbers separated by commas: ").strip()
            logging.info(f"Mode command called with arguments: {n}")
            n_list = n.split(',')
            n_decimal = [Decimal(i) for i in n_list]
            result = Calculator.mode(n_decimal)
            logging.info('Mode calculated.')
            print(f"mode({n}) = {[str(x) for x in result]}")
        except InvalidOperation as e:
            logging.error('Invalid operation: {}'.format(e))
            print('Invalid operation: {}'.format(e))
    