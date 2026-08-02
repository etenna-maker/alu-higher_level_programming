#!/usr/bin/python3
"""Unittests for the Square class."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Test the creation of Square instances."""

    def test_is_rectangle(self):
        """Square inherits from Rectangle."""
        self.assertIsInstance(Square(10), Rectangle)

    def test_is_base(self):
        """Square inherits from Base as well."""
        self.assertIsInstance(Square(10), Base)

    def test_no_args(self):
        """Size is mandatory."""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        """Square takes at most four arguments."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_sets_both(self):
        """Size sets width and height together."""
        s = Square(10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_defaults(self):
        """x and y default to zero."""
        s = Square(10)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_all_args(self):
        """Every argument is assigned."""
        s = Square(10, 2, 3, 7)
        self.assertEqual((s.size, s.x, s.y, s.id), (10, 2, 3, 7))

    def test_ids_increment(self):
        """Ids increment when not given."""
        Base._Base__nb_objects = 0
        self.assertEqual(Square(1).id, 1)
        self.assertEqual(Square(1).id, 2)

    def test_size_is_private(self):
        """Width stays private behind size."""
        with self.assertRaises(AttributeError):
            print(Square(10).__size)


class TestSquareSize(unittest.TestCase):
    """Test the size getter and setter."""

    def test_getter(self):
        """The getter returns the width."""
        self.assertEqual(Square(7).size, 7)

    def test_setter(self):
        """The setter changes width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_setter_string(self):
        """A string size uses the width message."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_setter_float(self):
        """A float size is refused."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = 1.5

    def test_setter_zero(self):
        """A zero size is refused."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0

    def test_setter_negative(self):
        """A negative size is refused."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -3

    def test_init_string(self):
        """Validation happens at creation too."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_init_zero(self):
        """A zero size is refused at creation."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_validation_inherited(self):
        """x validation comes from Rectangle."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "1")

    def test_y_validation_inherited(self):
        """y validation comes from Rectangle."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 1, -1)


class TestSquareArea(unittest.TestCase):
    """Test the inherited area method."""

    def test_small(self):
        """A small square."""
        self.assertEqual(Square(5).area(), 25)

    def test_one(self):
        """The smallest square."""
        self.assertEqual(Square(1).area(), 1)

    def test_after_resize(self):
        """The area follows the size."""
        s = Square(5)
        s.size = 3
        self.assertEqual(s.area(), 9)


class TestSquareDisplay(unittest.TestCase):
    """Test the inherited display method."""

    def capture(self, square):
        """Return what a square prints."""
        captured = io.StringIO()
        sys.stdout = captured
        square.display()
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_simple(self):
        """A square with no offset."""
        self.assertEqual(self.capture(Square(2)), "##\n##\n")

    def test_with_x(self):
        """x adds leading spaces."""
        self.assertEqual(self.capture(Square(2, 2)), "  ##\n  ##\n")

    def test_with_x_and_y(self):
        """x and y are combined."""
        self.assertEqual(self.capture(Square(3, 1, 3)),
                         "\n\n\n ###\n ###\n ###\n")


class TestSquareStr(unittest.TestCase):
    """Test the __str__ method."""

    def test_full(self):
        """Every attribute appears."""
        self.assertEqual(str(Square(10, 2, 1, 7)), "[Square] (7) 2/1 - 10")

    def test_defaults(self):
        """Default x and y appear as zero."""
        Base._Base__nb_objects = 0
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")

    def test_after_resize(self):
        """The string follows the size."""
        s = Square(5, 0, 0, 1)
        s.size = 8
        self.assertEqual(str(s), "[Square] (1) 0/0 - 8")


class TestSquareUpdate(unittest.TestCase):
    """Test the update method."""

    def test_no_args_changes_nothing(self):
        """Calling update with nothing leaves the object alone."""
        s = Square(5, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_args_id(self):
        """The first positional argument is the id."""
        s = Square(5, 0, 0, 1)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")

    def test_args_size(self):
        """The second positional argument is the size."""
        s = Square(5, 0, 0, 1)
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")

    def test_args_all(self):
        """Every positional argument is applied in order."""
        s = Square(5, 0, 0, 1)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_args_extra_ignored(self):
        """Extra positional arguments are ignored."""
        s = Square(5, 0, 0, 1)
        s.update(1, 2, 3, 4, 5)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_args_validation(self):
        """Positional arguments are still validated."""
        s = Square(5, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, "invalid")

    def test_kwargs(self):
        """Keyword arguments update by name."""
        s = Square(5, 0, 0, 1)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")

    def test_kwargs_many(self):
        """Several keyword arguments are applied."""
        s = Square(5, 0, 0, 1)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_kwargs_skipped_when_args(self):
        """Keyword arguments are ignored when args are given."""
        s = Square(5, 0, 0, 1)
        s.update(1, 2, size=100)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")

    def test_kwargs_validation(self):
        """Keyword arguments are still validated."""
        s = Square(5, 0, 0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)


class TestSquareToDictionary(unittest.TestCase):
    """Test the to_dictionary method."""

    def test_type(self):
        """The result is a dictionary."""
        self.assertEqual(type(Square(10, 2, 1, 7).to_dictionary()), dict)

    def test_keys(self):
        """Every expected key is present."""
        d = Square(10, 2, 1, 7).to_dictionary()
        self.assertEqual(sorted(d.keys()), ["id", "size", "x", "y"])

    def test_values(self):
        """Every value is correct."""
        d = Square(10, 2, 1, 7).to_dictionary()
        self.assertEqual(d, {"id": 7, "size": 10, "x": 2, "y": 1})

    def test_no_width_or_height(self):
        """Width and height are not part of the dictionary."""
        d = Square(10, 2, 1, 7).to_dictionary()
        self.assertNotIn("width", d)
        self.assertNotIn("height", d)

    def test_used_by_update(self):
        """The dictionary can rebuild another square."""
        s1 = Square(10, 2, 1, 7)
        s2 = Square(1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))

    def test_no_args(self):
        """to_dictionary takes no argument."""
        with self.assertRaises(TypeError):
            Square(1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
