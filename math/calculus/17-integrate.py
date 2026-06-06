#!/usr/bin/env python3
"""Module for calculating the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Calculate the integral of a polynomial represented as a list."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, (int, float)):
        return None
    result = [C]
    for i, coef in enumerate(poly):
        if not isinstance(coef, (int, float)):
            return None
        val = coef / (i + 1)
        result.append(int(val) if val == int(val) else val)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result
