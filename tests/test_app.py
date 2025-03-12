'''Tests for the App class'''
import pytest
from app import App

def test_app_start_exit_command(monkeypatch):
    '''Test that the REPL exists correctly on 'exit' command'''
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unkown_command(capfd, monkeypatch):
    '''Test that the REPL handles unknown commands correctly'''
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code

    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
