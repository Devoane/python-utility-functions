"""
My Library - A Python utility library for data processing, mathematical operations, and text manipulation.
"""

from .data_utils import remove_duplicates, flatten_list
from .math_tools import factorial, gcd
from .text_processing import count_vowels, reverse_words

__all__ = ["remove_duplicates", "flatten_list", "factorial", "gcd", "count_vowels", "reverse_words"]
