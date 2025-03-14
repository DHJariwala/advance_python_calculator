# pylint: disable=line-too-long
'''
This document contains the Calculator class, which is a static class that performs arithmetic operations on two numbers.
'''
from decimal import Decimal
from typing import Callable
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, mode, subtract, multiply, divide, mean, median
from calculator.statistic import CalculationStatistic

class Calculator:
    '''This class is a static class that performs arithmetic operations on two numbers.'''
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        '''This function performs an arithmetic operation on two numbers.'''
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        Calculations
        return calculation.perform()
    @staticmethod
    def _perform_statistic_operation(a: list[Decimal], operation: Callable[[list[Decimal]], Decimal]) -> Decimal:
        '''This function performs a statistic operation on a list of numbers.'''
        calculation = CalculationStatistic.create(a, operation)
        Calculations.add_statistic_calculation(calculation)
        return calculation.perform()
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        '''This function adds two numbers.'''
        return Calculator._perform_operation(a, b, add)
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        '''This function subtracts two numbers.'''
        return Calculator._perform_operation(a, b, subtract)
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        '''This function multiplies two numbers.'''
        return Calculator._perform_operation(a, b, multiply)
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        '''This function divides two numbers.'''
        return Calculator._perform_operation(a, b, divide)
    @staticmethod
    def mean(a: list[Decimal]) -> Decimal:
        '''This function calculates the mean of a list of numbers.'''
        return Calculator._perform_statistic_operation(a, mean)
    @staticmethod
    def median(a: list[Decimal]) -> Decimal:
        '''This function calculates the median of a list of numbers.'''
        return Calculator._perform_statistic_operation(a, median)
    @staticmethod
    def mode(a: list[Decimal]) -> Decimal:
        '''This function calculates the mode of a list of numbers.'''
        return Calculator._perform_statistic_operation(a, mode)
    @staticmethod
    def print_history():
        '''This function prints the history of calculations.'''
        for index, calculation in enumerate(Calculations.get_history()):
            print(f'{index+1}. {calculation} = {calculation.perform()}')
    @staticmethod
    def clear_history():
        '''This function clears the history of calculations.'''
        Calculations.clear_history()
    @staticmethod
    def save_history_to_csv():
        '''This function saves the history of calculations to a CSV file.'''
        Calculations.add_calculations_data_to_csv()
    @staticmethod
    def print_all_calculations():
        Calculations.print_all_calculations()
    @staticmethod
    def delete_at_index(index):
        Calculations.delete_at_index(index)
    @staticmethod
    def load_csv_data():
        Calculations.add_csv_data()
    @staticmethod
    def delete_csv():
        Calculations.delete_csv()
        
