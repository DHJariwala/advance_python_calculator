'''This file is the main file of the data_handler package.'''
import os  
import logging
import pandas as pd
from calculator.statistic import CalculationStatistic
from dotenv import load_dotenv
from calculator.calculation import Calculation
from calculator.operations import add, mean, median, mode, subtract, multiply, divide
from decimal import Decimal

class DataHandler:
    def __init__(self):
        load_dotenv()
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
            'divide': divide,
            'mean': mean,
            'median': median,
            'mode' : mode
        }
        self.statistic_operations = ['mean', 'median','mode']

    def load_csv_data(self) -> list[dict]:
        '''Load CSV data from the file system.'''
        if os.path.exists(self.csv_filepath):
            try:
                df = pd.read_csv(self.csv_filepath)
                # Do not force numeric conversion so that list data remain intact
                data = df.to_dict(orient='records')
                return data
            except Exception as e:
                logging.error(f"Error reading CSV file: {e}")
                return []
        else:
            logging.warning('CSV file not found')
            return []

    def add_to_csv(self, calculation):
        '''Add a calculation to the CSV data.'''
        # If calculation.a is a list (as in CalculationStatistic), convert it to a string representation.
        if isinstance(calculation.a, list):
            num_1_val = repr(calculation.a)
        else:
            num_1_val = calculation.a

        to_add_data = {
            'num_1': num_1_val,
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
        self.csv_data = []
        logging.info("CSV data cleared.")

    def get_csv_data(self) -> list[dict]:
        '''Return the current CSV data.'''
        return self.csv_data

    def convert_to_calculation(self) -> list:
        '''Convert the CSV data to a list of Calculation objects.'''
        calculations = []
        for row in self.csv_data:
            operator = row['operator']
            if operator in self.statistic_operations:
                # For statistic operations, num_1 is stored as a string representation of a list of Decimals.
                try:
                    # Evaluate the string in a safe environment that only permits the Decimal constructor.
                    a_val = eval(row['num_1'], {"__builtins__": {}}, {"Decimal": Decimal})
                except Exception as e:
                    logging.error(f"Error converting num_1 to list of Decimals: {e}")
                    a_val = row['num_1']
                calculations.append(CalculationStatistic(a_val, self.operations[operator]))
            else:
                # For normal calculations, try to convert num_1 and num_2 to float.
                try:
                    a_val = float(row['num_1'])
                except Exception:
                    a_val = row['num_1']
                try:
                    b_val = float(row['num_2'])
                except Exception:
                    b_val = row['num_2']
                calculations.append(Calculation(a_val, b_val, self.operations[operator]))
        return calculations

    def delete_csv_file_data(self):
        '''Clear all CSV data.'''
        self.csv_data = []
        self.save_csv_data()
        logging.info("CSV data cleared.")
