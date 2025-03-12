# pylint: disable=line-too-long
'''This document contains the Calculations class, which represents a collection of Calculation objects.'''
from typing import List
from calculator.calculation import Calculation

class Calculations:
    '''This class represents a collection of Calculation objects.'''
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
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
