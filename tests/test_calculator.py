'''Tests for the Calculator class.'''
from decimal import Decimal
import pytest

from calculator import Calculator
from calculator.calculations import Calculations
from calculator.statistic import CalculationStatistic

# --- Arithmetic operation tests ---

def test_addition():
    """Test that addition works correctly."""
    result = Calculator.add(Decimal(2), Decimal(2))
    assert result == Decimal(4)

def test_subtraction():
    """Test that subtraction works correctly."""
    result = Calculator.subtract(Decimal(2), Decimal(2))
    assert result == Decimal(0)

def test_multiply():
    """Test that multiplication works correctly."""
    result = Calculator.multiply(Decimal(2), Decimal(2))
    assert result == Decimal(4)

def test_divide():
    """Test that division works correctly."""
    result = Calculator.divide(Decimal(2), Decimal(2))
    assert result == Decimal(1)

# --- Statistic operation tests ---

@pytest.fixture
def dummy_statistic():
    """A dummy calculation statistic object with a perform() method."""
    class DummyStatistic:
        '''A dummy statistic object.'''
        def perform(self):
            '''A dummy perform method.'''
            return Decimal(10)
    return DummyStatistic()

def test_mean_statistic(mocker, dummy_statistic):
    """
    Test that Calculator.mean calls _perform_statistic_operation and returns the expected value.
    """
    # Patch CalculationStatistic.create to return our dummy object.
    patch = mocker.patch.object(CalculationStatistic, "create", return_value=dummy_statistic)
    result = Calculator.mean([Decimal("1"), Decimal("2"), Decimal("3")])
    assert result == Decimal(10)
    patch.assert_called_once()
    # Additionally, you can check that the first argument of create is the list and the second is the mean function.
    args, _ = patch.call_args
    assert args[0] == [Decimal("1"), Decimal("2"), Decimal("3")]
    # args[1] is the mean function imported in Calculator; no need to call it here.

def test_median_statistic(mocker, dummy_statistic):
    """
    Test that Calculator.median calls _perform_statistic_operation and returns the expected value.
    """
    patch = mocker.patch.object(CalculationStatistic, "create", return_value=dummy_statistic)
    result = Calculator.median([Decimal("4"), Decimal("5"), Decimal("6")])
    assert result == Decimal(10)
    patch.assert_called_once()
    args, _ = patch.call_args
    assert args[0] == [Decimal("4"), Decimal("5"), Decimal("6")]

def test_mode_statistic(mocker, dummy_statistic):
    """
    Test that Calculator.mode calls _perform_statistic_operation and returns the expected value.
    """
    patch = mocker.patch.object(CalculationStatistic, "create", return_value=dummy_statistic)
    result = Calculator.mode([Decimal("7"), Decimal("7"), Decimal("8")])
    assert result == Decimal(10)
    patch.assert_called_once()
    args, _ = patch.call_args
    assert args[0] == [Decimal("7"), Decimal("7"), Decimal("8")]

# --- History and file operations tests ---

def test_print_history(monkeypatch, capsys):
    """Test that print_history prints calculation history correctly."""
    # Create a dummy calculation with predictable output.
    class DummyCalculation:
        '''A dummy calculation object.'''
        def __str__(self):
            return "dummy_calc"
        def perform(self):
            '''A dummy perform method.'''
            return Decimal(42)
    # Patch Calculations.get_history to return two dummy calculations.
    monkeypatch.setattr(Calculations, "get_history", lambda: [DummyCalculation(), DummyCalculation()])
    # Capture printed output.
    Calculator.print_history()
    captured = capsys.readouterr().out
    # Check that both lines (indexed 1 and 2) appear with expected text.
    assert "1. dummy_calc = 42" in captured
    assert "2. dummy_calc = 42" in captured

def test_clear_history(mocker):
    """Test that clear_history calls the underlying clear_history method on Calculations."""
    mock_clear = mocker.patch.object(Calculations, "clear_history")
    Calculator.clear_history()
    mock_clear.assert_called_once()

def test_save_history_to_csv(mocker):
    """Test that save_history_to_csv calls the underlying add_calculations_data_to_csv method on Calculations."""
    mock_save = mocker.patch.object(Calculations, "add_calculations_data_to_csv")
    Calculator.save_history_to_csv()
    mock_save.assert_called_once()

def test_print_all_calculations(mocker):
    """Test that print_all_calculations calls the underlying print_all_calculations method on Calculations."""
    mock_print_all = mocker.patch.object(Calculations, "print_all_calculations")
    Calculator.print_all_calculations()
    mock_print_all.assert_called_once()

def test_delete_at_index(mocker):
    """Test that delete_at_index calls the underlying delete_at_index method on Calculations with the correct index."""
    mock_delete = mocker.patch.object(Calculations, "delete_at_index")
    Calculator.delete_at_index(3)
    mock_delete.assert_called_once_with(3)

def test_load_csv_data(mocker):
    """Test that load_csv_data calls the underlying add_csv_data method on Calculations."""
    mock_load = mocker.patch.object(Calculations, "add_csv_data")
    Calculator.load_csv_data()
    mock_load.assert_called_once()

def test_delete_csv(mocker):
    """Test that delete_csv calls the underlying delete_csv method on Calculations."""
    mock_delete = mocker.patch.object(Calculations, "delete_csv")
    Calculator.delete_csv()
    mock_delete.assert_called_once()
