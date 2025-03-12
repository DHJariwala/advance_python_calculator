'''This file contains the tests for the commands in the app/plugins directory'''
import os
import pytest
from app import App
from app.plugins.clear import ClearCommand

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
