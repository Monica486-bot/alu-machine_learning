#!/usr/bin/env python3
"""Module for calculating the sum of i squared from 1 to n."""


def summation_i_squared(n):
    """Calculate sum of i^2 for i=1 to n using closed-form formula."""
    if not isinstance(n, (int, float)) or isinstance(n, bool) or n < 1:
        return None
    n = int(n)
    return n * (n + 1) * (2 * n + 1) // 6
