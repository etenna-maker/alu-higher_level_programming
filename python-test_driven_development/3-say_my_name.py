#!/usr/bin/python3
"""This module defines a function that prints a person's full name.

say_my_name(first_name, last_name) prints a greeting built from
the two names given. Both must be strings, last name is optional.
"""


def say_my_name(first_name, last_name=""):
    """Print "My name is <first_name> <last_name>".

    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
