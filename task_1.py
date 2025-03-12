import math         # https://docs.python.org/3/library/math.html
import random       # https://docs.python.org/3/library/random.htm
import time         # https://docs.python.org/3/library/time.html

def generate_random_data(size=5):
    """Generates random numerical and textual data."""
    numbers = [random.randint(0, 100) for _ in range(size)]
    letters = [chr(random.randint(65, 90)) for _ in range(size)]
    return numbers, letters

def zipped(list1, list2):
    """Zips two lists together."""
    return list(zip(list1, list2))    # https://docs.python.org/3/library/functions.html#zip

def process_data(data):
    """Sorts data and calculates the roots of numbers."""
    sorted_data = sorted(data)  # https://docs.python.org/3/library/functions.html#sorted
    sqrt_data = [math.sqrt(x) if x > 0 else None for x in sorted_data]   # https://docs.python.org/3/library/math.html#math.sqrt
    return sorted_data, sqrt_data

def safe_division(numbers):
    """Randomly selects two numbers from the list and divides them."""
    results = []
    for _ in range(len(numbers) // 2):    # Perform division multiple times but not for all elements.
        a, b = random.sample(numbers, 2)    # https://docs.python.org/3/library/random.html#random.sample
        try:
            results.append(f'{a} / {b} = {a / b:.2f}')
        except ZeroDivisionError:
            results.append(f'{a} / {b} = Division by zero')  # https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
        except TypeError:
            return None   # https://docs.python.org/3/library/exceptions.html#TypeError
    return results

def main():
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
    division_results = safe_division(sorted_numbers)
    print('Random Division Results:')
    for result in division_results:
        print(result)

    # Measure the execution time
    start_time = time.time()            # https://docs.python.org/3/library/time.html#time.time
    time.sleep(1)                       # https://docs.python.org/3/library/time.html#time.sleep
    print(f'Execution time: {time.time() - start_time:.2f} seconds')

if __name__ == '__main__':
    main()
        