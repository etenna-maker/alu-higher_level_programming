#!/usr/bin/python3
"""This module defines the Square class.

Square inherits from Rectangle and represents a rectangle whose width
and height are always equal. It reuses every validation rule already
defined by Rectangle for its size and position.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
            x (int): The horizontal position of the square.
            y (int): The vertical position of the square.
            id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size, assigning both width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square attributes.

        Args:
            *args: id, size, x and y in that order.
            **kwargs: Attribute names and values, skipped if args given.
        """
        if args and len(args) != 0:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}

    def __str__(self):
        """Return the printable representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
