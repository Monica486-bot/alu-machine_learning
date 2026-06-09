#!/usr/bin/env python3
"""Module for Normal distribution."""


class Normal:
    """Represents a Normal distribution."""

    e = 2.718281828459045
    pi = 3.141592653589793

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize Normal distribution."""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            self.stddev = float(
                (sum((x - self.mean) ** 2 for x in data) / len(data)) ** 0.5
            )

    def z_score(self, x):
        """Calculate z-score of x."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate x-value of z-score."""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculate PDF for x-value."""
        coef = 1 / (self.stddev * (2 * self.pi) ** 0.5)
        exp = -0.5 * ((x - self.mean) / self.stddev) ** 2
        return coef * (self.e ** exp)

    def cdf(self, x):
        """Calculate CDF for x-value."""
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))
        erf = (2 / self.pi ** 0.5) * (
            z - z**3 / 3 + z**5 / 10 - z**7 / 42 + z**9 / 216
        )
        return 0.5 * (1 + erf)
