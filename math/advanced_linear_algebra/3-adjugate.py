#!/usr/bin/env python3
"""Module for calculating the adjugate matrix of a matrix."""
cofactor = __import__('2-cofactor').cofactor


def adjugate(matrix):
    """Calculate and return the adjugate matrix of a matrix."""
    if not isinstance(matrix, list) or not all(
            isinstance(r, list) for r in matrix):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(r) != n for r in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    c = cofactor(matrix)
    return [[c[j][i] for j in range(n)] for i in range(n)]
