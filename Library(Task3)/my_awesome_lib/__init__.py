"""
My Awesome Library - Data and Utility Functions

A Python package providing essential tools for:
- Data conversion (JSON/dict utilities)
- Mathematical operations
- Text processing

Exported Modules:
----------------
1. data_utils: JSON/dictionary conversion tools
2. math_tools: Basic mathematical operations
3. text_processing: String manipulation utilities

Usage Example:
-------------
>>> from my_awesome_lib import data_utils
>>> data = [{"sample": "data"}]
>>> json_str = data_utils.convert_dicts_to_json(data)

Version: 0.1.0
License: MIT
"""

from .data_utils import (
    convert_dicts_to_json,
    parse_json
)
from .math_tools import (
    add_numbers,
    calculate_average,
    factorial
)
from .text_processing import (
    reverse_string,
    count_vowels,
    is_palindrome
)

__all__ = [
    # Data utils
    'convert_dicts_to_json',
    'parse_json',
    
    # Math tools
    'add_numbers',
    'calculate_average',
    'factorial',
    
    # Text processing
    'reverse_string',
    'count_vowels',
    'is_palindrome'
]

__version__ = '0.1.0'
__author__ = 'Devoane'