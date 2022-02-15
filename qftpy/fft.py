import numpy as np
import quaternion
from utils import *

fft = np.fft.fft
fft2 = np.fft.fft2


def _fft():
    pass


def _ifft():
    pass


def qfft(seq, axis, side='L'):
    assert side == 'L' or side == 'R', 'Invalid side for qfft.'
    sideFactor = 1 if side == 'L' else -1
    axis = unit(axis)

    B = orthoNormalBasis(axis)
    X = changeBasis(X, B)

    # TODO build array
    # c1=fft(scalar(X) + x(X)j)
    # c2=fft(y(X) + Sz(X)j)
    # Y=quaternion(R1,I1,R2,I2)


def qfft2():
    pass


def iqfft():
    pass


def iqfft2():
    pass


def qfftshift(x):
    return np.fft.fftshift(x)


def iqfftshift(x):
    return np.fft.ifftshift(x)