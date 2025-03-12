'''This module contains the MenuCommand class.'''
import importlib
import logging
import pkgutil
from app.commands import Command
from calculator import Calculator

class PrintCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method prints the history'''
        Calculator.print_history()
        logging.info('Printed calculator local history.')
