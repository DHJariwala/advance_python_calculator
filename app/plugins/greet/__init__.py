'''This is a plugin that greets the user.'''
import logging
from app.commands import Command

class GreetCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method greets the user.'''
        logging.info('Greet command called')
        print("Hello World!")
