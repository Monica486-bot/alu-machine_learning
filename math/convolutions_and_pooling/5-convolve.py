#!/usr/bin/env python3
"""Module for convolution with multiple kernels."""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Perform convolution on images using multiple kernels."""
    m, h, w, c = images.shape
    kh, kw, _, nc = kernels.shape
    sh, sw = stride
    if padding == 'same':
        oh = int(np.ceil(h / sh))
        ow = int(np.ceil(w / sw))
        ph = max((oh - 1) * sh + kh - h, 0) // 2
        pw = max((ow - 1) * sw + kw - w, 0) // 2
    elif padding == 'valid':
        ph, pw = 0, 0
        oh = (h - kh) // sh + 1
        ow = (w - kw) // sw + 1
    else:
        ph, pw = padding
        oh = (h + 2 * ph - kh) // sh + 1
        ow = (w + 2 * pw - kw) // sw + 1
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)))
    output = np.zeros((m, oh, ow, nc))
    for i in range(oh):
        for j in range(ow):
            for k in range(nc):
                output[:, i, j, k] = np.sum(
                    padded[:, i*sh:i*sh+kh, j*sw:j*sw+kw, :] * kernels[
                        :, :, :, k],
                    axis=(1, 2, 3))
    return output
