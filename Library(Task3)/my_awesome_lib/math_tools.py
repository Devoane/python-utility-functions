def add_numbers(a: float, b: float) -> float:
    """Add two numbers with type checking.
    
    Args:
        a: First operand (float or int)
        b: Second operand (float or int)
    
    Returns:
        Sum of a and b as float
        
    Raises:
        TypeError: If inputs are not numbers
        
    Example:
        >>> add_numbers(2, 3.5)
        5.5
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return float(a + b)

def factorial(n: int) -> int:
    """Calculate factorial with input validation.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not integer
        
    Example:
        >>> factorial(5)
        120
    """
    if not isinstance(n, int):
        raise TypeError("Input must be integer")
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    return 1 if n <= 1 else n * factorial(n - 1)