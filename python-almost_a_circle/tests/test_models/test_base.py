#!/usr/bin/python3
"""Unittests for the Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Test the creation of Base instances and their ids."""

    def setUp(self):
        """Reset the private object counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_increments(self):
        """Ids increment when no id is given."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

    def test_id_given(self):
        """A given id is used as is."""
        self.assertEqual(Base(12).id, 12)

    def test_id_given_does_not_increment(self):
        """A given id does not disturb the counter."""
        Base()
        Base(89)
        self.assertEqual(Base().id, 2)

    def test_id_none(self):
        """Passing None falls back to the counter."""
        self.assertEqual(Base(None).id, 1)

    def test_id_negative(self):
        """Negative ids are accepted."""
        self.assertEqual(Base(-7).id, -7)

    def test_id_zero(self):
        """Zero is a valid id."""
        self.assertEqual(Base(0).id, 0)

    def test_id_string(self):
        """A string id is stored unchanged."""
        self.assertEqual(Base("hello").id, "hello")

    def test_no_nb_objects_attribute(self):
        """The object counter stays private."""
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects)

    def test_two_args(self):
        """Base takes at most one argument."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Test the to_json_string static method."""

    def test_none(self):
        """None becomes an empty list string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """An empty list becomes an empty list string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_returns_string(self):
        """The result is always a string."""
        self.assertEqual(type(Base.to_json_string([{"a": 1}])), str)

    def test_one_dictionary(self):
        """A single dictionary is serialized."""
        result = Base.to_json_string([{"id": 9}])
        self.assertEqual(result, '[{"id": 9}]')

    def test_two_dictionaries(self):
        """Two dictionaries produce a list of length two."""
        result = Base.to_json_string([{"id": 1}, {"id": 2}])
        self.assertEqual(len(Base.from_json_string(result)), 2)

    def test_no_args(self):
        """The method requires an argument."""
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestBaseFromJsonString(unittest.TestCase):
    """Test the from_json_string static method."""

    def test_none(self):
        """None becomes an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string becomes an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_returns_list(self):
        """The result is always a list."""
        self.assertEqual(type(Base.from_json_string('[{"id": 1}]')), list)

    def test_one_dictionary(self):
        """A single dictionary is deserialized."""
        result = Base.from_json_string('[{"id": 9}]')
        self.assertEqual(result, [{"id": 9}])

    def test_no_args(self):
        """The method requires an argument."""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestBaseSaveToFile(unittest.TestCase):
    """Test the save_to_file class method."""

    def tearDown(self):
        """Remove any files created by the tests."""
        for name in ["Rectangle.json", "Square.json", "Base.json"]:
            try:
                os.remove(name)
            except IOError:
                pass
            except OSError:
                pass

    def test_none(self):
        """Saving None writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_empty_list(self):
        """Saving an empty list writes an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_one_rectangle(self):
        """A rectangle is written to Rectangle.json."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        with open("Rectangle.json", "r") as a_file:
            self.assertTrue(len(a_file.read()) > 2)

    def test_one_square(self):
        """A square is written to Square.json."""
        Square.save_to_file([Square(10, 2, 8, 1)])
        with open("Square.json", "r") as a_file:
            self.assertTrue(len(a_file.read()) > 2)

    def test_overwrites(self):
        """Saving twice overwrites the file."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_no_args(self):
        """The method requires an argument."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestBaseCreate(unittest.TestCase):
    """Test the create class method."""

    def test_rectangle(self):
        """A rectangle is rebuilt from its dictionary."""
        r1 = Rectangle(3, 5, 1, 0, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))

    def test_rectangle_is_new_object(self):
        """The created rectangle is a different object."""
        r1 = Rectangle(3, 5, 1, 0, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)

    def test_square(self):
        """A square is rebuilt from its dictionary."""
        s1 = Square(3, 5, 1, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))

    def test_square_is_new_object(self):
        """The created square is a different object."""
        s1 = Square(3, 5, 1, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsNot(s1, s2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Test the load_from_file class method."""

    def tearDown(self):
        """Remove any files created by the tests."""
        for name in ["Rectangle.json", "Square.json"]:
            try:
                os.remove(name)
            except IOError:
                pass
            except OSError:
                pass

    def test_no_file(self):
        """A missing file gives an empty list."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        except OSError:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_returns_list(self):
        """The result is a list."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        self.assertEqual(type(Rectangle.load_from_file()), list)

    def test_rectangle_types(self):
        """Loaded rectangles are Rectangle instances."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        for item in Rectangle.load_from_file():
            self.assertIsInstance(item, Rectangle)

    def test_square_types(self):
        """Loaded squares are Square instances."""
        Square.save_to_file([Square(10, 2, 8, 1)])
        for item in Square.load_from_file():
            self.assertIsInstance(item, Square)

    def test_round_trip(self):
        """Saved and loaded rectangles match."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        self.assertEqual(str(Rectangle.load_from_file()[0]), str(r1))


if __name__ == "__main__":
    unittest.main()
