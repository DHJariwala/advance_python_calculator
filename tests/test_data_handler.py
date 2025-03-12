# pylint: disable=comparison-with-callable,unspecified-encoding
'''Tests for the DataHandler class'''
import os
import pytest
import pandas as pd
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from data_handler import DataHandler

# Use a dedicated test folder and file
TEST_FOLDER_PATH = 'data'
TEST_FILE_NAME = 'calculator_history.csv'

@pytest.fixture(scope="function")
def handler_fixture(monkeypatch):
    """
    Fixture to set up environment variables and create a DataHandler instance.
    Clears CSV data at the start but does not remove the file afterward.
    """
    monkeypatch.setenv('CALCULATOR_HISTORY_FOLDER_PATH', TEST_FOLDER_PATH)
    monkeypatch.setenv('CALCULATOR_HISTORY_FILE_NAME', TEST_FILE_NAME)
    handler = DataHandler()
    # Clear in-memory data and reset file (if any) to ensure isolation.
    handler.csv_data = []
    handler.save_csv_data()
    yield handler
    # Do not delete the file to preserve it as requested.
    # (If needed, cleanup code can be commented or removed.)

def test_load_empty_csv(handler_fixture):
    """Test that loading an empty CSV returns an empty list."""
    handler = handler_fixture
    handler.clear_csv_data()  # ensure file is empty
    assert handler.get_csv_data() == []

def test_add_to_csv(handler_fixture):
    """Test adding a calculation to CSV data."""
    handler = handler_fixture
    handler.clear_csv_data()
    calc = Calculation(5, 3, add)
    handler.add_to_csv(calc)
    data = handler.get_csv_data()
    assert len(data) == 1
    assert data[0] == {'num_1': 5, 'num_2': 3, 'operator': 'add'}

def test_save_and_load_csv(handler_fixture):
    """Test saving data to CSV and loading it in a new instance."""
    handler = handler_fixture
    handler.clear_csv_data()
    calc = Calculation(10, 4, subtract)
    handler.add_to_csv(calc)
    handler.save_csv_data()
    # Create a new instance to simulate re-loading from file
    new_handler = DataHandler()
    data = new_handler.get_csv_data()
    assert len(data) == 1
    assert data[0] == {'num_1': 10, 'num_2': 4, 'operator': 'subtract'}

def test_clear_csv_data(handler_fixture):
    """Test that clearing CSV data empties the in-memory data and the file."""
    handler = handler_fixture
    handler.clear_csv_data()
    # In-memory data should be empty.
    assert handler.get_csv_data() == []
    # Since the original save_csv_data writes an empty DataFrame from an empty list,
    # reading the file should raise EmptyDataError (no headers written).
    with pytest.raises(pd.errors.EmptyDataError):
        pd.read_csv(handler.csv_filepath)

def test_convert_to_calculation(handler_fixture):
    """Test converting CSV data to Calculation objects."""
    handler = handler_fixture
    handler.clear_csv_data()
    calc = Calculation(8, 2, divide)
    handler.add_to_csv(calc)
    handler.save_csv_data()
    calculations = handler.convert_to_calculation()
    assert len(calculations) == 1
    # Check that the attributes match; we cannot call perform_operation
    assert calculations[0].a == 8
    assert calculations[0].b == 2
    assert calculations[0].operation == divide

def test_invalid_operator_in_conversion(handler_fixture):
    """Test that converting a row with an invalid operator raises KeyError."""
    handler = handler_fixture
    handler.clear_csv_data()
    handler.csv_data = [{'num_1': 5, 'num_2': 3, 'operator': 'invalid_operator'}]
    handler.save_csv_data()
    with pytest.raises(KeyError):
        _ = handler.convert_to_calculation()

def test_delete_csv_data(handler_fixture):
    """Test that delete_csv_file_data clears the in-memory data and results in an empty file."""
    handler = handler_fixture
    handler.clear_csv_data()
    calc = Calculation(12, 6, multiply)
    handler.add_to_csv(calc)
    handler.save_csv_data()
    handler.delete_csv_file_data()
    assert handler.get_csv_data() == []
    # Since delete_csv_file_data calls save_csv_data on an empty list,
    # reading the file should raise EmptyDataError.
    with pytest.raises(pd.errors.EmptyDataError):
        pd.read_csv(handler.csv_filepath)

def test_load_corrupted_csv(handler_fixture):
    """Test that loading a corrupted CSV returns an empty list."""
    handler = handler_fixture
    # Write corrupted content to the file directly.
    with open(handler.csv_filepath, 'w') as f:
        f.write("invalid,data\n,missing,fields")
    data = handler.load_csv_data()
    assert data == []

def test_saving_to_new_folder(monkeypatch):
    """Test that saving data to a new (non-existent) folder works correctly."""
    new_folder = './new_test_data'
    file_name = 'test_calc_history.csv'
    monkeypatch.setenv('CALCULATOR_HISTORY_FOLDER_PATH', new_folder)
    monkeypatch.setenv('CALCULATOR_HISTORY_FILE_NAME', file_name)
    handler = DataHandler()
    handler.clear_csv_data()
    calc = Calculation(20, 10, add)
    handler.add_to_csv(calc)
    handler.save_csv_data()
    assert os.path.exists(handler.csv_filepath)
    # Do not delete the file as per request.
