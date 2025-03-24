"""
Module containing functions for file operations.
"""

import os
import csv
import json
from typing import List, Dict, Any

def read_text_file(file_path: str) -> str:
    """
    Reads the content of a text file.
    
    Args:
        file_path: Path to the file
        
    Returns:
        str: File content as a string
        
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If there is no access to the file
        
    Examples:
        >>> content = read_text_file('example.txt')
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_csv_to_dict(file_path: str, delimiter: str = ',') -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns a list of dictionaries.
    
    Args:
        file_path: Path to the CSV file
        delimiter: Character separating columns (default is comma)
        
    Returns:
        List[Dict[str, str]]: List of dictionaries where keys are column headers
        
    Raises:
        FileNotFoundError: If the file does not exist
        
    Examples:
        >>> data = read_csv_to_dict('data.csv')
        >>> print(data[0]['name'])
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        return list(reader)

def save_to_json(data: Any, file_path: str, indent: int = 4) -> None:
    """
    Saves data to a JSON file.
    
    Args:
        data: Data to be saved (can be a list, dictionary, etc.)
        file_path: Path to the output file
        indent: Indentation in the JSON file (default is 4 spaces)
        
    Returns:
        None
        
    Raises:
        TypeError: If data cannot be serialized to JSON
        PermissionError: If there are no write permissions
        
    Examples:
        >>> save_to_json({'name': 'Jan', 'age': 30}, 'data.json')
    """
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=indent, ensure_ascii=False)
