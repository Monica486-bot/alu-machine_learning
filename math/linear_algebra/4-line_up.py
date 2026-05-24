#!/usr/bin/env python3
"""Module for element-wise addition of two arrays."""


def add_arrays(arr1, arr2):
    """Add two arrays element-wise; return None if shapes differ."""
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
