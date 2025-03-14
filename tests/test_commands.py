'''This file contains the tests for the commands in the app/plugins directory'''
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

def test_app_greet_command(monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_fly_command(monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['fly', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_clear_command(monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['clear', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_email_command(monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['email', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"



def test_clear_command(mocker):
    """Test that ClearCommand.execute() calls os.system correctly"""
    # Mock os.system to prevent actually clearing the screen
    mock_system = mocker.patch("os.system")

    cmd = ClearCommand()
    cmd.execute()

    # Assert that os.system was called with the correct argument
    expected_command = 'cls' if os.name == 'nt' else 'clear'
    mock_system.assert_called_once_with(expected_command)

def test_clear_command_exception(mocker, capsys):
    """Test that ClearCommand.execute() handles exceptions gracefully"""

    # Mock os.system to raise an exception
    mocker.patch("os.system", side_effect=Exception("Test Exception"))

    cmd = ClearCommand()
    cmd.execute()

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the error message was printed
    assert "Can't do this command: Test Exception" in captured.out

def test_add_command(monkeypatch, capsys):
    """Test that AddCommand.execute() correctly adds two numbers"""
    # Mock input to provide test values
    inputs = iter(['add',"10.5", "5.5", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the correct result was printed
    assert "10.5 + 5.5 = 16.0" in captured.out

def test_add_command_invalid_input(monkeypatch, capsys):
    """Test that AddCommand.execute() handles invalid input gracefully"""
    # Mock input to provide invalid test values
    inputs = iter(['add', "a", "b", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the error message was printed
    assert "Invalid number input: a or b is not a valid number." in captured.out

def test_subtract_command(monkeypatch, capsys):
    """Test that AddCommand.execute() correctly adds two numbers"""
    # Mock input to provide test values
    inputs = iter(['subtract',"10.5", "5.5", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the correct result was printed
    assert "10.5 - 5.5 = 5.0" in captured.out

def test_subtract_command_invalid_input(monkeypatch, capsys):
    """Test that AddCommand.execute() handles invalid input gracefully"""
    # Mock input to provide invalid test values
    inputs = iter(['subtract', "a", "b", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the error message was printed
    assert "Invalid number input: a or b is not a valid number." in captured.out

def test_multiply_command(monkeypatch, capsys):
    """Test that AddCommand.execute() correctly adds two numbers"""
    # Mock input to provide test values
    inputs = iter(['multiply',"1", "2", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the correct result was printed
    assert "1 x 2 = 2" in captured.out

def test_multiply_command_invalid_input(monkeypatch, capsys):
    """Test that AddCommand.execute() handles invalid input gracefully"""
    # Mock input to provide invalid test values
    inputs = iter(['multiply', "a", "b", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the error message was printed
    assert "Invalid number input: a or b is not a valid number." in captured.out

def test_divide_command(monkeypatch, capsys):
    """Test that AddCommand.execute() correctly adds two numbers"""
    # Mock input to provide test values
    inputs = iter(['divide',"2", "2", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the correct result was printed
    assert "2 / 2 = 1" in captured.out

def test_divide_command_invalid_input(monkeypatch, capsys):
    """Test that AddCommand.execute() handles invalid input gracefully"""
    # Mock input to provide invalid test values
    inputs = iter(['divide', "a", "b", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the error message was printed
    assert "Invalid number input: a or b is not a valid number." in captured.out

def test_print_command(mocker, caplog):
    """
    Test that PrintCommand.execute() calls Calculator.print_history()
    and logs the expected message.
    """
    # Patch the Calculator.print_history method to prevent actual output.
    mock_print_history = mocker.patch.object(Calculator, 'print_history')
    # Instantiate the command and execute it.
    cmd = PrintCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    # Assert that the patched method was called.
    mock_print_history.assert_called_once()
    # Verify that the log contains the expected message.
    assert 'Printed calculator local history.' in caplog.text

def test_save_data_command(mocker, caplog):
    """
    Test that SaveDataCommand.execute() calls Calculator.save_history_to_csv()
    and logs the expected messages.
    """
    # Patch the Calculator.save_history_to_csv method.
    mock_save_history = mocker.patch.object(Calculator, 'save_history_to_csv')
    # Instantiate the command and execute it.
    cmd = SaveDataCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    # Assert that the patched method was called.
    mock_save_history.assert_called_once()
    # Verify that both log messages are present.
    assert 'Save data command called' in caplog.text
    assert 'Data saved to CSV file' in caplog.text

def test_clear_data_command(mocker, caplog):
    """
    Test that ClearDataCommand.execute() calls Calculator.clear_history()
    and logs the expected message.
    """
    # Patch Calculator.clear_history to avoid side effects
    mock_clear = mocker.patch.object(Calculator, 'clear_history')
    cmd = ClearDataCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    mock_clear.assert_called_once()
    assert 'Cleared calculator local history.' in caplog.text


def test_delete_csv_command(mocker, caplog):
    """
    Test that DeleteCSVCommand.execute() calls Calculator.delete_csv()
    and logs the expected messages.
    """
    # Patch Calculator.delete_csv to avoid deleting an actual file
    mock_delete_csv = mocker.patch.object(Calculator, 'delete_csv')
    cmd = DeleteCSVCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    mock_delete_csv.assert_called_once()
    assert 'Delete CSV command called' in caplog.text
    assert 'CSV file deleted.' in caplog.text


def test_delete_data_command_no_deletion(monkeypatch, mocker, caplog):
    """
    Test that DeleteDataCommand.execute() does not delete data
    when the user enters 0 (i.e. exit scenario).
    """
    # Patch methods to avoid real operations
    mock_print_all = mocker.patch.object(Calculator, 'print_all_calculations')
    mock_delete_at_index = mocker.patch.object(Calculator, 'delete_at_index')
    # Simulate user input "0" so that int("0")-1 == -1
    monkeypatch.setattr('builtins.input', lambda prompt: "0")
    cmd = DeleteDataCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    mock_print_all.assert_called_once()
    mock_delete_at_index.assert_not_called()
    assert 'Data not deleted' in caplog.text


def test_delete_data_command_deletion(monkeypatch, mocker, caplog):
    """
    Test that DeleteDataCommand.execute() deletes data when a valid index is provided.
    """
    # Patch methods to avoid side effects
    mock_print_all = mocker.patch.object(Calculator, 'print_all_calculations')
    mock_delete_at_index = mocker.patch.object(Calculator, 'delete_at_index')
    # Simulate valid user input "2", so delete_index becomes int("2")-1 == 1
    monkeypatch.setattr('builtins.input', lambda prompt: "2")
    cmd = DeleteDataCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    mock_print_all.assert_called_once()
    mock_delete_at_index.assert_called_once_with(1)
    assert 'Data deleted at location 2' in caplog.text


def test_delete_data_command_invalid_input(monkeypatch, mocker, caplog):
    """
    Test that DeleteDataCommand.execute() handles invalid input gracefully.
    """
    # Patch methods so that Calculator.delete_at_index is not called.
    # mock_print_all = mocker.patch.object(Calculator, 'print_all_calculations')
    mock_delete_at_index = mocker.patch.object(Calculator, 'delete_at_index')
    # Simulate invalid input that cannot be converted to int
    monkeypatch.setattr('builtins.input', lambda prompt: "invalid")
    cmd = DeleteDataCommand()
    with caplog.at_level(logging.ERROR):
        cmd.execute()
    mock_delete_at_index.assert_not_called()
    assert 'Invalid input. Please enter a valid number.' in caplog.text

def test_load_data_command(mocker, caplog):
    """
    Test that LoadDataCommand.execute() calls Calculator.load_csv_data()
    and logs the expected messages.
    """
    # Patch the Calculator.load_csv_data method.
    mock_load_csv = mocker.patch.object(Calculator, 'load_csv_data')
    # Instantiate and execute the command.
    cmd = LoadDataCommand()
    with caplog.at_level(logging.INFO):
        cmd.execute()
    # Verify that load_csv_data was called once.
    mock_load_csv.assert_called_once()
    # Verify that both expected log messages are present.
    assert 'Load data command called' in caplog.text
    assert 'Data loaded from CSV file' in caplog.text

def test_mean_command_valid(monkeypatch, capsys, faker):
    """
    Test that MeanCommand.execute() calculates the mean correctly
    for a valid list of numbers.
    """
    # Generate a list of random integers using faker.
    numbers = [faker.random_int(min=1, max=100) for _ in range(5)]
    input_str = ",".join(map(str, numbers))
    # Patch Calculator.mean to compute the mean as sum(values)/count.
    def mean_func(decimal_list):
        total = sum(decimal_list, Decimal(0))
        count = Decimal(len(decimal_list))
        return total / count
    monkeypatch.setattr(Calculator, 'mean', mean_func)
    # Patch input() to return our generated string.
    monkeypatch.setattr('builtins.input', lambda prompt: input_str)
    # Execute the command.
    cmd = MeanCommand()
    cmd.execute()
    # Capture and verify output.
    captured = capsys.readouterr()
    expected_mean = mean_func([Decimal(str(n)) for n in numbers])
    expected_output = f"mean({input_str}) = {expected_mean}"
    assert expected_output in captured.out

def test_mean_command_invalid(monkeypatch, capsys, faker):
    """
    Test that MeanCommand.execute() handles invalid input gracefully.
    An invalid value in the comma-separated list should trigger an error.
    """
    # Create an input string with an invalid number.
    invalid_input = "a," + ",".join(str(faker.random_int(min=1, max=100)) for _ in range(3))
    monkeypatch.setattr('builtins.input', lambda prompt: invalid_input)
    # Execute the command.
    cmd = MeanCommand()
    cmd.execute()
    # Capture output and verify that an error message was printed.
    captured = capsys.readouterr()
    assert "Invalid operation:" in captured.out

def test_median_command_valid(monkeypatch, capsys, faker):
    """
    Test that MedianCommand.execute() calculates the median correctly
    for a valid list of numbers.
    """
    # Generate a list of random integers using faker.
    numbers = [faker.random_int(min=1, max=100) for _ in range(5)]
    input_str = ",".join(map(str, numbers))
    # Define a median function for testing purposes.
    def median_func(decimal_list):
        sorted_list = sorted(decimal_list)
        n = len(sorted_list)
        if n % 2 == 1:
            return sorted_list[n // 2]
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    # Patch Calculator.median to use our median_func.
    monkeypatch.setattr(Calculator, 'median', median_func)
    # Patch input() to return our generated comma-separated string.
    monkeypatch.setattr('builtins.input', lambda prompt: input_str)
    # Execute the command.
    cmd = MedianCommand()
    cmd.execute()
    # Capture and verify output.
    captured = capsys.readouterr()
    expected_result = median_func([Decimal(str(n)) for n in numbers])
    expected_output = f"Median({input_str}) = {expected_result}"
    assert expected_output in captured.out

def test_median_command_invalid(monkeypatch, capsys, faker):
    """
    Test that MedianCommand.execute() handles invalid input gracefully.
    An invalid value in the comma-separated list should trigger an error.
    """
    # Create an input string with an invalid value.
    invalid_input = "a," + ",".join(str(faker.random_int(min=1, max=100)) for _ in range(3))
    monkeypatch.setattr('builtins.input', lambda prompt: invalid_input)
    # Execute the command.
    cmd = MedianCommand()
    cmd.execute()
    # Capture output and verify that an error message was printed.
    captured = capsys.readouterr()
    assert "Invalid operation:" in captured.out

def test_mode_command_valid(monkeypatch, capsys, faker):
    """
    Test that ModeCommand.execute() calculates the mode correctly
    for a valid list of numbers.
    """
    # Generate a duplicate value to serve as the mode.
    mode_value = faker.random_int(min=1, max=100)
    other1 = faker.random_int(min=1, max=100)
    while other1 == mode_value:
        other1 = faker.random_int(min=1, max=100)
    other2 = faker.random_int(min=1, max=100)
    while other2 in (mode_value, other1):
        other2 = faker.random_int(min=1, max=100)
    # Create a list that has mode_value repeated.
    values = [mode_value, mode_value, other1, other2]
    input_str = ",".join(map(str, values))
    # Patch Calculator.mode to return a list containing the mode_value as a Decimal.
    monkeypatch.setattr(Calculator, 'mode', lambda decimals: [Decimal(str(mode_value))])
    # Patch input() to return our generated comma-separated string.
    monkeypatch.setattr('builtins.input', lambda prompt: input_str)
    # Execute the command.
    cmd = ModeCommand()
    cmd.execute()
    # Capture and verify output.
    captured = capsys.readouterr()
    expected_output = f"mode({input_str}) = ['{str(mode_value)}']"
    assert expected_output in captured.out

def test_mode_command_invalid(monkeypatch, capsys, faker):
    """
    Test that ModeCommand.execute() handles invalid input gracefully.
    An invalid value in the comma-separated list should trigger an error.
    """
    # Create an input string with an invalid number.
    invalid_input = "a," + ",".join(str(faker.random_int(min=1, max=100)) for _ in range(3))
    monkeypatch.setattr('builtins.input', lambda prompt: invalid_input)
    # Execute the command.
    cmd = ModeCommand()
    cmd.execute()
    # Capture output and verify that an error message was printed.
    captured = capsys.readouterr()
    assert "Invalid operation:" in captured.out
