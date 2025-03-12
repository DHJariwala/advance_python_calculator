'''Clears the local history of the user's calculation data.'''
import logging
from app.commands import Command

class ClearDataCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method clears the local history of the user's calculation data.'''
        logging.info('Clear data command called')
        with open('data.txt', 'w') as file:
            file.write('')
        print('Data cleared.')
        logging.info('Data cleared.')
