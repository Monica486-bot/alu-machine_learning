#!/usr/bin/env python3
"""Module for convolution on images with channels."""
import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """Perform convolution on images with channels."""
    m, h, w, c = images.shape
    kh, kw, _ = kernel.shape
    sh, sw = stride
    if padding == 'same':
        ph = max((h - 1) * sh + kh - h, 0) // 2
        pw = max((w - 1) * sw + kw - w, 0) // 2
        oh, ow = h, w
    elif padding == 'valid':
        ph, pw = 0, 0
        oh = (h - kh) // sh + 1
        ow = (w - kw) // sw + 1
    else:
        ph, pw = padding
        oh = (h + 2 * ph - kh) // sh + 1
        ow = (w + 2 * pw - kw) // sw + 1
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)))
    output = np.zeros((m, oh, ow))
    for i in range(oh):
        for j in range(ow):
            output[:, i, j] = np.sum(
                padded[:, i*sh:i*sh+kh, j*sw:j*sw+kw, :] * kernel,
                axis=(1, 2, 3))
    return output
