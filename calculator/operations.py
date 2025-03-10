'''This file contains all the calculator operations'''
from decimal import Decimal

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
    '''Divide two numbers'''
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
