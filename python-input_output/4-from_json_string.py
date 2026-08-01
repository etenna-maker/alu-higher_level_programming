#!/usr/bin/python3
"""Defines a function that returns an object from a JSON string."""
import json


def from_json_string(my_str):
    """Return a Python data structure represented by a JSON string."""
    return json.loads(my_str)
