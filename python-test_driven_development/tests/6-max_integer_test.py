#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function
    """
    def test_max_integer(self):
        """Method to test the max_integer function
        """
        # Test case 1: List with positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test case 2: List with positive integers in descending order
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

        # Test case 3: List with negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test case 4: List with positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

        # Test case 5: List with duplicate integers
        self.assertEqual(max_integer([1, 2, 2, 3, 4]), 4)

        # Test case 6: Empty list and None
        self.assertEqual(max_integer([]))
        self.assertEqual(max_integer([1, 2, 3, None]))

        # Test case 7: List with a single element
        self.assertEqual(max_integer([5]), 5)

        # Test case 8: List with non-integer element
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "a"])
