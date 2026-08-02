#!/usr/bin/python3
"""Unittests checking documentation and style across the project."""
import unittest
import models.base
import models.rectangle
import models.square
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestModuleDocs(unittest.TestCase):
    """Check that every module carries a real docstring."""

    def test_base_module(self):
        """The base module is documented."""
        self.assertTrue(len(models.base.__doc__) > 20)

    def test_rectangle_module(self):
        """The rectangle module is documented."""
        self.assertTrue(len(models.rectangle.__doc__) > 20)

    def test_square_module(self):
        """The square module is documented."""
        self.assertTrue(len(models.square.__doc__) > 20)


class TestClassDocs(unittest.TestCase):
    """Check that every class carries a real docstring."""

    def test_base_class(self):
        """The Base class is documented."""
        self.assertTrue(len(Base.__doc__) > 20)

    def test_rectangle_class(self):
        """The Rectangle class is documented."""
        self.assertTrue(len(Rectangle.__doc__) > 20)

    def test_square_class(self):
        """The Square class is documented."""
        self.assertTrue(len(Square.__doc__) > 20)


class TestBaseMethodDocs(unittest.TestCase):
    """Check that every Base method carries a docstring."""

    def test_init(self):
        """The constructor is documented."""
        self.assertTrue(len(Base.__init__.__doc__) > 20)

    def test_to_json_string(self):
        """to_json_string is documented."""
        self.assertTrue(len(Base.to_json_string.__doc__) > 20)

    def test_from_json_string(self):
        """from_json_string is documented."""
        self.assertTrue(len(Base.from_json_string.__doc__) > 20)

    def test_save_to_file(self):
        """save_to_file is documented."""
        self.assertTrue(len(Base.save_to_file.__doc__) > 20)

    def test_create(self):
        """create is documented."""
        self.assertTrue(len(Base.create.__doc__) > 20)

    def test_load_from_file(self):
        """load_from_file is documented."""
        self.assertTrue(len(Base.load_from_file.__doc__) > 20)


class TestRectangleMethodDocs(unittest.TestCase):
    """Check that every Rectangle method carries a docstring."""

    def test_init(self):
        """The constructor is documented."""
        self.assertTrue(len(Rectangle.__init__.__doc__) > 20)

    def test_area(self):
        """area is documented."""
        self.assertTrue(len(Rectangle.area.__doc__) > 20)

    def test_display(self):
        """display is documented."""
        self.assertTrue(len(Rectangle.display.__doc__) > 20)

    def test_update(self):
        """update is documented."""
        self.assertTrue(len(Rectangle.update.__doc__) > 20)

    def test_to_dictionary(self):
        """to_dictionary is documented."""
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 20)

    def test_str(self):
        """__str__ is documented."""
        self.assertTrue(len(Rectangle.__str__.__doc__) > 20)


class TestSquareMethodDocs(unittest.TestCase):
    """Check that every Square method carries a docstring."""

    def test_init(self):
        """The constructor is documented."""
        self.assertTrue(len(Square.__init__.__doc__) > 20)

    def test_update(self):
        """update is documented."""
        self.assertTrue(len(Square.update.__doc__) > 20)

    def test_to_dictionary(self):
        """to_dictionary is documented."""
        self.assertTrue(len(Square.to_dictionary.__doc__) > 20)

    def test_str(self):
        """__str__ is documented."""
        self.assertTrue(len(Square.__str__.__doc__) > 20)


class TestPep8(unittest.TestCase):
    """Check that the project follows the pycodestyle rules."""

    def check(self, path):
        """Return the number of style errors found in a file."""
        try:
            import pycodestyle
        except ImportError:
            self.skipTest("pycodestyle is not installed")
        style = pycodestyle.StyleGuide(quiet=True)
        return style.check_files([path]).total_errors

    def test_base(self):
        """models/base.py is style clean."""
        self.assertEqual(self.check("models/base.py"), 0)

    def test_rectangle(self):
        """models/rectangle.py is style clean."""
        self.assertEqual(self.check("models/rectangle.py"), 0)

    def test_square(self):
        """models/square.py is style clean."""
        self.assertEqual(self.check("models/square.py"), 0)


if __name__ == "__main__":
    unittest.main()
