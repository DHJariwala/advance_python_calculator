# pylint: disable=line-too-long, comparison-with-callable
'''This document contains the Calculation class, which represents an arithmetic operation on two numbers.'''
# import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    '''Generate test data'''
    # Define operation mappings for both Calculator and Calculation tests
    operations_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operations_mappings.keys()))
        operation_func = operations_mappings[operation_name]
        if operation_func == divide:
            b = Decimal('1') if b == Decimal('0') else b
        expected = operation_func(a, b)
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    '''Add option to generate test data'''
    parser.addoption(
        "--num_records",
        action="store",
        default=5,
        type=int,
        help="Number of test records to generate"
    )

def pytest_generate_tests(metafunc):
    '''Generate test data'''
    if {'a','b','expected'}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption('--num_records')
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(a,b,op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a,b,op_name,op_func,expected in parameters]
        metafunc.parametrize('a,b,operation,expected', modified_parameters)
