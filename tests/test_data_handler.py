# pylint: disable=comparison-with-callable,unspecified-encoding,broad-exception-raised
'''Tests for the DataHandler class'''
import logging
import os
import pytest
import pandas as pd
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from data_handler import DataHandler

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
    # Clear in-memory data and reset file to ensure isolation.
    handler.csv_data = []
    handler.save_csv_data()
    yield handler
    # Do not delete the file here per your request.

def test_missing_env_vars(monkeypatch):
    """Test that DataHandler.__init__ raises ValueError when environment variables are missing (empty)."""
    monkeypatch.setenv('CALCULATOR_HISTORY_FOLDER_PATH', '')
    monkeypatch.setenv('CALCULATOR_HISTORY_FILE_NAME', '')
    with pytest.raises(ValueError):
        _ = DataHandler()

def test_load_empty_csv(handler_fixture):
    """Test that loading an empty CSV returns an empty list."""
    handler = handler_fixture
    handler.clear_csv_data()  # ensure both in-memory and file are empty
    assert handler.get_csv_data() == []
    # Reading the file should raise an EmptyDataError because no headers are written.
    with pytest.raises(pd.errors.EmptyDataError):
        pd.read_csv(handler.csv_filepath)

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
    # Create a new instance to simulate re-loading from file.
    new_handler = DataHandler()
    data = new_handler.get_csv_data()
    assert len(data) == 1
    assert data[0] == {'num_1': 10, 'num_2': 4, 'operator': 'subtract'}

def test_clear_csv_data(handler_fixture):
    """Test that clearing CSV data empties the in-memory data and results in an empty file."""
    handler = handler_fixture
    handler.clear_csv_data()
    # In-memory data should be empty.
    assert handler.get_csv_data() == []
    # Since clear_csv_data() does not write an empty DataFrame (and thus no headers), reading the file should raise EmptyDataError.
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
    # Check that the attributes match.
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
    # Reading the file should raise EmptyDataError.
    with pytest.raises(pd.errors.EmptyDataError):
        pd.read_csv(handler.csv_filepath)

def test_load_corrupted_csv(handler_fixture):
    """Test that loading a corrupted CSV returns an empty list."""
    handler = handler_fixture
    # Write corrupted content directly to the file.
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
    # Clean up: Remove the created file and folder.
    os.remove(handler.csv_filepath)
    os.rmdir(new_folder)
def test_save_csv_data_exception(handler_fixture, monkeypatch, caplog):
    """Test that save_csv_data logs an error when an exception is raised."""
    # Patch DataFrame.to_csv to simulate an exception.
    def dummy_to_csv(*args, **kwargs):
        raise Exception("Simulated save error")
    monkeypatch.setattr(pd.DataFrame, "to_csv", dummy_to_csv)
    with caplog.at_level(logging.ERROR):
        handler_fixture.save_csv_data()
    assert "Error saving data to CSV: Simulated save error" in caplog.text
