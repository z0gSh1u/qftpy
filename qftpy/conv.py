'''
    Quaternion convolution (1D and 2D).

    by z0gSh1u @ github.com/z0gSh1u/qftpy
'''

import numpy as np
import quaternion

def conv(A, kL=None, kR=None):
    # TODO scalar

    assert len(A.shape) == 1, 'A should be 1D sequence.'
    assert len(kL.shape) == 1 and len(kR.shape) == 1, 'kL and kR should be 1D sequence.'
    assert len(kL) == len(kR), 'kL and kR should have same length.'

    m = len(kL)
    n = len(A)
    res = np.zeros((m + n - 1), dtype=np.quaternion)

    if m < n:
        for i in range(0, m - 1):
            res[i : i + n - 1] += kL[i] * A * kR[i]
    else:
        assert False

    return res

def conv2(A, kL=None, kR=None):
    pass