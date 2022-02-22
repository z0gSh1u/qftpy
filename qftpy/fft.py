'''
    Fast (Discrete) Quaternion Fourier Transforms (1D and 2D) and inverse.

    by z0gSh1u @ github.com/z0gSh1u/qftpy
'''

__all__ = ['qfft', 'iqfft', 'qfft2', 'iqfft2', 'qfftshift', 'iqfftshift']

import numpy as np
import quaternion
from .utils import unit, _ortho, _orthoNormalBasis, _transformBasis, ALL_ONE_AXIS


def _qft1d(_name, _func, seq, axis, side='L', N=None):
    '''
        Since Fourier Transform is orthogonal, we can unify forward and inverse together.
    '''
    assert side == 'L' or side == 'R', 'Invalid side `{}` for {}.'.format(side, _name)
    sideFactor = -1 if side == 'R' else 1
    axis = unit(axis)

    # Project the quaternions onto a set of new basis.
    newBasis = _orthoNormalBasis(axis)
    newSeq = [_transformBasis(x, newBasis) for x in seq]
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
    ans = np.array([_transformBasis(x, newBasis.T) for x in ans])

    return ans


def _qft2d(_name, _func, mat, axis, side='L', N=None):
    '''
        Since Fourier Transform is orthogonal, we can unify forward and inverse together.
    '''
    assert side == 'L' or side == 'R' or side == 'D', 'Invalid side `{}` for {}.'.format(side, _name)
    sideFactor = -1 if side == 'R' else 1  # use 1 for two-sided
    axis = unit(axis)

    # Project the quaternions onto a set of new basis.
    newBasis = _orthoNormalBasis(axis)

    h, w = mat.shape
    mat = mat.flatten()
    newMat = [_transformBasis(x, newBasis) for x in mat]

    # Construct sub-sequence according to real-imag decomposition rule.
    subMat1 = np.array([complex(v.w, v.x) for v in newMat]).reshape((h, w))
    subMat2 = np.array([complex(v.y, v.z) for v in newMat]).reshape((h, w))

    # Perform regular FFT / IFFT.
    F1 = _func(subMat1).flatten()
    F2 = _func(subMat2).flatten()

    # Rearrange the result.
    ans = np.array([np.quaternion(f1.real, f1.imag, f2.real, sideFactor * f2.imag) for (f1, f2) in zip(F1, F2)],
                   dtype=np.quaternion)
    # Project back.
    ans = np.array([_transformBasis(x, newBasis.T) for x in ans])
    ans = ans.reshape((h, w))

    return ans


def qfft(seq, axis=ALL_ONE_AXIS, side='L', N=None):
    '''
        Perform `N`-dot (`None` to auto determine) 1D Fast (Discrete) Quaternion Fourier Transform on \\
        quaternion array `seq` with respect to transform `axis` using the `side` ('L' or 'R') -sided formula.
    '''
    return _qft1d(qfft.__name__, np.fft.fft, seq, axis, side, N)


def iqfft(seq, axis=ALL_ONE_AXIS, side='L', N=None):
    '''
        Perform `N`-dot (`None` to auto determine) 1D Inverse Fast (Discrete) Quaternion Fourier Transform on \\
        quaternion array `seq` with respect to transform `axis` using the `side` ('L' or 'R') -sided formula.
    '''
    return _qft1d(iqfft.__name__, np.fft.ifft, seq, axis, side, N)


def qfft2(mat, axis=ALL_ONE_AXIS, side='L'):
    '''
        Perform 2D Fast (Discrete) Quaternion Fourier Transform on matrix `mat` with respect to transform `axis` \\
        using the `side` [ 'L', 'R' or 'D'(ual) ]-sided formula.
    '''
    return _qft2d(qfft2.__name__, np.fft.fft2, mat, axis, side)


def iqfft2(mat, axis=ALL_ONE_AXIS, side='L'):
    '''
        Perform 2D Inverse Fast (Discrete) Quaternion Fourier Transform on matrix `mat` \\
            with respect to transform `axis` using the `side` [ 'L', 'R' or 'D'(ual) ]-sided formula.
    '''
    return _qft2d(iqfft2.__name__, np.fft.ifft2, mat, axis, side)


def qfftshift(x):
    '''
        Shift DC (lowest frequency) component to the center.
    '''
    return np.fft.fftshift(x)


def iqfftshift(x):
    '''
        Inverse of `qfftshift`.
    '''
    return np.fft.ifftshift(x)