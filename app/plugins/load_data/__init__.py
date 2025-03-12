import logging
from app.commands import Command
from calculator import Calculator

class LoadDataCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method deletes the local history of the user's calculation data.'''
        logging.info('Load data command called')
        Calculator.load_csv_data()
        logging.info('Data loaded from CSV file')
