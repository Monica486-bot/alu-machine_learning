#!/usr/bin/env python3
"""Module for calculating posterior probability."""
import numpy as np
intersection = __import__('1-intersection').intersection
marginal = __import__('2-marginal').marginal


def posterior(x, n, P, Pr):
    """Calculate posterior probability for each p in P given x and n."""
    return intersection(x, n, P, Pr) / marginal(x, n, P, Pr)
