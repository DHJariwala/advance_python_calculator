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
