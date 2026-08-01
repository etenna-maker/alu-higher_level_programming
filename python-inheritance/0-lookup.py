#!/usr/bin/python3
"""Defines a function that returns attributes and methods of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
