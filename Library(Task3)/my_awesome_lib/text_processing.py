"""
Module containing text processing utilities.

This module provides functions for analyzing and manipulating text data.

References:
    - Regular expressions: https://docs.python.org/3/library/re.html
    - Collections module: https://docs.python.org/3/library/collections.html
"""

import re
from collections import Counter
from typing import List, Dict, Tuple

def count_words(text: str) -> int:
    """
    Count the number of words in a text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        int: The number of words in the text
        
    Raises:
        TypeError: If the text is not a string
        
    Examples:
        >>> count_words("This is a sample text")
        5
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    
    words = text.strip().split()
    return len(words)

def remove_punctuation(text: str) -> str:
    """
    Remove punctuation marks from text.
    
    Args:
        text (str): The text to process
        
    Returns:
        str: Text without punctuation marks
        
    Raises:
        TypeError: If the text is not a string
        
    Examples:
        >>> remove_punctuation("Hello, how are you?")
        'Hello how are you'
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    
    return re.sub(r'[^\w\s]', '', text)

def most_common_words(text: str, n: int = 5) -> List[Tuple[str, int]]:
    """
    Returns the n most frequently occurring words in the text.
    
    Args:
        text (str): The text to analyze
        n (int, optional): Number of words to return. Defaults to 5.
        
    Returns:
        list: List of tuples (word, count)
        
    Raises:
        TypeError: If the text is not a string or n is not an integer
        ValueError: If n is not a positive integer
        
    Examples:
        >>> most_common_words("this is a test this is an example")
        [('this', 2), ('is', 2), ('a', 1), ('test', 1), ('an', 1)]
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(n)