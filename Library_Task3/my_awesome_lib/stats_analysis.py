"""
Module containing functions for statistical analysis.
"""

import math
from typing import List, Union

def mean(numbers: List[Union[int, float]]) -> float:
    """
    Calculates the arithmetic mean of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        float: Arithmetic mean
        
    Raises:
        ValueError: If the list is empty
        TypeError: If elements of the list are not numbers
        
    Examples:
        >>> mean([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be numbers")
    
    return sum(numbers) / len(numbers)

def median(numbers: List[Union[int, float]]) -> float:
    """
    Calculates the median of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        float: Median
        
    Raises:
        ValueError: If the list is empty
        TypeError: If elements of the list are not numbers
        
    Examples:
        >>> median([1, 3, 5, 7, 9])
        5
        >>> median([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be numbers")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]

def standard_deviation(numbers: List[Union[int, float]]) -> float:
    """
    Calculates the standard deviation of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        float: Standard deviation
        
    Raises:
        ValueError: If the list has fewer than 2 elements
        TypeError: If elements of the list are not numbers
        
    Examples:
        >>> round(standard_deviation([1, 2, 3, 4, 5]), 2)
        1.41
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least 2 elements")
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be numbers")
    
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)
