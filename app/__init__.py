'''This module is the main module of the application. It is responsible for'''
import pkgutil
import importlib
from app.commands import CommandHandler, Command

class App:
    '''This class is the main class of the application. It is responsible for'''
    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        '''This method loads all the plugins from the app.plugins package.'''
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_handler.set_command(plugin_name, item())
                    except TypeError:
                        continue

    def start(self):
        '''This method starts the application.'''
        self.load_plugins()
        print("Type 'menu' to see all available commands. Type 'exit' to exit.")
        while True:
            self.command_handler.executed_command(input(">>> ").strip())