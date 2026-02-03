# Python - Module 2 - Assignment - Calculator Program

A simple interactive command-line calculator written in Python.  
The program is modular, testable, and designed with clean separation of
responsibilities. Unit tests are implemented using **pytest** with
coverage support.

---

## Features

- Interactive calculator loop
- Supported arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Modulo (`%`)
- Input validation with user-friendly error messages
- Graceful handling of invalid input and runtime errors
- Exit anytime using: `q`, `quit`, or `exit`
- Fully unit tested using pytest

---

## Requirements

- Python 3.12 or higher
- pytest
- pytest-cov (optional, for coverage)

---

## How to Run

From the project root directory:

```bash
python app/main.py
```

On startup, you will see instructions describing the input format and
available operators.

---

## Usage Examples

```text
10 + 5
20 - 4
6 * 7
8 / 2
10 % 3
```

Example output:

```text
> 10 + 5
15.0
```

---

## Exiting the Program

You can exit the calculator at any time by typing:

```text
q
quit
exit
```

---

## Error Handling

- Invalid input format:
  ```
  Error: Format: <number> <operator> <number>
  ```

- Non-numeric operands:
  ```
  Error: Operands must be numbers
  ```

- Division or modulo by zero:
  ```
  Error: Cannot divide by zero
  ```

- Unknown operator:
  ```
  Error: Unknown operator: <operator>
  ```

The program continues running after errors until you quit.

---

## Running Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest -v
```
---

## Design Overview

- **main.py**  
  Application entry point. Starts the calculator.

- **calculator/__init__.py**  
  Controls the interactive loop and delegates parsing and calculations.

- **parser/__init__.py**  
  Handles input validation and conversion.

- **operations/__init__.py**  
  Contains pure arithmetic functions with no side effects.

This structure ensures readability, testability, and maintainability.

---

## License

This project is provided for educational and learning purposes.
You are free to modify and extend it as needed.
