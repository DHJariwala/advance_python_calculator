'''This file contains calculation class, which only deals with one calculation at a time'''
from decimal import Decimal
from typing import Callable

class Calculation:
    '''Calculation class represents a single calculation'''
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> None:
        self.a = a
        self.b = b
        self.operation = operation
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> 'Calculation':
        '''Factory method for calculation class'''
        return Calculation(a, b, operation)
    def perform(self) -> Decimal:
        '''Perform the calculation'''
        return self.operation(self.a, self.b)
    def __repr__(self) -> str:
        '''Representation of the class'''
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
