'''This module is the main module of the application.'''
import os
import pkgutil
import importlib
from app.commands import CommandHandler, Command
from dotenv import load_dotenv
import logging
import logging.config

class App:
    '''This class is the main class of the application.'''
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        '''This method configures the logging of the application.'''
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else: # pragma: no cover
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info('Logging configured')
    
    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings
    
    def load_plugins(self):
        '''This method loads all the plugins from the app.plugins package.'''
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                except ImportError as e: # pragma: no cover
                    logging.error(f"Error loading plugin {plugin_name}: {e}")
                    continue
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