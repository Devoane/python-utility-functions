"""
Module: data_utils
Provides functions for working with lists (e.g., removing duplicates, flattening nested lists).
"""

from typing import List, Any  # Importing generic types for better type hinting
# https://docs.python.org/3/library/typing.html#typing.List

def remove_duplicates(lst: List[Any]) -> List[Any]:
    """
    Removes duplicate elements from a list while preserving order.
    
    :param lst: List of elements (any type).
    :return: List without duplicates.
    :rtype: List[Any]
    """
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def flatten_list(nested_lst: List[Any]) -> List[Any]:
    """
    Flattens a nested list into a single-level list.

    :param nested_lst: List containing nested lists or mixed elements.
    :return: Flattened list.
    :rtype: List[Any]
    """
    flat_list: List[Any] = []  # Explicitly defining variable type
    # https://docs.python.org/3/library/typing.html#typing.Any
    for sublist in nested_lst:
        if isinstance(sublist, list):
            flat_list.extend(sublist)
        else:
            flat_list.append(sublist)
    return flat_list
