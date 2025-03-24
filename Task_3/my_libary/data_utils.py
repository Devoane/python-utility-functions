"""
Module: data_utils
Provides functions for working with lists (e.g., removing duplicates, flattening nested lists).
"""

from typing import List, Any

def remove_duplicates(lst: List[Any]) -> List[Any]:
    """
    Removes duplicate elements from a list while preserving order.
    
    :param lst: List of elements (any type).
    :return: List without duplicates.
    """
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def flatten_list(nested_lst: List[Any]) -> List[Any]:
    """
    Flattens a nested list into a single-level list.

    :param nested_lst: List containing nested lists.
    :return: Flattened list.
    """
    flat_list = []
    for sublist in nested_lst:
        if isinstance(sublist, list):
            flat_list.extend(sublist)
        else:
            flat_list.append(sublist)
    return flat_list
