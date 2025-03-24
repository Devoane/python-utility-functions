"""
Unit tests for the stats_analysis module.
"""

import unittest
import math
from my_awesome_lib import stats_analysis

class TestStatsAnalysis(unittest.TestCase):
    
    def test_mean(self):
        self.assertEqual(stats_analysis.mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(stats_analysis.mean([0, 0, 0]), 0.0)
        self.assertEqual(stats_analysis.mean([-1, 1]), 0.0)
        
        # Error tests
        with self.assertRaises(ValueError):
            stats_analysis.mean([])
        with self.assertRaises(TypeError):
            stats_analysis.mean(["a", "b"])
    
    def test_median(self):
        # Odd number of elements
        self.assertEqual(stats_analysis.median([1, 3, 5, 7, 9]), 5)
        # Even number of elements
        self.assertEqual(stats_analysis.median([1, 2, 3, 4]), 2.5)
        # Unsorted list
        self.assertEqual(stats_analysis.median([9, 1, 5, 3, 7]), 5)
        
        # Error tests
        with self.assertRaises(ValueError):
            stats_analysis.median([])
        with self.assertRaises(TypeError):
            stats_analysis.median(["a", "b"])
    
    def test_standard_deviation(self):
        # Accuracy to 2 decimal places
        self.assertAlmostEqual(
            stats_analysis.standard_deviation([1, 2, 3, 4, 5]),
            1.41,
            places=2
        )
        self.assertEqual(stats_analysis.standard_deviation([0, 0, 0]), 0.0)
        
        # Error tests
        with self.assertRaises(ValueError):
            stats_analysis.standard_deviation([1])
        with self.assertRaises(TypeError):
            stats_analysis.standard_deviation(["a", "b"])

if __name__ == '__main__':
    unittest.main()
