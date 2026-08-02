#!/usr/bin/python3
"""This module defines the Rectangle class.

Rectangle inherits from Base and represents a rectangle described by
a width, a height and the x and y coordinates of its position. Every
attribute is validated through its own getter and setter.
"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle, inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The horizontal position of the rectangle.
            y (int): The vertical position of the rectangle.
            id (int): The identity of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, validating type and value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, validating type and value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The horizontal position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x, validating type and value."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: The vertical position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y, validating type and value."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the # character, honouring x and y."""
        for i in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update the rectangle attributes.

        Args:
            *args: id, width, height, x and y in that order.
            **kwargs: Attribute names and values, skipped if args given.
        """
        if args and len(args) != 0:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}

    def __str__(self):
        """Return the printable representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
