'''Tests for the Calculator class.'''
from decimal import Decimal

from calculator import Calculator
from calculator.calculations import Calculations

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

# --- Other Calculator methods ---

def test_print_history(monkeypatch, capsys):
    """Test that print_history prints calculation history correctly."""
    # Create a dummy calculation with predictable output.
    class DummyCalculation:
        '''Dummy calculation class'''
        def __str__(self):
            return "dummy_calc"
        def perform(self):
            '''Dummy perform method'''
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
