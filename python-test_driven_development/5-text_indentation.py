#!/usr/bin/python3
"""This module defines a function that indents text.

text_indentation(text) prints a text and adds two new lines
after each of the characters ., ? and :, with no space at the
beginning or the end of any printed line.
"""


def text_indentation(text):
    """Print text with two new lines after each of ., ? and :.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
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
