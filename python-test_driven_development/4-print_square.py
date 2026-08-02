#!/usr/bin/python3
"""This module defines a function that prints a square.

print_square(size) prints a square made of the # character.
The size given must be a positive integer and sets both the
width and the height of the square.
"""


def print_square(size):
    """Print a square of size "size" using the # character.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than zero.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
