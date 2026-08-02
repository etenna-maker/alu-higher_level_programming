#!/usr/bin/python3
"""This module defines the Base class.

Base is the parent of every other class in this project. It manages
the id attribute of all instances and provides the serialization and
deserialization helpers shared by its subclasses.
"""
import csv
import json


class Base:
    """Represent the base class of all other classes in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of objects to a file."""
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as a_file:
            a_file.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as a_file:
                list_dicts = cls.from_json_string(a_file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of a list of objects to a file."""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as a_file:
            if list_objs is None or list_objs == []:
                a_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(a_file, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from a CSV file."""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline="") as a_file:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                reader = csv.DictReader(a_file, fieldnames=fields)
                list_dicts = [dict([key, int(value)] for key, value in
                              row.items()) for row in reader]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
