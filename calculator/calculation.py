# pylint: disable=line-too-long
'''This document contains the Calculation class, which represents an arithmetic operation on two numbers.'''
from decimal import Decimal
from typing import Callable

class Calculation:
    '''This class represents an arithmetic operation on two numbers.'''
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        '''This function initializes the Calculation class.'''
        self.a = a
        self.b = b
        self.operation = operation
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        '''This function creates a Calculation object.'''
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        '''This function performs the arithmetic operation.'''
        return self.operation(self.a, self.b)
    def __repr__(self):
        '''This function returns a string representation of the Calculation object.'''
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
