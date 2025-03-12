# pylint: disable=line-too-long
'''
This document contains the Calculator class, which is a static class that performs arithmetic operations on two numbers.
'''
from decimal import Decimal
from typing import Callable
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    '''This class is a static class that performs arithmetic operations on two numbers.'''
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        '''This function performs an arithmetic operation on two numbers.'''
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
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
