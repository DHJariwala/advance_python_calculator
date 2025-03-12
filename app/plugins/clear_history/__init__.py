'''Clears the local history of the user's calculation data.'''
import logging
from app.commands import Command
from calculator import Calculator

class ClearDataCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method clears the local history of the user's calculation data.'''
        Calculator.clear_history()
        logging.info('Cleared calculator local history.')
