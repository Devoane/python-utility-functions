import pytest
from my_awesome_lib.data_utils import convert_dicts_to_json, parse_json

class TestDataUtils:
    def test_convert_dicts_to_json(self):
        data = [{"name": "Alice", "age": 30}]
        result = convert_dicts_to_json(data)
        assert '"name": "Alice"' in result
        assert '"age": 30' in result

    def test_parse_json(self):
        json_str = '[{"test": 123}]'
        assert parse_json(json_str) == [{"test": 123}]