#!/usr/bin/env python3
"""Module for slicing a numpy.ndarray along specific axes."""


def np_slice(matrix, axes={}):
    """Slice matrix along specified axes; axes maps axis index to slice tuple."""
    slices = [slice(*axes[i]) if i in axes else slice(None)
              for i in range(matrix.ndim)]
    return matrix[tuple(slices)]
