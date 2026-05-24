#!/usr/bin/env python3
"""Module for calculating the minor matrix of a matrix."""
determinant = __import__('0-determinant').determinant


def minor(matrix):
    """Calculate and return the minor matrix of a matrix."""
    if not isinstance(matrix, list) or not all(
            isinstance(r, list) for r in matrix):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(r) != n for r in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if n == 1:
        return [[1]]
    return [[determinant([[matrix[i][k] for k in range(n) if k != j]
                          for i in range(n) if i != row])
             for j in range(n)]
            for row in range(n)]
