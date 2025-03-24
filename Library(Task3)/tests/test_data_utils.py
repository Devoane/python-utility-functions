import pytest
from my_lib.data_utils import convert_dicts_to_json, parse_json

class TestDataUtils:
    """Test suite for data_utils module."""
    
    def test_convert_dicts_to_json(self):
        input_data = [{"id": 1, "name": "Test"}]
        output = convert_dicts_to_json(input_data)
        assert '"id": 1' in output
        assert '"name": "Test"' in output
        assert output.count('\n') > 3  # Verify pretty-printing

    def test_parse_valid_json(self):
        assert parse_json('[{"valid": true}]') == [{"valid": True}]

    def test_parse_invalid_json(self):
        with pytest.raises(ValueError, match="Invalid JSON"):
            parse_json("{invalid}")