#!/usr/bin/env python3
"""Module for Binomial distribution."""


class Binomial:
    """Represents a Binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize Binomial distribution."""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            var = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - var / mean
            self.n = round(mean / p)
            self.p = float(mean / self.n)

    @staticmethod
    def _factorial(n):
        """Calculate factorial of n."""
        r = 1
        for i in range(1, n + 1):
            r *= i
        return r

    def pmf(self, k):
        """Calculate PMF for k successes."""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        c = (self._factorial(self.n)
             // (self._factorial(k) * self._factorial(self.n - k)))
        return c * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculate CDF for k successes."""
        k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(i) for i in range(k + 1))
