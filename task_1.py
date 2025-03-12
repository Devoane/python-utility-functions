import math         # https://docs.python.org/3/library/math.html
import random       # https://docs.python.org/3/library/random.htm
import time         # https://docs.python.org/3/library/time.html

def generate_random_data(size=5):
    """Generates random numerical and textual data."""
    numbers = [random.randint(0, 100) for _ in range(size)]                   # https://docs.python.org/3/library/random.html#random.randint
    letters = [chr(random.randint(65, 90)) for _ in range(size)]              # https://docs.python.org/3/library/random.html#random.randint
    return numbers, letters

def zipped(list1, list2):
    """Zips two lists together."""
    return list(zip(list1, list2))                                            # https://docs.python.org/3/library/functions.html#zip

def process_data(data):
    """Sorts data and calculates the roots of numbers."""
    sorted_data = sorted(data)                                                # https://docs.python.org/3/library/functions.html#sorted
    sqrt_data = [math.sqrt(x) if x > 0 else None for x in sorted_data]        # https://docs.python.org/3/library/math.html#math.sqrt
    return sorted_data, sqrt_data

def safe_division(numbers):
    """Performs a single division operation with error handling."""
    if len(numbers) < 2:
        return ['Not enough numbers for division.']
    
    a, b = random.sample(numbers, 2)                                         # https://docs.python.org/3/library/random.html#random.sample

    try:
        # Check types for TypeError
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))): # https://docs.python.org/3/library/functions.html#isinstance
            raise TypeError('Invalid type for division.')
        
        result = a / b
        return [f'{a} / {b} = {result:.2f}']
    except ZeroDivisionError:                                                # https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
        return [f'{a} / {b} = Division by zero.']
    except TypeError as e:                                                   # https://docs.python.org/3/library/exceptions.html#TypeError
        return [f'Type Error: = {e}']
    
def main():
    start_time = time.time()                                                 # https://docs.python.org/3/library/time.html#time.time
    # Generate random data
    numbers, letters = generate_random_data()
    print('Numbers:', numbers)
    print('Letters:', letters)

    # Zip lkist into pairs
    zipped_data = zipped(numbers, letters)
    print('Zipped pairs:', zipped_data)

    # Process numerical data (sorting and calculating square roots)
    sorted_numbers, sqrt_numbers = process_data(numbers)
    print('Sorted numbers:', sorted_numbers)
    print('Square roots:', sqrt_numbers)

    # Perform random division operations
    division_result = safe_division(sorted_numbers)
    print('Division Result (valid data):', division_result[0])

    # Test case for ZeroDivisionError
    zero_division_data = [10, 0, 20, 5]  # List containing zero
    print('Testing ZeroDivisionError handling:')
    division_result = safe_division(zero_division_data)
    print('Division Result (zero division):', division_result[0])

    # Test case for TypeError
    type_error_data = ['10', 20, 5]      # List containing string
    print('Testing TypeError handling:')
    division_result = safe_division(type_error_data)
    print('Division Result (type error):', division_result[0])

    # Calculate real execution time
    execution_time = time.time() - start_time
    print(f'Execution time: {execution_time:.5f} seconds')

if __name__ == '__main__':
    main()
        