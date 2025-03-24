"""
Unit tests for the file_utils module.
"""

import unittest
import os
import tempfile
import json
from my_awesome_lib import file_utils

class TestFileUtils(unittest.TestCase):
    
    def setUp(self):
        # Create temporary files for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file_path = os.path.join(self.temp_dir.name, "test_file.txt")
        self.test_csv_path = os.path.join(self.temp_dir.name, "test_file.csv")
        self.test_json_path = os.path.join(self.temp_dir.name, "test_file.json")
        
        # Create a text file
        with open(self.test_file_path, 'w', encoding='utf-8') as f:
            f.write("This is a test file.\nSecond line.")
        
        # Create a CSV file
        with open(self.test_csv_path, 'w', encoding='utf-8') as f:
            f.write("name,age,city\n")
            f.write("Jan,30,Warsaw\n")
            f.write("Anna,25,Krakow\n")
    
    def tearDown(self):
        # Remove temporary files
        self.temp_dir.cleanup()
    
    def test_read_text_file(self):
        content = file_utils.read_text_file(self.test_file_path)
        self.assertEqual(content, "This is a test file.\nSecond line.")
        
        # Test non-existent file
        with self.assertRaises(FileNotFoundError):
            file_utils.read_text_file("non_existent_file.txt")
    
    def test_read_csv_to_dict(self):
        data = file_utils.read_csv_to_dict(self.test_csv_path)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["name"], "Jan")
        self.assertEqual(data[1]["city"], "Krakow")
        
        # Test non-existent file
        with self.assertRaises(FileNotFoundError):
            file_utils.read_csv_to_dict("non_existent_file.csv")
    
    def test_save_to_json(self):
        test_data = {"name": "Test", "values": [1, 2, 3]}
        file_utils.save_to_json(test_data, self.test_json_path)
        
        # Check if the file exists
        self.assertTrue(os.path.exists(self.test_json_path))
        
        # Check the content of the file
        with open(self.test_json_path, 'r', encoding='utf-8') as f:
            loaded_data = json.load(f)
        
        self.assertEqual(loaded_data, test_data)

if __name__ == '__main__':
    unittest.main()
