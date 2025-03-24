# **Test-Driven Development (TDD) - Unit Testing in Python**  

## 📌 Description  
This project demonstrates **Test-Driven Development (TDD)** by implementing five utility functions and writing unit tests for them using Python's `unittest` module. The goal is to develop reliable and well-tested code by first writing tests and then implementing functions to pass those tests.  

## ⚙️ Implemented Functions  

1. **Email Validation (`is_valid_email`)**  
   - Checks if an email address is valid (contains `@` and `.` in proper places).  

2. **Area Calculation (`calculate_area`)**  
   - Calculates the area of different shapes (`circle`, `square`, `rectangle`).  

3. **List Filtering & Sorting (`filter_and_sort_list`)**  
   - Filters even numbers from a list and returns them sorted.  

4. **Date Format Conversion (`convert_date_format`)**  
   - Converts dates from `DD-MM-YYYY` format to `YYYY/MM/DD`.  

5. **Palindrome Checker (`is_palindrome`)**  
   - Checks if a given text is a palindrome.  

## 🧪 Unit Tests  

Each function has **at least three test cases** covering:  
✅ **Valid inputs**  
✅ **Edge cases**  
✅ **Invalid inputs (error handling)**  

Tests are implemented in `test_app.py` using the `unittest` framework.  

## 🚀 Launch
1. Download the repository:
  `git clone https://github.com/Devoane/python-utility-functions.git)`
2. Go to directory:
  `cd python-utility-functions/test_driven_development(Task2)`
3. Run all unit test using `unittest`.
  `python -m unittest test_app.py`

## 🛠 Python Modules
- **Python 3** – [Official Documentation](https://docs.python.org/3/)
- **Testing Framework:**
  - `unittest` – [Documentation](https://docs.python.org/3/library/unittest.html)
  - Assertion methods
    - [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)
    - [`assertTrue()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue)
    - [`assertRaises()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)
- **Standard Python Modules**
  - `re` - [Documentation](https://docs.python.org/3/library/re.html)
  - `datetime` - [Documentation](https://docs.python.org/3/library/datetime.html)
  - `math` - [Documentation](https://docs.python.org/3/library/math.html)
