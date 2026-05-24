#!/usr/bin/env python3
"""Module for concatenating two matrices along a specific axis."""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenate two matrices along axis; return None if incompatible."""
    if axis == 0:
        if isinstance(mat1[0], list) and len(mat1[0]) != len(mat2[0]):
            return None
        if not isinstance(mat1[0], list) and not isinstance(mat2[0], list):
            return mat1 + mat2
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    if len(mat1) != len(mat2):
        return None
    result = [cat_matrices(r1, r2, axis - 1) for r1, r2 in zip(mat1, mat2)]
    if any(r is None for r in result):
        return None
    return result
