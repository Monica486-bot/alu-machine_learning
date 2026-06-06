#!/usr/bin/env python3
"""Module for calculating the derivative of a polynomial."""


def poly_derivative(poly):
    """Calculate the derivative of a polynomial represented as a list."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    result = [i * poly[i] for i in range(1, len(poly))]
    return result if result else [0]
