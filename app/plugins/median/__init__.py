'''This is a plugin that calculates the median of a list of numbers.'''
import logging
from app.commands import Command
from decimal import InvalidOperation, Decimal
from calculator import Calculator

class MedianCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method calculates the median of a list of numbers.'''
        logging.info('Median command called')
        try:
            n = input("Enter a list of numbers separated by commas: ").strip()
            logging.info(f"Median command called with arguments: {n}")
            n_list = n.split(',')
            n_decimal = [Decimal(i) for i in n_list]
            result = Calculator.median(n_decimal)
            logging.info('Median calculated.')
            print(f"Median({n}) = {result}")
        except InvalidOperation as e:
            logging.error('Invalid operation: {}'.format(e))
            print('Invalid operation: {}'.format(e))
