'''This module contains the basic arithmetic operations of a calculator'''
from decimal import Decimal
# Defining Functions with type hints
def add(a: Decimal, b: Decimal) -> Decimal:
    '''Add two numbers'''
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    '''Subtract two numbers'''
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    '''Multiply two numbers'''
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    '''Divide two numbers. But raise an error if b is zero'''
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def mean(a: list[Decimal]) -> Decimal:
    '''Calculate the mean of a list of numbers'''
    if len(a) == 0:
        raise ValueError("Cannot calculate the mean of an empty list")
    return sum(a) / len(a)
def median(a: list[Decimal]) -> Decimal:
    '''Calculate the median of a list of numbers'''
    if len(a) == 0:
        raise ValueError("Cannot calculate the median of an empty list")
    sorted_a = sorted(a)
    n = len(sorted_a)
    if n % 2 == 0:
        return (sorted_a[n//2 - 1] + sorted_a[n//2]) / 2
    return sorted_a[n//2]