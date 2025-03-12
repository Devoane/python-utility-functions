import math         # https://docs.python.org/3/library/math.html
import random       # https://docs.python.org/3/library/random.htm
import time         # https://docs.python.org/3/library/time.html

def generate_random_data(size=5):
    """Generates random numerical and textual data."""
    numbers = [random.randint(1, 100) for _ in range(size)]
    letters = [chr(random.randint(65, 90)) for _ in range(size)]
    return numbers, letters

def zipped(list1, list2):
    """Zips two lists together."""
    return list(zip(list1, list2))    # https://docs.python.org/3/library/functions.html#zip

