#!/usr/bin/env python3
"""Module for Multivariate Normal distribution."""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initialize MultiNormal from data of shape (d, n)."""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1, keepdims=True)
        diff = data - self.mean
        self.cov = np.dot(diff, diff.T) / (n - 1)

    def pdf(self, x):
        """Calculate PDF at data point x of shape (d, 1)."""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.mean.shape[0]
        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))
        diff = x - self.mean
        cov_inv = np.linalg.inv(self.cov)
        cov_det = np.linalg.det(self.cov)
        coef = 1 / np.sqrt(((2 * np.pi) ** d) * cov_det)
        exp = np.exp(-0.5 * np.dot(np.dot(diff.T, cov_inv), diff)[0, 0])
        return float(coef * exp)
