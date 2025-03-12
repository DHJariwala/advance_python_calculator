'''This module contains the MenuCommand class.'''
import importlib
import pkgutil
from app.commands import Command

class MenuCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method prints the available commands.'''
        plugin_package = 'app.plugins'
        command_set = self._get_command_set(plugin_package = plugin_package)
        print("Available commands:")
        for command in command_set:
            print(f"- {command}")
    @staticmethod
    def _get_command_set(plugin_package):
        '''This method returns a set of available commands.'''
        command_set = []
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugin_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugin_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            command_set.append(plugin_name)
                    except TypeError:
                        continue
        return set(command_set)
