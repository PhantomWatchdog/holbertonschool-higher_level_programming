#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function
    """
    # Test case 1: Test with a single element list
    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([5]), 5)

    # Test case 2: Test with multiple elements
    def test_positive_numbers(self):
        """Test with positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1, 3, 2, 5, 4]), 5)

    # Test case 3: Test with negative numbers
    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -3, -2, -5, -4]), -1)

    # Test case 4: Test with mixed numbers
    def test_mixed_numbers(self):
        """Testwith mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)
        self.assertEqual(max_integer([0, -1, -2, -3, -4]), 0)
        self.assertEqual(max_integer([-1, 0, 1, 2, 3]), 3)

    # Test case 5: Test with duplicate numbers
    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        self.assertEqual(max_integer([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([1, 2, 2, 3, 3]), 3)

    # Test case 6: Test with non integer
    def test_non_integer_elements(self):
        """Test with non-integer elements raises a TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])

    # Test case 7: Test with None as an element
    def test_none_as_element(self):
        """Test with None as an element raises a TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, None, 3, 4])

    # Test case 8: Test with an empty list
    def test_empty_list(self):
        """Test that an empty list returns None"""
        self.assertIsNone(max_integer([]))
