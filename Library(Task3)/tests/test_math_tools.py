import pytest
from my_awesome_lib.math_tools import add_numbers, factorial

class TestMathTools:
    def test_add_numbers(self):
        assert add_numbers(2, 3) == 5.0
        assert add_numbers(1.5, 2.5) == 4.0
        
    def test_add_numbers_invalid_input(self):
        with pytest.raises(TypeError):
            add_numbers("2", 3)
            
    def test_factorial(self):
        assert factorial(5) == 120
        assert factorial(0) == 1
        
    def test_factorial_errors(self):
        with pytest.raises(ValueError):
            factorial(-1)
        with pytest.raises(TypeError):
            factorial(2.5)