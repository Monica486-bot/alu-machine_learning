#!/usr/bin/env python3
"""Module for adding two matrices of any dimension element-wise."""


def add_matrices(mat1, mat2):
    """Add two matrices element-wise; return None if shapes differ."""
    if isinstance(mat1, list):
        if len(mat1) != len(mat2):
            return None
        result = [add_matrices(a, b) for a, b in zip(mat1, mat2)]
        if any(r is None for r in result):
            return None
        return result
    return mat1 + mat2
