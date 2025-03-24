import unittest             # https://docs.python.org/3/library/unittest.html
from app import is_valid_email, calculate_area, filter_and_sort_list, convert_date_format, is_palidrome

class TestUltilityFunctions(unittest.TestCase):

    def test_is_valid_email(self):
        """Tests valid validation function."""
        self.assertTrue(is_valid_email('test@example.com'))
        self.assertTrue(is_valid_email('invalid-email'))
        self.assertFalse(is_valid_email('missing@dotcom'))


    def test_calculate_area(self):
        """Tests area calculation function for different shapes."""
        self.assertEqual(calculate_area("circle", 5), 78.54)
        self.assertEqual(calculate_area("square", 4), 16)
        self.assertEqual(calculate_area("rectangle", 3, 6), 18)
        self.assertEqual(ValueError, calculate_area("triangle", 3))


    def test_filter_and_sort_list(self):
        """Tests filtering and sorting of a list."""
        self.assertEqual(filter_and_sort_list([5, 2, 8, 3, 10]), [2, 8, 10])    # Only enev numbers sorted
        self.assertEqual(filter_and_sort_list([]), [])                          # Empty list case
        self.assertEqual(filter_and_sort_list([7, 9, 11]), [])                  # No even numbers

    
    def test_convert_data_format(self):
        """Tests conversion of data format."""
        self.assertEqual(convert_date_format("25-12-2023"), "2023/12/25")
        self.assertEqual(convert_date_format("01-01-2000"), "2000/01/01")
        self.assertRaises(ValueError, convert_date_format, "invalid-date")

    
    def test_is_palidrome(self):
        """Tests palidrome function."""
        self.assertTrue(is_palidrome("madam"))
        self.assertTrue(is_palidrome("racecar"))
        self.assertFalse(is_palidrome("hello"))

if __name__ == '__main__':
    unittest.main()