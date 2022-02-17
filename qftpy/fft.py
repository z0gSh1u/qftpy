'''
    Fast (Discrete) Quaternion Fourier Transforms (1D and 2D) and inverse.

    by z0gSh1u @ github.com/z0gSh1u/qftpy
'''

import numpy as np
from .utils import *

fft2 = np.fft.fft2
ifft2 = np.fft.ifft2
fftshift = np.fft.fftshift
ifftshift = np.fft.ifftshift


def _qft1d(_name, _func, seq, axis, side='L', N=None):
    '''
        Since Fourier Transform is orthogonal, we can unify forward and inverse together.
    '''
    assert side == 'L' or side == 'R', 'Invalid side `{}` for {}.'.format(side, _name)
    sideFactor = 1 if side == 'L' else -1
    axis = unit(axis)

    # Project the quaternions onto a set of new basis.
    newBasis = orthoNormalBasis(axis)
    newSeq = [transformBasis(x, newBasis) for x in seq]
    # Construct sub-sequence according to real-imag decomposition rule.
    subSeq1 = np.array([complex(v.w, v.x) for v in newSeq])
    subSeq2 = np.array([complex(v.y, v.z) for v in newSeq])
    # Perform regular FFT / IFFT.
    F1 = _func(subSeq1, n=N)
    F2 = _func(subSeq2, n=N)

    # Rearrange the result.
    ans = np.array([np.quaternion(f1.real, f1.imag, f2.real, sideFactor * f2.imag) for (f1, f2) in zip(F1, F2)],
                   dtype=np.quaternion)
    # Project back.
    ans = np.array([transformBasis(x, newBasis.T) for x in ans])

    return ans


def qfft(seq, axis, side='L', N=None):
    '''
        Perform `N`-dot (`None` to auto determine) 1D Fast (Discrete) Quaternion Fourier Transform on 
        quaternion array `seq` with respect to transform axis `axis` using the `side` ('L' or 'R') -sided formula.
    '''
    return _qft1d(qfft.__name__, np.fft.fft, seq, axis, side, N)


def iqfft(seq, axis, side='L', N=None):
    '''
        Perform `N`-dot (`None` to auto determine) 1D Inverse Fast (Discrete) Quaternion Fourier Transform on 
        quaternion array `seq` with respect to transform axis `axis` using the `side` ('L' or 'R') -sided formula.
    '''
    return _qft1d(iqfft.__name__, np.fft.ifft, seq, axis, side, N)


def qfft2(seq, axis, side='L', N=None):
    # TODO

    assert side == 'L' or side == 'R', 'Invalid side `{}` for {}.'.format(side, 'qfft2')
    sideFactor = 1 if side == 'L' else -1
    axis = unit(axis)

    # Project the quaternions onto a set of new basis.
    newBasis = orthoNormalBasis(axis)
    newSeq = [transformBasis(x, newBasis) for x in seq]
    # Construct sub-sequence according to real-imag decomposition rule.
    subSeq1 = np.array([complex(v.w, v.x) for v in newSeq])
    subSeq2 = np.array([complex(v.y, v.z) for v in newSeq])
    # Perform regular FFT / IFFT.
    F1 = fft2(subSeq1, n=N)
    F2 = fft2(subSeq2, n=N)

    # Rearrange the result.
    ans = np.array([np.quaternion(f1.real, f1.imag, f2.real, sideFactor * f2.imag) for (f1, f2) in zip(F1, F2)],
                   dtype=np.quaternion)
    # Project back.
    ans = np.array([transformBasis(x, newBasis.T) for x in ans])

    return ans


def iqfft2():
    pass


def qfftshift(x):
    return fftshift(x)


def iqfftshift(x):
    return ifftshift(x)