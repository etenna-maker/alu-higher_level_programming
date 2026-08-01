#!/usr/bin/python3
"""Defines a class Student with reload_from_json."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance."""
        if type(attrs) is list and all(type(a) is str for a in attrs):
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student with values from json."""
        for key, value in json.items():
            setattr(self, key, value)
