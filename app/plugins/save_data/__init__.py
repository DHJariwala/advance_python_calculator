import logging
from app.commands import Command
from calculator import Calculator

class SaveDataCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method saves the local history of the user's calculation data.'''
        logging.info('Save data command called')
        Calculator.save_data_to_csv()        
