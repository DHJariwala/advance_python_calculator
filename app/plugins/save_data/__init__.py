import logging
from app.commands import Command

class SaveDataCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method saves the local history of the user's calculation data.'''
        logging.info('Save data command called')
        with open('data.txt', 'w') as file:
            file.write('')
        print('Data saved.')
        logging.info('Data saved.')
