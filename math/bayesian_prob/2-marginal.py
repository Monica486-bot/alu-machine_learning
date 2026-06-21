#!/usr/bin/env python3
"""Module for calculating marginal probability."""
import numpy as np
intersection = __import__('1-intersection').intersection


def marginal(x, n, P, Pr):
    """Calculate marginal probability of obtaining x and n."""
    return np.sum(intersection(x, n, P, Pr))
