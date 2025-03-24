"""
Unit tests for the text_processing module.
"""

import unittest
import sys
import os

# Add the parent directory to the path to import my_awesome_lib
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_awesome_lib import text_processing

class TestTextProcessing(unittest.TestCase):
    
    def test_count_words(self):
        """Test the count_words function."""
        self.assertEqual(text_processing.count_words("This is a test"), 4)
        self.assertEqual(text_processing.count_words(""), 0)
        self.assertEqual(text_processing.count_words("  Spaces  "), 1)
        with self.assertRaises(TypeError):
            text_processing.count_words(123)
    
    def test_remove_punctuation(self):
        """Test the remove_punctuation function."""
        self.assertEqual(
            text_processing.remove_punctuation("Hello, how are you?"),
            "Hello how are you"
        )
        self.assertEqual(
            text_processing.remove_punctuation("a,b.c;d!e"),
            "abcde"
        )
        with self.assertRaises(TypeError):
            text_processing.remove_punctuation(123)
    
    def test_most_common_words(self):
        """Test the most_common_words function."""
        result = text_processing.most_common_words("this is a test this is", 3)
        self.assertEqual(result, [('this', 2), ('is', 2), ('a', 1)])
        
        # Test with empty text
        self.assertEqual(text_processing.most_common_words("", 3), [])
        
        # Test with invalid parameters
        with self.assertRaises(TypeError):
            text_processing.most_common_words(123, 3)
        with self.assertRaises(TypeError):
            text_processing.most_common_words("text", "3")
        with self.assertRaises(ValueError):
            text_processing.most_common_words("text", 0)

if __name__ == '__main__':
    unittest.main()