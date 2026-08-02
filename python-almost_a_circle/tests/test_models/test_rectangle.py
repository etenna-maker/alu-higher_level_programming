#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Test the creation of Rectangle instances."""

    def test_is_base(self):
        """Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """Width and height are mandatory."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Height is mandatory."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        """Rectangle takes at most five arguments."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_two_args(self):
        """Width and height alone are enough."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_x_and_y(self):
        """x and y default to zero."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_all_args(self):
        """Every argument is assigned."""
        r = Rectangle(10, 2, 3, 4, 7)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (10, 2, 3, 4, 7))

    def test_ids_increment(self):
        """Ids increment when not given."""
        Base._Base__nb_objects = 0
        self.assertEqual(Rectangle(1, 1).id, 1)
        self.assertEqual(Rectangle(1, 1).id, 2)

    def test_width_is_private(self):
        """Width is stored privately."""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2).__width)

    def test_height_is_private(self):
        """Height is stored privately."""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2).__height)

    def test_x_is_private(self):
        """x is stored privately."""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2).__x)

    def test_y_is_private(self):
        """y is stored privately."""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2).__y)


class TestRectangleValidation(unittest.TestCase):
    """Test the validation done by the setters."""

    def test_width_string(self):
        """A string width is refused."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_width_float(self):
        """A float width is refused."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.5, 2)

    def test_width_none(self):
        """A None width is refused."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_width_list(self):
        """A list width is refused."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1], 2)

    def test_width_zero(self):
        """A zero width is refused."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        """A negative width is refused."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_string(self):
        """A string height is refused."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_height_float(self):
        """A float height is refused."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 1.5)

    def test_height_zero(self):
        """A zero height is refused."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative(self):
        """A negative height is refused."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_string(self):
        """A string x is refused."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3")

    def test_x_dict(self):
        """A dictionary x is refused."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_x_negative(self):
        """A negative x is refused."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)

    def test_x_zero_allowed(self):
        """A zero x is accepted."""
        self.assertEqual(Rectangle(10, 2, 0).x, 0)

    def test_y_string(self):
        """A string y is refused."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")

    def test_y_negative(self):
        """A negative y is refused."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_y_zero_allowed(self):
        """A zero y is accepted."""
        self.assertEqual(Rectangle(10, 2, 3, 0).y, 0)

    def test_setter_validates(self):
        """The setters validate after creation too."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10

    def test_width_before_height(self):
        """Width is validated before height."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", "2")


class TestRectangleArea(unittest.TestCase):
    """Test the area method."""

    def test_small(self):
        """A small rectangle."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_larger(self):
        """A larger rectangle."""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_one_by_one(self):
        """The smallest rectangle."""
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_changed(self):
        """The area follows the attributes."""
        r = Rectangle(2, 10)
        r.width = 5
        self.assertEqual(r.area(), 50)

    def test_no_args(self):
        """area takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Test the display method."""

    def capture(self, rectangle):
        """Return what a rectangle prints."""
        captured = io.StringIO()
        sys.stdout = captured
        rectangle.display()
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_simple(self):
        """A rectangle with no offset."""
        self.assertEqual(self.capture(Rectangle(2, 2)), "##\n##\n")

    def test_one_by_one(self):
        """The smallest rectangle."""
        self.assertEqual(self.capture(Rectangle(1, 1)), "#\n")

    def test_with_x(self):
        """x adds leading spaces."""
        self.assertEqual(self.capture(Rectangle(3, 2, 1, 0)),
                         " ###\n ###\n")

    def test_with_y(self):
        """y adds leading new lines."""
        self.assertEqual(self.capture(Rectangle(2, 2, 0, 1)),
                         "\n##\n##\n")

    def test_with_x_and_y(self):
        """x and y are combined."""
        self.assertEqual(self.capture(Rectangle(2, 3, 2, 2)),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_no_args(self):
        """display takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).display(1)


class TestRectangleStr(unittest.TestCase):
    """Test the __str__ method."""

    def test_full(self):
        """Every attribute appears."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_defaults(self):
        """Default x and y appear as zero."""
        Base._Base__nb_objects = 0
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")

    def test_changed(self):
        """The string follows the attributes."""
        r = Rectangle(4, 6, 2, 1, 12)
        r.width = 7
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 7/6")


class TestRectangleUpdate(unittest.TestCase):
    """Test the update method."""

    def test_no_args_changes_nothing(self):
        """Calling update with nothing leaves the object alone."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")

    def test_args_id(self):
        """The first positional argument is the id."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_args_width(self):
        """The second positional argument is the width."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_args_all(self):
        """Every positional argument is applied in order."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_args_extra_ignored(self):
        """Extra positional arguments are ignored."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_args_validation(self):
        """Positional arguments are still validated."""
        r = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_kwargs(self):
        """Keyword arguments update by name."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")

    def test_kwargs_many(self):
        """Several keyword arguments are applied."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_kwargs_skipped_when_args(self):
        """Keyword arguments are ignored when args are given."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, height=100)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_kwargs_validation(self):
        """Keyword arguments are still validated."""
        r = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)


class TestRectangleToDictionary(unittest.TestCase):
    """Test the to_dictionary method."""

    def test_type(self):
        """The result is a dictionary."""
        self.assertEqual(type(Rectangle(10, 2, 1, 9, 1).to_dictionary()),
                         dict)

    def test_keys(self):
        """Every expected key is present."""
        d = Rectangle(10, 2, 1, 9, 1).to_dictionary()
        self.assertEqual(sorted(d.keys()),
                         ["height", "id", "width", "x", "y"])

    def test_values(self):
        """Every value is correct."""
        d = Rectangle(10, 2, 1, 9, 1).to_dictionary()
        self.assertEqual(d, {"id": 1, "width": 10, "height": 2,
                             "x": 1, "y": 9})

    def test_used_by_update(self):
        """The dictionary can rebuild another rectangle."""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))

    def test_no_args(self):
        """to_dictionary takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
