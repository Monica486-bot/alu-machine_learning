#!/usr/bin/env python3
"""Module for Exponential distribution."""


class Exponential:
    """Represents an Exponential distribution."""

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """Initialize Exponential distribution."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(1 / (sum(data) / len(data)))

    def pdf(self, x):
        """Calculate PDF for time period x."""
        if x < 0:
            return 0
        return self.lambtha * (self.e ** (-self.lambtha * x))

    def cdf(self, x):
        """Calculate CDF for time period x."""
        if x < 0:
            return 0
        return 1 - (self.e ** (-self.lambtha * x))
