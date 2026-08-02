#!/usr/bin/python3
"""This module supplies one function, say_my_name.

say_my_name(first_name, last_name) prints a greeting built
from the two names it is given. Both names must be strings,
and the last name is optional.
"""


def say_my_name(first_name, last_name=""):
    """Print "My name is <first name> <last name>".

    Both arguments must be strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
