#!/usr/bin/python3
"""Defines a class Square with a private attribute size."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
