# pylint: disable=line-too-long
'''This document contains the Calculations class, which represents a collection of Calculation objects.'''
from typing import List
from calculator.calculation import Calculation
from calculator.statistic import CalculationStatistic
from data_handler import DataHandler

class Calculations:
    '''This class represents a collection of Calculation objects.'''
    history: List[Calculation] = []
    data_handler = DataHandler()

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        '''This function adds a Calculation object to the collection.'''
        cls.history.append(calculation)
    
    @classmethod
    def add_statistic_calculation(cls, calculation: CalculationStatistic) -> None:
        '''This function adds a Calculation object to the collection.'''
        cls.history.append(calculation)

    @classmethod
    def clear_history(cls) -> None:
        '''This function clears the collection of Calculation objects.'''
        cls.history.clear()

    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''This function returns the collection of Calculation objects.'''
        return cls.history

    @classmethod
    def get_latest(cls) -> Calculation:
        '''This function returns the most recent Calculation object.'''
        return None if not cls.history else cls.history[-1]

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        '''This function returns a list of Calculation objects that match the specified operation.'''
        return [calculation for calculation in cls.history if calculation.operation.__name__ == operation_name]
    @classmethod
    def clear_csv_data(cls):
        '''This function clears the CSV data.'''
        cls.data_handler.clear_csv_data()
    @classmethod
    def add_csv_data(cls):
        cls.history += cls.data_handler.convert_to_calculation()
        cls.data_handler.clear_csv_data()
    @classmethod
    def add_calculations_data_to_csv(cls):
        for calc in cls.history:
            cls.data_handler.add_to_csv(calc)
        cls.data_handler.save_csv_data()
        cls.clear_history()
    @classmethod
    def print_all_calculations(cls):
        # print(cls.history)
        for index, calc in enumerate(cls.history):
            print(f'{index+1}. {calc} = {calc.perform()}')
    @classmethod
    def delete_at_index(cls, index):
        try:
            cls.history.pop(index)
        except IndexError:
            print(f'Delete from improrper index : {index}')
    @classmethod
    def delete_csv(cls):
        cls.data_handler.delete_csv_file_data()
