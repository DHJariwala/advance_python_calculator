'''This is a plugin that calculates the mean of a list of numbers.'''
import logging
from app.commands import Command
from decimal import InvalidOperation, Decimal
from calculator import Calculator

class MeanCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method calculates the mean of a list of numbers.'''
        logging.info('Mean command called')
        try:
            n = input("Enter a list of numbers separated by commas: ").strip()
            logging.info(f"Mean command called with arguments: {n}")
            n_list = n.split(',')
            n_decimal = [Decimal(i) for i in n_list]
            result = Calculator.mean(n_decimal)
            logging.info('Mean calculated.')
            print(f"mean({n}) = {result}")
        except InvalidOperation as e:
            logging.error('Invalid operation: {}'.format(e))
            print('Invalid operation: {}'.format(e))
    