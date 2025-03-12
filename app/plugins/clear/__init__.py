# pylint: disable=broad-exception-caught
'''This is the clear plugin. It will clear the screen.'''
import os
from app.commands import Command

class ClearCommand(Command):
    '''This is the clear command. It will clear the screen.'''
    def execute(self):
        '''This method will clear the terminal screen.'''
        print('Hello from the clear command!')
        try:
            print('cls' if os.name == 'nt' else 'clear')
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            print(f"Can't do this command: {e}")
