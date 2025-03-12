import logging
from app.commands import Command
from calculator import Calculator

class DeleteDataCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method deletes the local history of the user's calculation data.'''
        logging.info('Delete data command called')
        Calculator.print_all_calculations()
        delete_index = int(input('Enter the index of the calculation to delete (0 to exit): ')) - 1
        if delete_index == -1:
            logging.info('Data not deleted')
            return
        Calculator.delete_at_index(delete_index)
        logging.info(f'Data deleted at location {delete_index+1}')