# Advance Python Calculator
This is an advance calculator for python that has REPL execution method on the terminal. The app has basic calculator functionality and statistic functionality. This project is a part of IS-601 course.

All of the data handling is done by pandas.
Created an intuitive interface for simplifying complex pandas functionality.

Done rigourous testing on the code and achieved **99% coverage** (all of the main functionalities have **100% coverage**).

All the test cases passed and proper formatting of the code was maininted with pylint.

Implemented proper logging functionality.

Practiced good version control and proper commit history.

Used clean code principles for proper maintainable and scalable codebase.



The application has the following functionalities (these are all **plugins**):
- add
  - add two numbers
- subtract
  - subtract two numbers
- multiply
  - multiply two numbers
- divide
  - divide two numbers
- mean
  - take mean of a list of numbers
- median
  - take median of a list of numbers
- mode
  - take mode of a list of numbers
- save_data
  - save's local history into CSV file and delete the local history
- load_data
  - load the data from CSV file into the local history
- delete_data
  - delete a specific calculation from local history
- delete_csv
  - delete all CSV data
- print_history
  - print's the local history
- clear_history
  - clear's the local history
- greet
  - greet's the user
- menu
  - shows all of the possible commands
- clear
  - clears the terminal
- exit
  - exit's the application

## Configuring the app

### Clone this project
```bash
git clone git@github.com:DHJariwala/advance_python_calculator.git
```
Make sure you are in the application folder
```bash
cd advance_python_calculator
```

### Virtual environment
Make the virtual environment using the following command
```bash
python3 -m venv venv
```
Activate the virtual environment on MacOS or Linux using the following command
```bash
source venv/bin/activate
```
Activate the virtual environment on Windows using the following command
```bash
.\venv\Scripts\activate
```

### Installing Requirements
Install all the requirements using
```bash
pip install -r requirements.txt
```

### Environment variables
make a environment variable file using the following
```bash
touch .env
```
Inside the `.env` file add the following environment variables
```bash
CALCULATOR_HISTORY_FOLDER_PATH = 'data'
CALCULATOR_HISTORY_FILE_NAME = 'calculator_history.csv'
```

### Running the app
Run the app using the following command
```bash
python3 main.py
```
If your python installation is not `python3`, maybe it's just `python`, in this case, run the following command
```bash
python main.py
```

## Rubrics

### Total Points: 100

#### ✅ Functionality (40 Points)

- ✅ **Calculator Operations:** 20 points for implementing basic and statistical operations.
- ✅ **History Management:** 10 points for effective management using Pandas.
- ✅ **Configuration via Environment Variables:** 5 points for flexible application configuration.
- ✅ **REPL Interface:** 5 points for a user-friendly command-line interface.

#### ✅ Design Patterns (20 Points)

- ✅ **Implementation and Application:** 10 points for the effective use of design patterns.
- ✅ **Documentation and Explanation:** 10 points for thorough documentation of design pattern rationale and implementation.

#### ✅ Testing and Code Quality (20 Points)

- ✅ **Comprehensive Testing with Pytest:** 10 points for extensive test coverage.
- ✅ **Code Quality and Adherence to Standards:** 10 points for clean, maintainable code.

#### ✅ Version Control, Documentation, and Logging (20 Points)

- ✅ **Commit History:** 10 points for logical and informative commit messages.
- ✅ **README Documentation:** 5 points for comprehensive setup and usage instructions.
- ✅ **Logging Practices:** 5 points for implementing adaptable and informative logging.

