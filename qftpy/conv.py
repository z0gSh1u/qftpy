'''
    Quaternion convolution (1D and 2D).

    by z0gSh1u @ github.com/z0gSh1u/qftpy
'''

__all__ = ['conv', 'conv2']

import numpy as np
import quaternion


def conv(A, kL=None, kR=None):
    """
        Perform 1D linear convolution <kL, A, kR> on quaternion sequences. \\
        Keep a certain kernel `None` to perform one-sided convolution, or provide
        both for two-sided one. \\
        The length of kernels cannot be longer than `A`. \\
        The right-sided result is the conjugation of the left-sided one actually.
    """
    assert len(A.shape) == 1, 'A should be 1D sequence.'
    assert any([kL is not None, kR is not None]), 'kL and kR are both None.'

    # Use unit 1 for None parameters
    if kL is None:
        kL = np.ones_like(kR, dtype=np.quaternion)
    if kR is None:
        kR = np.ones_like(kL, dtype=np.quaternion)

    assert len(kL.shape) == 1 and len(kR.shape) == 1, 'kL and kR should be 1D sequence.'
    assert len(kL) == len(kR), 'kL and kR should have same length.'

    m = len(kL)
    n = len(A)
    assert m <= n, 'kL and kR cannot be longer than A.'

    # Perform convolution.
    res = np.zeros((m + n - 1), dtype=np.quaternion)
    for i in range(0, m):
        res[i:i + n] += kL[i] * A * kR[i]

    return res


def conv2(A, kL=None, kR=None, keepShape=False):
    """
        Perform 2D convolution <kL, A, kR> on quaternion matrices. \\
        Keep a certain kernel `None` to perform one-sided convolution, or provide
        both for two-sided one. \\
        The shape of kernels should not be larger than `A`. \\
        If `keepShape` is `True`, the output matrix will have same shape as `A`.
        Otherwise a little bigger with padding.
    """
    assert len(A.shape) == 2, 'A should be 2D matrix.'
    assert any([kL is not None, kR is not None]), 'kL and kR are both None.'

    # Use unit 1 for None parameters
    if kL is None:
        kL = np.ones_like(kR, dtype=np.quaternion)
    if kR is None:
        kR = np.ones_like(kL, dtype=np.quaternion)

    assert len(kL.shape) == 2 and len(kR.shape) == 2, 'kL and kR should be 2D sequence.'
    assert np.array_equal(kL.shape, kR.shape), 'kL and kR should have same shape.'

    M, N = A.shape  # source matrix is M*N
    m, n = kL.shape  # kernel is m*n

    assert m <= M and n <= N, 'kL and kR should not overlay A.'

    # Perform convolution.
    res = np.zeros((M + m - 1, N + n - 1), dtype=np.quaternion)
    for i in range(0, m):
        for j in range(0, n):
            res[i:i + M, j:j + N] += kL[i, j] * A * kR[i, j]

    if keepShape:
        res = res[m // 2:m // 2 + M, n // 2:n // 2 + N]

    return res