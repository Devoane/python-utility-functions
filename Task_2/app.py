import re                       # https://docs.python.org/3/library/re.html
from datetime import datetime   # https://docs.python.org/3/library/datetime.html
import math


def is_valid_email(email):
    """Checks if the given email is valid."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'  # Improved regex
    return bool(re.match(pattern, email))

def calculate_area(shape, a, b=None):
    """Calculates the area of the given shape"""
    if shape == 'circle':
        return round(math.pi * a ** 2, 2)
    elif shape == 'square':
        return a * a
    elif shape == 'rectangle' and b is not None:
        return  a * b
    else:
        raise ValueError('Unsupported shape')
    
def filter_and_sort_list(numbers):
    """Filters even numbers and returns then sorted"""
    return sorted([num for num in numbers if num % 2 == 0])

def convert_date_format(date_str):
    """Converts date from DD-MM-YYYY to YYYY/MM/DD format."""
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")  # Convert string to datetime object
        return date_obj.strftime("%Y/%m/%d").strip()  # Ensure no unwanted characters
    except ValueError:
        raise ValueError("Invalid date format")

    
def is_palidrome(text):
    """Cheks if a given string is a palindrome"""
    return text == text[::-1]       # Reverse the string and compare.