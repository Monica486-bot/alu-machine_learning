#!/usr/bin/env python3
"""Module for calculating the adjugate matrix of a matrix."""


def _det(matrix):
    """Calculate the determinant of a matrix (internal helper)."""
    if matrix == [[]]:
        return 1
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(n):
        sub = [[matrix[i][k] for k in range(n) if k != j]
               for i in range(1, n)]
        det += ((-1) ** j) * matrix[0][j] * _det(sub)
    return det


def adjugate(matrix):
    """Calculate and return the adjugate matrix of a matrix."""
    if not isinstance(matrix, list) or not all(
            isinstance(r, list) for r in matrix):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(r) != n for r in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if n == 1:
        return [[1]]
    cofactor = [[_det([[matrix[i][k] for k in range(n) if k != j]
                       for i in range(n) if i != row]) * ((-1) ** (row + j))
                 for j in range(n)]
                for row in range(n)]
    return [[cofactor[j][i] for j in range(n)] for i in range(n)]
