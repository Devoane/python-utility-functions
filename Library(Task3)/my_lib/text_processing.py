"""
Module: text_processing
Provides functions for text manipulation.
"""

from typing import Union  # Importing Union for flexible type hinting
# https://docs.python.org/3/library/typing.html#typing.Union

def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in a given text.

    :param text: Input string.
    :return: Number of vowels in the text.
    :rtype: int
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def reverse_words(sentence: str) -> str:
    """
    Reverses the order of words in a given sentence.

    :param sentence: Input string.
    :return: Sentence with words reversed.
    :rtype: str
    """
    return " ".join(sentence.split()[::-1])
    