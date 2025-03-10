'''This file has all the calculations. This has the calculations history.'''
from typing import List
from calculator.calculation import Calculation

class Calculations:
    '''This class represents a collection of Calculation objects.'''
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        '''This function adds a Calculation object to history.'''
        cls.history.append(calculation)
    @classmethod
    def clear_history(cls) -> None:
        '''This function clears the history of calculations.'''
        cls.history.clear()
    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''This function returns the history of calculations.'''
        return cls.history
    @classmethod
    def get_latest(cls) -> Calculation:
        '''This function returns the latest calculation.'''
        return None if not cls.history else cls.history[-1]
    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        '''This function finds all calculations by operation name.'''
        return [calculation for calculation in cls.history if calculation.operation.__name__ == operation_name]
