'''This file is the main file of the data_handler package.'''
import os  
import logging
import pandas as pd

from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class DataHandler:
    def __init__(self):
        folder_path = os.environ.get('CALCULATOR_HISTORY_FOLDER_PATH')
        file_name = os.environ.get('CALCULATOR_HISTORY_FILE_NAME')
        
        if not folder_path or not file_name:
            raise ValueError("Environment variables 'CALCULATOR_HISTORY_FOLDER_PATH' or 'CALCULATOR_HISTORY_FILE_NAME' are not set")
        
        os.makedirs(folder_path, exist_ok=True)
        self.csv_filepath = os.path.join(folder_path, file_name)
        self.csv_data = self.load_csv_data()
        self.operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }

    def load_csv_data(self) -> list[dict]:
        '''Load CSV data from the file system.'''
        if os.path.exists(self.csv_filepath):
            try:
                df = pd.read_csv(self.csv_filepath)
                # Convert numeric fields (if necessary)
                df['num_1'] = pd.to_numeric(df['num_1'], errors='coerce')
                df['num_2'] = pd.to_numeric(df['num_2'], errors='coerce')
                # Convert to list of dictionaries
                data = df.to_dict(orient='records')
                return data
            except Exception as e:
                # logging.error(f"Error reading CSV file: {e}")
                return []
        else:
            logging.warning('CSV file not found')
            return []

    def add_to_csv(self, calculation):
        '''Add a calculation to the CSV data.'''
        to_add_data = {
            'num_1': calculation.a,
            'num_2': calculation.b,
            'operator': calculation.operation.__name__,
        }
        # Append new row to the list
        self.csv_data.append(to_add_data)

    def save_csv_data(self):
        '''Save the CSV data to the file system using pandas.'''
        try:
            df = pd.DataFrame(self.csv_data)
            df.to_csv(self.csv_filepath, index=False)
            logging.info(f"Data saved to {self.csv_filepath}")
        except Exception as e:
            logging.error(f"Error saving data to CSV: {e}")

    def clear_csv_data(self):
        '''Clear all CSV data.'''
        self.load_csv_data()
        self.csv_data = []
        self.save_csv_data()
        logging.info("CSV data cleared.")

    def get_csv_data(self) -> list[dict]:
        '''Return the current CSV data.'''
        return self.csv_data
    def convert_to_calculation(self) -> dict:
        '''Convert the CSV data to a list of Calculation objects.'''
        return [Calculation(row['num_1'], row['num_2'], self.operations[row['operator']]) for row in self.csv_data]
