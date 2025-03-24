import unittest  # https://docs.python.org/3/library/unittest.html
from app import is_valid_email, calculate_area, filter_and_sort_list, convert_date_format, is_palindrome

class TestUtilityFunctions(unittest.TestCase):
    """Unit tests for utility functions in app.py"""

    def setUp(self):
        """Set up common test data before each test."""
        self.valid_emails = ["test@example.com", "user.name@domain.co", "name+alias@sub.domain.com"]
        self.invalid_emails = ["invalid-email", "missing@dotcom", "@nouser.com", "user@.com"]
        
        self.area_test_cases = [
            ("circle", 5, None, 78.54),
            ("square", 4, None, 16),
            ("rectangle", 3, 6, 18)
        ]

        self.invalid_shapes = ["triangle", "hexagon"]

        self.date_test_cases = [
            ("25-12-2023", "2023/12/25"),
            ("01-01-2000", "2000/01/01")
        ]

        self.palindromes = ["madam", "racecar", "Aibohphobia"]
        self.non_palindromes = ["hello", "world", "Python"]

    def test_is_valid_email(self):
        """Tests email validation function with valid and invalid emails."""
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email), f"Valid email '{email}' was marked as invalid.")

        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), f"Invalid email '{email}' was marked as valid.")

    def test_calculate_area(self):
        """Tests area calculation function for different shapes."""
        for shape, a, b, expected in self.area_test_cases:
            with self.subTest(shape=shape, a=a, b=b):
                self.assertEqual(calculate_area(shape, a, b), expected, f"Failed for shape {shape}.")

        for shape in self.invalid_shapes:
            with self.assertRaises(ValueError, msg=f"Shape {shape} should raise ValueError"):
                calculate_area(shape, 5)

    def test_filter_and_sort_list(self):
        """Tests filtering and sorting of even numbers from a list."""
        self.assertEqual(filter_and_sort_list([5, 2, 8, 3, 10]), [2, 8, 10])
        self.assertEqual(filter_and_sort_list([]), [])
        self.assertEqual(filter_and_sort_list([7, 9, 11]), [])

    def test_convert_date_format(self):
        """Tests date format conversion function."""
        for input_date, expected_output in self.date_test_cases:
            with self.subTest(input_date=input_date):
                self.assertEqual(convert_date_format(input_date), expected_output)

        with self.assertRaises(ValueError, msg="Invalid date should raise ValueError"):
            convert_date_format("invalid-date")

    def test_is_palindrome(self):
        """Tests palindrome checking function."""
        for word in self.palindromes:
            with self.subTest(word=word):
                self.assertTrue(is_palindrome(word), f"'{word}' should be a palindrome.")

        for word in self.non_palindromes:
            with self.subTest(word=word):
                self.assertFalse(is_palindrome(word), f"'{word}' should NOT be a palindrome.")

if __name__ == "__main__":
    unittest.main()
