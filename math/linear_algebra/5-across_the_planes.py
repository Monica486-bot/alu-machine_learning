#!/usr/bin/env python3
"""Module for element-wise addition of two 2D matrices."""


def add_matrices2D(mat1, mat2):
    """Add two 2D matrices element-wise; return None if shapes differ."""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(mat1, mat2)]
