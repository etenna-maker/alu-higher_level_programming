#!/usr/bin/python3
"""This module supplies one function, text_indentation.

text_indentation(text) prints a text and adds two new lines
after each of the characters ., ? and :, removing any spaces
at the beginning and the end of every printed line.
"""


def text_indentation(text):
    """Print text with two new lines after each of ., ? and :.

    text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
