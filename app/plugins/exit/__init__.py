'''This is a plugin that exits the program when called.'''
import logging
import sys
from app.commands import Command

class ExitCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method exits the program when called'''
        logging.info('Exit command called')
        sys.exit("Exiting...")
