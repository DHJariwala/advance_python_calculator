# pylint: disable=line-too-long
"""
Tests for the commands in the app/plugins directory.

The following environment is assumed for the REPL:
  - The App.start() method reads commands from input and exits with "Exiting..."
  - Arithmetic commands (add, subtract, multiply, divide) print results or error messages.
  - Statistic commands (mean, median, mode) prompt for a comma‐separated list and then print the result or error.
  - Other plugin commands call corresponding Calculator methods and log messages.
"""

import logging
import os
from decimal import Decimal
import pytest

from calculator import Calculator
from app import App
from app.plugins.print_history import PrintCommand
from app.plugins.save_data import SaveDataCommand
from app.plugins.clear_history import ClearDataCommand
from app.plugins.delete_csv import DeleteCSVCommand
from app.plugins.delete_data import DeleteDataCommand
from app.plugins.load_data import LoadDataCommand
from app.plugins.clear import ClearCommand
from app.plugins.mean import MeanCommand
from app.plugins.median import MedianCommand
from app.plugins.mode import ModeCommand


# --- Tests for the REPL (App) commands ---
def test_app_greet_command(monkeypatch):
    """Test that the REPL handles the 'greet' command and then exits."""
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...", "App did not exit as expected on 'greet' command"


def test_app_menu_command(monkeypatch):
    """Test that the REPL handles the 'menu' command and then exits."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...", "App did not exit as expected on 'menu' command"


def test_app_fly_command(monkeypatch):
    """Test that the REPL handles an unknown command 'fly' and then exits."""
    inputs = iter(['fly', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...", "App did not exit as expected on unknown command"


def test_app_clear_command(monkeypatch):
    """Test that the REPL handles the 'clear' command and then exits."""
    inputs = iter(['clear', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...", "App did not exit as expected on 'clear' command"


def test_app_email_command(monkeypatch):
    """Test that the REPL handles the 'email' command and then exits."""
    inputs = iter(['email', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...", "App did not exit as expected on 'email' command"


# --- Tests for the ClearCommand plugin ---
def test_clear_command(monkeypatch, mocker):
    """Test that ClearCommand.execute() calls os.system with the correct command."""
    mock_system = mocker.patch("os.system")
    cmd = ClearCommand()
    cmd.execute()
    expected_command = 'cls' if os.name == 'nt' else 'clear'
    mock_system.assert_called_once_with(expected_command)


def test_clear_command_exception(mocker, capsys):
    """Test that ClearCommand.execute() handles exceptions gracefully."""
    mocker.patch("os.system", side_effect=Exception("Test Exception"))
    cmd = ClearCommand()
    cmd.execute()
    captured = capsys.readouterr()
    assert "Can't do this command: Test Exception" in captured.out


# --- Tests for arithmetic commands (add, subtract, multiply, divide) ---
def test_add_command(monkeypatch, capsys):
    """Test that AddCommand.execute() correctly adds two numbers."""
    inputs = iter(['add', "10.5", "5.5", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capsys.readouterr()
    assert "10.5 + 5.5 = 16.0" in captured.out


def test_add_command_invalid_input(monkeypatch, capsys):
    """Test that AddCommand.execute() handles invalid input gracefully."""
    inputs = iter(['add', "a", "b", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capsys.readouterr()
    assert "Invalid number input: a or b is not a valid number." in captured.out


def test_subtract_command(monkeypatch, capsys):
    """Test that SubtractCommand.execute() correctly subtracts two numbers."""
    inputs = iter(['subtract', "10.5", "5.5", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capsys.readouterr()
    assert "10.5 - 5.5 = 5.0" in captured.out


def test_subtract_command_invalid_input(monkeypatch, capsys):
    """Test that SubtractCommand.execute() handles invalid input gracefully."""
    inputs = iter(['subtract', "a", "b", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capsys.readouterr()
    assert "Invalid number input: a or b is not a valid number." in captured.out


def test_multiply_command(monkeypatch, capsys):
    """Test that MultiplyCommand.execute() correctly multiplies two numbers."""
    inputs = iter(['multiply', "1", "2", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capsys.readouterr()
    assert "1 x 2 = 2" in captured.out


def test_multiply_command_invalid_input(monkeypatch, capsys):
    """Test that MultiplyCommand.execute() handles invalid input gracefully."""
    inputs = iter(['multiply', "a", "b", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capsys.readouterr()
    assert "Invalid number input: a or b is not a valid number." in captured.out


def test_divide_command(monkeypatch, capsys):
    """Test that DivideCommand.execute() correctly divides two numbers."""
    inputs = iter(['divide', "2", "2", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capsys.readouterr()
    assert "2 / 2 = 1" in captured.out


def test_divide_command_invalid_input(monkeypatch, capsys):
    """Test that DivideCommand.execute() handles invalid input gracefully."""
    inputs = iter(['divide', "a", "b", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capsys.readouterr()
    assert "Invalid number input: a or b is not a valid number." in captured.out


# --- Tests for Calculator-related plugin commands ---
def test_print_command(mocker, caplog):
    """Test that PrintCommand.execute() calls Calculator.print_history() and logs expected message."""
    mock_print_history = mocker.patch.object(Calculator, 'print_history')
    cmd = PrintCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    mock_print_history.assert_called_once()
    assert 'Printed calculator local history.' in caplog.text


def test_save_data_command(mocker, caplog):
    """Test that SaveDataCommand.execute() calls Calculator.save_history_to_csv() and logs expected messages."""
    mock_save_history = mocker.patch.object(Calculator, 'save_history_to_csv')
    cmd = SaveDataCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    mock_save_history.assert_called_once()
    assert 'Save data command called' in caplog.text
    assert 'Data saved to CSV file' in caplog.text


def test_clear_data_command(mocker, caplog):
    """Test that ClearDataCommand.execute() calls Calculator.clear_history() and logs expected message."""
    mock_clear = mocker.patch.object(Calculator, 'clear_history')
    cmd = ClearDataCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    mock_clear.assert_called_once()
    assert 'Cleared calculator local history.' in caplog.text


def test_delete_csv_command(mocker, caplog):
    """Test that DeleteCSVCommand.execute() calls Calculator.delete_csv() and logs expected messages."""
    mock_delete_csv = mocker.patch.object(Calculator, 'delete_csv')
    cmd = DeleteCSVCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    mock_delete_csv.assert_called_once()
    assert 'Delete CSV command called' in caplog.text
    assert 'CSV file deleted.' in caplog.text


def test_delete_data_command_no_deletion(monkeypatch, mocker, caplog):
    """Test that DeleteDataCommand.execute() does not delete data when the user inputs 0."""
    mock_print_all = mocker.patch.object(Calculator, 'print_all_calculations')
    mock_delete_at_index = mocker.patch.object(Calculator, 'delete_at_index')
    monkeypatch.setattr('builtins.input', lambda prompt: "0")
    cmd = DeleteDataCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    mock_print_all.assert_called_once()
    mock_delete_at_index.assert_not_called()
    assert 'Data not deleted' in caplog.text


def test_delete_data_command_deletion(monkeypatch, mocker, caplog):
    """Test that DeleteDataCommand.execute() deletes data when a valid index is provided."""
    mock_print_all = mocker.patch.object(Calculator, 'print_all_calculations')
    mock_delete_at_index = mocker.patch.object(Calculator, 'delete_at_index')
    monkeypatch.setattr('builtins.input', lambda prompt: "2")
    cmd = DeleteDataCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    mock_print_all.assert_called_once()
    mock_delete_at_index.assert_called_once_with(1)
    assert 'Data deleted at location 2' in caplog.text


def test_delete_data_command_invalid_input(monkeypatch, mocker, caplog):
    """Test that DeleteDataCommand.execute() handles invalid input gracefully."""
    mock_delete_at_index = mocker.patch.object(Calculator, 'delete_at_index')
    monkeypatch.setattr('builtins.input', lambda prompt: "invalid")
    cmd = DeleteDataCommand()
    with caplog.at_level(logging.ERROR):
        cmd.execute()
    mock_delete_at_index.assert_not_called()
    assert 'Invalid input. Please enter a valid number.' in caplog.text


def test_load_data_command(mocker, caplog):
    """Test that LoadDataCommand.execute() calls Calculator.load_csv_data() and logs expected messages."""
    mock_load_csv = mocker.patch.object(Calculator, 'load_csv_data')
    cmd = LoadDataCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    mock_load_csv.assert_called_once()
    assert 'Load data command called' in caplog.text
    assert 'Data loaded from CSV file' in caplog.text


# --- Tests for statistic commands ---
def test_mean_command_valid(monkeypatch, capsys, faker):
    """Test that MeanCommand.execute() calculates the mean correctly for valid input."""
    numbers = [faker.random_int(min=1, max=100) for _ in range(5)]
    input_str = ",".join(map(str, numbers))
    def mean_func(decimal_list):
        total = sum(decimal_list, Decimal(0))
        count = Decimal(len(decimal_list))
        return total / count
    monkeypatch.setattr(Calculator, 'mean', mean_func)
    monkeypatch.setattr('builtins.input', lambda prompt: input_str)
    cmd = MeanCommand()
    cmd.execute()
    captured = capsys.readouterr()
    expected_mean = mean_func([Decimal(str(n)) for n in numbers])
    expected_output = f"mean({input_str}) = {expected_mean}"
    assert expected_output in captured.out


def test_mean_command_invalid(monkeypatch, capsys, faker):
    """Test that MeanCommand.execute() handles invalid input gracefully."""
    invalid_input = "a," + ",".join(str(faker.random_int(min=1, max=100)) for _ in range(3))
    monkeypatch.setattr('builtins.input', lambda prompt: invalid_input)
    cmd = MeanCommand()
    cmd.execute()
    captured = capsys.readouterr()
    assert "Invalid operation:" in captured.out


def test_median_command_valid_even(monkeypatch, capsys):
    """
    Test that MedianCommand.execute() calculates the median correctly for an even-length list.
    This test covers the else branch of the local median function.
    """
    # Provide a fixed even-length input.
    input_str = "4,1,3,5"
    def median_func(decimal_list):
        sorted_list = sorted(decimal_list)
        n = len(sorted_list)
        if n % 2 == 1:
            return sorted_list[n // 2]
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    monkeypatch.setattr(Calculator, 'median', median_func)
    monkeypatch.setattr('builtins.input', lambda prompt: input_str)
    cmd = MedianCommand()
    cmd.execute()
    captured = capsys.readouterr()
    # For input "4,1,3,5", sorted: [1,3,4,5] median = (3+4)/2 = 3.5
    expected_result = median_func([Decimal("4"), Decimal("1"), Decimal("3"), Decimal("5")])
    expected_output = f"Median({input_str}) = {expected_result}"
    assert expected_output in captured.out


def test_median_command_valid_odd(monkeypatch, capsys):
    """
    Test that MedianCommand.execute() calculates the median correctly for an odd-length list.
    This test covers the if branch of the local median function.
    """
    # Provide a fixed odd-length input.
    input_str = "3,1,5"
    def median_func(decimal_list):
        sorted_list = sorted(decimal_list)
        n = len(sorted_list)
        if n % 2 == 1:
            return sorted_list[n // 2]
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    monkeypatch.setattr(Calculator, 'median', median_func)
    monkeypatch.setattr('builtins.input', lambda prompt: input_str)
    cmd = MedianCommand()
    cmd.execute()
    captured = capsys.readouterr()
    # For input "3,1,5", sorted: [1,3,5] median = 3
    expected_result = median_func([Decimal("3"), Decimal("1"), Decimal("5")])
    expected_output = f"Median({input_str}) = {expected_result}"
    assert expected_output in captured.out


def test_median_command_invalid(monkeypatch, capsys, faker):
    """Test that MedianCommand.execute() handles invalid input gracefully."""
    invalid_input = "a," + ",".join(str(faker.random_int(min=1, max=100)) for _ in range(3))
    monkeypatch.setattr('builtins.input', lambda prompt: invalid_input)
    cmd = MedianCommand()
    cmd.execute()
    captured = capsys.readouterr()
    assert "Invalid operation:" in captured.out


def test_mode_command_valid(monkeypatch, capsys, faker):
    """
    Test that ModeCommand.execute() calculates the mode correctly for valid input.
    This test forces the while loops in the mode command to execute.
    """
    # Prepare a custom random_int function that returns a fixed sequence.
    sequence = [50, 50, 60, 50, 70]  # Forces both while loops to run.
    def fake_random_int(*args, **kwargs):
        return sequence.pop(0)
    monkeypatch.setattr(faker, "random_int", fake_random_int)
    mode_value = faker.random_int(min=1, max=100)   # returns 50
    other1 = faker.random_int(min=1, max=100)         # returns 50, forcing loop; then returns 60
    while other1 == mode_value:
        other1 = faker.random_int(min=1, max=100)
    other2 = faker.random_int(min=1, max=100)         # returns 50, forcing loop; then returns 70
    while other2 in (mode_value, other1):
        other2 = faker.random_int(min=1, max=100)
    values = [mode_value, mode_value, other1, other2]
    input_str = ",".join(map(str, values))
    monkeypatch.setattr(Calculator, 'mode', lambda decimals: [Decimal(str(mode_value))])
    monkeypatch.setattr('builtins.input', lambda prompt: input_str)
    cmd = ModeCommand()
    cmd.execute()
    captured = capsys.readouterr()
    expected_output = f"mode({input_str}) = ['{str(mode_value)}']"
    assert expected_output in captured.out


def test_mode_command_invalid(monkeypatch, capsys, faker):
    """Test that ModeCommand.execute() handles invalid input gracefully."""
    invalid_input = "a," + ",".join(str(faker.random_int(min=1, max=100)) for _ in range(3))
    monkeypatch.setattr('builtins.input', lambda prompt: invalid_input)
    cmd = ModeCommand()
    cmd.execute()
    captured = capsys.readouterr()
    assert "Invalid operation:" in captured.out
