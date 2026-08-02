#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test a list already in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list in no particular order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list where the max is the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test calling the function with no argument."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test a list holding a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list of negative integers."""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_signs(self):
        """Test a list mixing negative and positive integers."""
        self.assertEqual(max_integer([-10, 0, 10]), 10)

    def test_duplicates(self):
        """Test a list where the max appears more than once."""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_single_string(self):
        """Test a string treated as a list of characters."""
        self.assertEqual(max_integer("hello"), "o")


if __name__ == '__main__':
    unittest.main()
