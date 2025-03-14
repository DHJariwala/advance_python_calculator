# pylint: disable=comparison-with-callable,unspecified-encoding,broad-exception-raised
'''Tests for the DataHandler class'''
import os
import logging
from decimal import Decimal
import pytest
import pandas as pd

from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from calculator.statistic import CalculationStatistic
from data_handler import DataHandler

TEST_FOLDER_PATH = 'data'
TEST_FILE_NAME = 'calculator_history.csv'

@pytest.fixture(scope="function")
def handler_fixture(monkeypatch):
    """
    Fixture to set up environment variables and create a DataHandler instance.
    Uses delete_csv_file_data() to clear the file on disk as well as the in-memory data.
    """
    monkeypatch.setenv('CALCULATOR_HISTORY_FOLDER_PATH', TEST_FOLDER_PATH)
    monkeypatch.setenv('CALCULATOR_HISTORY_FILE_NAME', TEST_FILE_NAME)
    handler = DataHandler()
    # Clear both in-memory data and the CSV file.
    handler.delete_csv_file_data()
    yield handler
    # Optionally, add cleanup here if needed.

def test_missing_env_vars(monkeypatch):
    """Test that DataHandler.__init__ raises ValueError when environment variables are missing."""
    monkeypatch.setenv('CALCULATOR_HISTORY_FOLDER_PATH', '')
    monkeypatch.setenv('CALCULATOR_HISTORY_FILE_NAME', '')
    with pytest.raises(ValueError):
        _ = DataHandler()

def test_load_empty_csv(handler_fixture):
    """Test that loading an empty CSV returns an empty list and the CSV file is empty."""
    handler = handler_fixture
    handler.delete_csv_file_data()  # This writes an empty CSV file.
    assert handler.get_csv_data() == []
    with pytest.raises(pd.errors.EmptyDataError):
        pd.read_csv(handler.csv_filepath)

def test_add_to_csv(handler_fixture):
    """Test adding a normal calculation to CSV data."""
    handler = handler_fixture
    handler.clear_csv_data()  # Clear only the in-memory data.
    calc = Calculation(5, 3, add)
    handler.add_to_csv(calc)
    data = handler.get_csv_data()
    assert len(data) == 1
    # Since calc.a is not a list, it is stored directly.
    assert data[0] == {'num_1': 5, 'num_2': 3, 'operator': 'add'}

def test_save_and_load_csv(handler_fixture):
    """Test saving data to CSV and reloading it in a new DataHandler instance."""
    handler = handler_fixture
    handler.clear_csv_data()  # Only clear in-memory data.
    calc = Calculation(10, 4, subtract)
    handler.add_to_csv(calc)
    handler.save_csv_data()
    # Create a new instance to simulate re-loading from the file.
    new_handler = DataHandler()
    data = new_handler.get_csv_data()
    assert len(data) == 1
    assert data[0] == {'num_1': 10, 'num_2': 4, 'operator': 'subtract'}

def test_clear_csv_data(handler_fixture):
    """Test that clear_csv_data clears the in-memory data (it does not update the file)."""
    handler = handler_fixture
    calc = Calculation(7, 2, multiply)
    handler.add_to_csv(calc)
    # Clear in-memory data.
    handler.clear_csv_data()
    assert handler.get_csv_data() == []
    # Note: clear_csv_data() does not call save_csv_data(), so the file content remains unchanged.

def test_convert_to_calculation(handler_fixture):
    """Test converting CSV data for a normal calculation to Calculation objects."""
    handler = handler_fixture
    handler.delete_csv_file_data()  # Write an empty CSV file.
    calc = Calculation(8, 2, divide)
    handler.add_to_csv(calc)
    handler.save_csv_data()
    calculations = handler.convert_to_calculation()
    assert len(calculations) == 1
    assert calculations[0].a == 8
    assert calculations[0].b == 2
    assert calculations[0].operation == divide

def test_convert_to_calculation_statistic(handler_fixture):
    """Test converting CSV data for a statistic operation (e.g., 'mean') to a CalculationStatistic object."""
    handler = handler_fixture
    handler.delete_csv_file_data()  # Update the file.
    # Create a fake row for a statistic operation.
    data_list = [Decimal('1.0'), Decimal('2.0'), Decimal('3.0')]
    handler.csv_data.append({
        'num_1': repr(data_list),  # Stored as a string representation of a list.
        'num_2': None,
        'operator': 'mean'
    })
    handler.save_csv_data()
    calculations = handler.convert_to_calculation()
    assert len(calculations) == 1
    # Ensure the object is of the correct type.
    assert isinstance(calculations[0], CalculationStatistic)
    # Check that the evaluated list matches.
    assert calculations[0].a == data_list

def test_invalid_operator_in_conversion(handler_fixture):
    """Test that a row with an invalid operator raises a KeyError during conversion."""
    handler = handler_fixture
    handler.clear_csv_data()
    handler.csv_data = [{'num_1': 5, 'num_2': 3, 'operator': 'invalid_operator'}]
    handler.save_csv_data()
    with pytest.raises(KeyError):
        _ = handler.convert_to_calculation()

def test_delete_csv_data(handler_fixture):
    """Test that delete_csv_file_data clears the in-memory data and writes an empty CSV file."""
    handler = handler_fixture
    calc = Calculation(12, 6, multiply)
    handler.add_to_csv(calc)
    handler.save_csv_data()
    handler.delete_csv_file_data()
    assert handler.get_csv_data() == []
    with pytest.raises(pd.errors.EmptyDataError):
        pd.read_csv(handler.csv_filepath)

def test_load_corrupted_csv(handler_fixture):
    """Test that loading a corrupted CSV returns an empty list."""
    handler = handler_fixture
    # Write corrupted bytes that cannot be decoded in utf-8.
    with open(handler.csv_filepath, 'wb') as f:
        f.write(b'\xff\xff')
    data = handler.load_csv_data()
    assert data == []

def test_saving_to_new_folder(monkeypatch):
    """Test that saving data to a new (non-existent) folder works correctly."""
    new_folder = './new_test_data'
    file_name = 'test_calc_history.csv'
    monkeypatch.setenv('CALCULATOR_HISTORY_FOLDER_PATH', new_folder)
    monkeypatch.setenv('CALCULATOR_HISTORY_FILE_NAME', file_name)
    handler = DataHandler()
    handler.delete_csv_file_data()
    calc = Calculation(20, 10, add)
    handler.add_to_csv(calc)
    handler.save_csv_data()
    assert os.path.exists(handler.csv_filepath)
    # Clean up: remove the file and folder.
    os.remove(handler.csv_filepath)
    os.rmdir(new_folder)

def test_save_csv_data_exception(handler_fixture, monkeypatch, caplog):
    """Test that save_csv_data logs an error when an exception is raised."""
    def dummy_to_csv(*args, **kwargs):
        raise Exception("Simulated save error")
    monkeypatch.setattr(pd.DataFrame, "to_csv", dummy_to_csv)
    with caplog.at_level(logging.ERROR):
        handler_fixture.save_csv_data()
    assert "Error saving data to CSV: Simulated save error" in caplog.text
