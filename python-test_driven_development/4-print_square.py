#!/usr/bin/python3
"""This module supplies one function, print_square.

print_square(size) prints a square made of the # character.
The size given must be a positive integer, and it determines
both the width and the height of the square.
"""


def print_square(size):
    """Print a square of size "size" using the # character.

    size must be an integer greater than or equal to 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
