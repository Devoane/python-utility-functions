# *Library_Task3*

## 📌 Description
**Library_Task3** is a Python library that provides various utility functions for text processing, file handling, and statistical analysis.  
It is designed to make it easier to work with text data, process files, and perform common file operations such as reading, writing, and parsing.  
The library also includes functions for basic statistical analysis, such as calculating the mean, median, and mode of datasets.

The library includes:
- Functions for analyzing and processing text data (word count, removing punctuation, finding most common words)
- File handling utilities (reading text and CSV files, saving data to JSON)
- Statistical analysis functions (mean, median, mode)

## ⚙ Functionalities

### 🔹 1. **Text Processing**

#### **count_words(text: str) -> int**
- Counts the number of words in a text.
  
#### **remove_punctuation(text: str) -> str**
- Removes punctuation marks from the text.

#### **most_common_words(text: str, n: int = 5) -> List[Tuple[str, int]]**
- Returns the `n` most frequently occurring words in the text.

### 🔹 2. **File Handling**

#### **read_text_file(file_path: str) -> str**
- Reads the contents of a text file.
  
#### **read_csv_to_dict(file_path: str, delimiter: str = ',') -> List[Dict[str, str]]**
- Reads a CSV file and returns the data as a list of dictionaries.

#### **save_to_json(data: Any, file_path: str, indent: int = 4) -> None**
- Saves data to a JSON file.

### 🔹 3. **Statistical Analysis**

#### **mean(data: List[float]) -> float**
- Calculates the mean of a list of numbers.

#### **median(data: List[float]) -> float**
- Calculates the median of a list of numbers.

#### **standard_deviation(numbers: List[Union[int, float]]) -> float**
- Calculates the standard deviation of a list of numbers.

## 🛠 Python Modules
- **Python 3** – [Official Documentation](https://docs.python.org/3/)
- **Standard modules:**
  - `re` – [Documentation](https://docs.python.org/3/library/re.html)
    - Regular expressions for text processing.
  - `csv` – [Documentation](https://docs.python.org/3/library/csv.html)
    - CSV file handling.
  - `json` – [Documentation](https://docs.python.org/3/library/json.html)
    - JSON file handling.
  - `os` – [Documentation](https://docs.python.org/3/library/os.html)
    - File system operations.
  - `collections.Counter` – [Documentation](https://docs.python.org/3/library/collections.html#collections.Counter)
    - A class to count the occurrences of items in a collection.
  - `statistics` – [Documentation](https://docs.python.org/3/library/statistics.html)
    - Built-in module for statistical calculations.
- **Python built-in functions:**
  - [`open()`](https://docs.python.org/3/library/functions.html#open) – used to open files.
  - [`os.path.exists()`](https://docs.python.org/3/library/os.path.html#os.path.exists) – checks if a file or directory exists.

## 🚀 Launch

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/Library_Task3.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Library_Task3
    ```
3. To install the library locally:
    ```bash
    pip install -e .
    ```

## 💻 Examples of Usage

### Example 1: Text Processing

```python
from Library_Task3.text_processing import count_words, remove_punctuation, most_common_words

text = "This is a sample text. It includes punctuation and some repeated words."

# Count words
word_count = count_words(text)
print(word_count)  # Output: 9

# Remove punctuation
clean_text = remove_punctuation(text)
print(clean_text)  # Output: "This is a sample text It includes punctuation and some repeated words"

# Find most common words
common_words = most_common_words(text, n=3)
print(common_words)  # Output: [('is', 2), ('a', 1), ('sample', 1)]
```

### Example 2: File Handling.

```python
from Library_Task3.file_utils import read_text_file, read_csv_to_dict, save_to_json

# Read text file
text = read_text_file("example.txt")
print(text)

# Read CSV file to dictionary
csv_data = read_csv_to_dict("data.csv")
print(csv_data)

# Save data to JSON
data = {"name": "John", "age": 30}
save_to_json(data, "output.json")
```

### Example 3: Statistic Analysis.

```python
from Library_Task3.stats_analysis import mean, median, standard_deviation

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate mean
mean_value = mean(data)
print(mean_value)  # Output: 5.5

# Calculate median
median_value = median(data)
print(median_value)  # Output: 5.5

# Calculate standard deviation
std_dev = standard_deviation(data)
print(round(std_dev, 2))  # Output: 2.87
```

## 💌 License.

This project is licensed under the MIT License - see the [LICENSE](./LICENSE.txt)
 file for details.
