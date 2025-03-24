import json
from typing import List, Dict, Union

def convert_dicts_to_json(data: List[Dict[str, Union[str, int, float]]]) -> str:
    """Convert a list of dictionaries to a formatted JSON string.

    Uses Python's built-in `json` module (https://docs.python.org/3/library/json.html).
    Handles common data types including strings, integers, and floats.

    Args:
        data: List of dictionaries to convert.
               Example: [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]

    Returns:
        Pretty-printed JSON string with 4-space indentation.

    Example:
        >>> data = [{"id": 1, "value": 3.14}]
        >>> print(convert_dicts_to_json(data))
        [
            {
                "id": 1,
                "value": 3.14
            }
        ]

    Note:
        For datetime objects or other non-serializable types, 
        consider extending with a custom JSON encoder.
    """
    return json.dumps(data, indent=4)


def parse_json(json_str: str) -> List[Dict[str, Union[str, int, float]]]:
    """Parse a JSON string into Python objects.

    Uses `json.loads()` from Python's standard library:
    https://docs.python.org/3/library/json.html#json.loads

    Args:
        json_str: Valid JSON string to parse.
                  Example: '[{"key": "value"}]'

    Returns:
        Deserialized Python object (typically list or dict).

    Raises:
        ValueError: When input is not valid JSON (wrapped from json.JSONDecodeError).

    Example:
        >>> parse_json('[{"test": 123}]')
        [{'test': 123}]
    """
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {str(e)}") from e