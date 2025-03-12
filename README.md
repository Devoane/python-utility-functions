# *The Python Utility Functions*

## 📌 Description
**The Python Utility Functions** project is a colection of basic functions that make it easier to work with data in Python.
It is designed in a modular way, which makes the code redable and easy to develop.

The main functionalities include random data generation, mathematic operations, sorting, exception handling, and measuring execution time.
The project can be used as a basis for futher learning and developing programming skills.

## ⚙ Functionalities

### 🔹 1. **Generating random data**
- Creates a random list of integers between 1 and 100
- Creates a random list of letters from A-Z
- Each run generates new values

### 🔹 2. **Combining lists with `zip()`**
- Creates a list of `(number, letter)` pairs, e.g. `[(23, 'A'), (5, 'X')]`
- Useful for processing related data

### 🔹 3. **Data operations**
- **Sorting a list of numbers** – uses the `sorted()` function
- **Calculating square roots** – `math.sqrt()` calculates the square roots of positive numbers
- The results are saved in new lists

### 🔹 4. **Exception handling**
- `ZeroDivisionError` – handling division by zero error
- `TypeError` – protection against data type errors
- The `safe_division()` function returns the result or an error message

### 🔹 5. **Code execution time measurement**
- `time.time()` measures the start and end time of the operation
- `time.sleep(1)` simulates a longer operation
- The result is given in seconds

## 🛠 Python Modules
- **Python 3** – [Official Documentation](https://docs.python.org/3/)
- **Standard modules:**
  - `math` – [Documentation](https://docs.python.org/3/library/math.html)
    - [`math.sqrt(x)`](https://docs.python.org/3/library/math.html#math.sqrt) – calculates the square root of `x`
  - `random` – [Documentation](https://docs.python.org/3/library/random.html)
    - [`random.randint(a, b)`](https://docs.python.org/3/library/random.html#random.randint) – randomizes an integer from the range `[a, b]`
    - [`random.sample(population, k)`](https://docs.python.org/3/library/random.html#random.sample) – Selects `k` random unique elements from a list 
  - `time` – [Documentation](https://docs.python.org/3/library/time.html)
    - [`time.time()`](https://docs.python.org/3/library/time.html#time.time) – returns time in seconds since UNIX epoch
- **Python built-in functions:**
  - [`zip()`](https://docs.python.org/3/library/functions.html#zip) – combines elements from several lists into pairs
  - [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) – returns a sorted list
  - [`chr()`](https://docs.python.org/3/library/functions.html#chr) – converts an integer to its corresponding Unicode character
  - [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance) – checks if an object is an instance of a specific type or class
- **Exception handling:**
  - [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError) – exception when dividing by zero
  - [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError) – exception for invalid data type

## 🚀 Launch
1. Download the repository:
  `git clone https://github.com/Devoane/python-utility-functions.git)`
2. Go to directory:
  `cd python-utility-functions`
3. Run the program:
  `python task_1.py`
    



