#!/usr/bin/env python3
"""Module for calculating the cofactor matrix of a matrix."""
minor = __import__('1-minor').minor


def cofactor(matrix):
    """Calculate and return the cofactor matrix of a matrix."""
    if not isinstance(matrix, list) or not all(
            isinstance(r, list) for r in matrix):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(r) != n for r in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    m = minor(matrix)
    return [[m[i][j] * ((-1) ** (i + j)) for j in range(n)]
            for i in range(n)]
