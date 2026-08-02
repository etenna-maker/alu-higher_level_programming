#!/usr/bin/python3
"""This module supplies one function, matrix_divided.

matrix_divided(matrix, div) divides every element of a matrix
by a number and returns a new matrix with the results rounded
to two decimal places. The original matrix is left unchanged.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Returns a new matrix rounded to 2 decimal places.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(err)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(err)
        for element in row:
            if not isinstance(element, (int, float)) or \
                    isinstance(element, bool):
                raise TypeError(err)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
