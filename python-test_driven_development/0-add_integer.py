#!/usr/bin/python3
"""This module supplies one function, add_integer.

add_integer(a, b) returns the sum of its two arguments.
Both arguments must be integers or floats, and floats are
cast to integers before the addition is performed.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Floats are cast to integers before addition.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
