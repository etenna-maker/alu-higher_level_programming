#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file and return chars written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
