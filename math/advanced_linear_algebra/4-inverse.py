#!/usr/bin/env python3
"""Module for calculating the inverse of a matrix."""
adjugate = __import__('3-adjugate').adjugate
determinant = __import__('0-determinant').determinant


def inverse(matrix):
    """Calculate and return the inverse of a matrix, or None if singular."""
    if not isinstance(matrix, list) or not all(
            isinstance(r, list) for r in matrix):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(r) != n for r in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    det = determinant(matrix)
    if det == 0:
        return None
    adj = adjugate(matrix)
    return [[adj[i][j] / det for j in range(n)] for i in range(n)]
