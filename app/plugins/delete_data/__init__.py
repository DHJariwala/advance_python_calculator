import logging
from app.commands import Command

class DeleteDataCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method deletes the local history of the user's calculation data.'''
        logging.info('Delete data command called')
        with open('data.txt', 'w') as file:
            file.write('')
        print('Data deleted.')
        logging.info('Data deleted.')
