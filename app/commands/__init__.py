from abc import ABC, abstractmethod

class Command(ABC):
    '''This class is the abstract base class for all the commands.'''
    @abstractmethod
    def execute(self): # pragma: no cover
        '''This method is the abstract method that should be implemented in the child classes.'''
        pass

class CommandHandler:
    '''This class is responsible for handling the commands.'''
    def __init__(self):
        self.commands = {}
    
    def set_command(self, command_name: str, command: Command):
        '''This method sets the command.'''
        self.commands[command_name] = command
    
    def executed_command(self, command_name: str):
        '''This method executes the command.'''
        # EAFP (Easier to Ask for Forgiveness than Permission)
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f'No such command: {command_name}')
