
import logging
from app.commands import Command
from calculator import Calculator


class DeleteCSVCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method deletes the CSV file.'''
        logging.info('Delete CSV command called')
        Calculator.delete_csv()
        logging.info('CSV file deleted.')