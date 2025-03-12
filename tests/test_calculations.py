'''Tests for calculations class'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

# ----- Existing tests for history management -----

@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    latest = Calculations.get_latest()
    # Latest should be the second added: (20,3) with subtract.
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    """Test finding calculations in the history by operation type."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"

# ----- Additional tests for CSV and data-related methods -----

def test_clear_csv_data(mocker):
    """Test that clear_csv_data calls the DataHandler's clear_csv_data method."""
    mock_clear = mocker.patch.object(Calculations.data_handler, "clear_csv_data")
    Calculations.clear_csv_data()
    mock_clear.assert_called_once()

def test_add_csv_data(mocker):
    """Test that add_csv_data appends calculations from data_handler.convert_to_calculation and clears CSV data."""
    Calculations.clear_history()
    # Create a dummy calculation.
    dummy_calc = Calculation(Decimal('3'), Decimal('1'), add)
    mock_convert = mocker.patch.object(Calculations.data_handler, "convert_to_calculation", return_value=[dummy_calc])
    mock_clear = mocker.patch.object(Calculations.data_handler, "clear_csv_data")
    Calculations.add_csv_data()
    # Check that the dummy calculation is appended.
    assert dummy_calc in Calculations.get_history()
    mock_convert.assert_called_once()
    mock_clear.assert_called_once()

def test_add_calculations_data_to_csv(mocker):
    """
    Test that add_calculations_data_to_csv calls data_handler.add_to_csv for each calculation,
    then calls save_csv_data and finally clears the history.
    """
    Calculations.clear_history()
    calc1 = Calculation(Decimal('4'), Decimal('2'), add)
    calc2 = Calculation(Decimal('7'), Decimal('3'), subtract)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    mock_add_to_csv = mocker.patch.object(Calculations.data_handler, "add_to_csv")
    mock_save_csv = mocker.patch.object(Calculations.data_handler, "save_csv_data")
    Calculations.add_calculations_data_to_csv()
    assert mock_add_to_csv.call_count == 2, "Expected add_to_csv to be called for each calculation"
    mock_save_csv.assert_called_once()
    assert len(Calculations.get_history()) == 0, "History should be cleared after saving"

def test_print_all_calculations(monkeypatch, capsys):
    """
    Test that print_all_calculations prints each calculation in the history.
    We monkeypatch the perform() method of Calculation instances for predictability.
    """
    # Dummy perform method that returns Decimal(100)
    def dummy_perform(self):
        return Decimal(100)
    # Create two dummy calculations.
    calc1 = Calculation(Decimal('1'), Decimal('1'), add)
    calc2 = Calculation(Decimal('2'), Decimal('2'), subtract)
    # Bind the dummy perform method to each instance.
    calc1.perform = dummy_perform.__get__(calc1, type(calc1))
    calc2.perform = dummy_perform.__get__(calc2, type(calc2))
    # Clear the current history and add the dummy calculations.
    Calculations.clear_history()
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    # Capture printed output.
    Calculations.print_all_calculations()
    captured = capsys.readouterr().out
    # Expect two lines: one for each calculation.
    assert "1. " in captured
    assert "2. " in captured
    # Check that each line shows '100' as the result.
    assert "100" in captured

def test_delete_at_index_valid():
    """Test that delete_at_index removes the correct calculation."""
    Calculations.clear_history()
    calc1 = Calculation(Decimal('1'), Decimal('1'), add)
    calc2 = Calculation(Decimal('2'), Decimal('2'), subtract)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    Calculations.delete_at_index(0)
    history = Calculations.get_history()
    assert len(history) == 1, "Expected one calculation remaining"
    assert history[0] == calc2, "Remaining calculation should be the second one"

def test_delete_at_index_invalid(monkeypatch, capsys):
    """Test that delete_at_index prints an error message when given an invalid index."""
    Calculations.clear_history()
    calc = Calculation(Decimal('1'), Decimal('1'), add)
    Calculations.add_calculation(calc)
    # Capture output from the print call in delete_at_index
    Calculations.delete_at_index(5)
    captured = capsys.readouterr().out
    assert "Delete from improrper index : 5" in captured
    # History should remain unchanged.
    history = Calculations.get_history()
    assert len(history) == 1

def test_delete_csv(mocker):
    """Test that delete_csv calls data_handler.delete_csv_file_data."""
    mock_delete = mocker.patch.object(Calculations.data_handler, "delete_csv_file_data")
    Calculations.delete_csv()
    mock_delete.assert_called_once()
