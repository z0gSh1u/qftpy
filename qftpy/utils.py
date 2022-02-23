'''
    Utilities for QFTPy.
    
    by z0gSh1u @ github.com/z0gSh1u/qftpy
'''

__all__ = ['unit', 'isPure', 'isScalarQ', 'dotProduct', 'crossProduct', 'isParallel', 'qzeros', 'qones', 'ALL_ONE_AXIS']

import numpy as np
import quaternion

EPS = np.finfo(np.float32).eps  # quaternion library internal uses float64. We relax epsilon to float32 here.
X_AXIS = np.quaternion(0, 1, 0, 0)
Y_AXIS = np.quaternion(0, 0, 1, 0)
Z_AXIS = np.quaternion(0, 0, 0, 1)
ALL_ONE_AXIS = np.quaternion(0, 1, 1, 1)


def unit(q):
    '''
        Normalize q (a single quaternion or a quaternion matrix) to unit modulus (1).
    '''
    len_ = np.abs(q)
    assert np.min(len_) > EPS, 'The modulus of q is too short.'
    u = q / len_
    return u


def isPure(q):
    '''
        Test if q is a pure quaternion.
    '''
    return abs(q.w) < EPS


def isScalarQ(q):
    '''
        Test if q is a scalar quaternion (x, y, z ~ 0).
    '''
    return abs(q.x) < EPS and abs(q.y) < EPS and abs(q.z) < EPS


def dotProduct(a, b, scalar=False):
    '''
        Calculate the dot product (scalar product, inner product) of two quaternions. \\
        Set `scalar=True` to include scalar components (`w`).
    '''
    return a.x * b.x + a.y * b.y + a.z * b.z + (a.w * b.w if scalar else 0)


def crossProduct(a, b):
    '''
        Calculate the cross product (vector product, outer product) of two pure quaternions.
    '''
    assert isPure(a) and isPure(b), 'a and b must be pure quaternions.'
    x = a.y * b.z - a.z * b.y
    y = a.z * b.x - a.x * b.z
    z = a.x * b.y - a.y * b.x
    return np.quaternion(0, x, y, z)


def isParallel(a, b):
    '''
        Test if `a` and `b` (both pure) are parallel.
    '''
    return np.abs(crossProduct(a, b)) < EPS


def qzeros(shape):
    '''
        Create all zero array with `shape`.
    '''
    return np.zeros(shape, dtype=np.quaternion)


def qones(shape):
    '''
        Create all one array with `shape`.
    '''
    return np.ones(shape, dtype=np.quaternion)


def _ortho(v, unit_=True):
    '''
        Construct a vector prependicular to `v` (pure). \\
        Set `unit_=True` to get result with unit length.
    '''
    assert isPure(v), 'v must be a pure quaternion.'
    # We first choose a vector `w` which is not parallel to v.
    # Consider standard basis first.
    if isParallel(v, X_AXIS):
        w = -Z_AXIS
    elif isParallel(v, Y_AXIS):
        w = -X_AXIS
    elif isParallel(v, Z_AXIS):
        w = -Y_AXIS
    else:
        # Now two vectors (not parallel) are sufficient to consider.
        candidates = [np.quaternion(0, 1, 1, 1), np.quaternion(0, 1, 1, 0)]
        w = candidates[1] if isParallel(candidates[0], v) else candidates[0]

    ans = crossProduct(v, w)
    return unit(ans) if unit_ else ans


def _orthoNormalBasis(v):
    '''
        Construct a set of orthogonal normal basis with `v` being one axis. \\
        Returns the transformation matrix in row vector formation.
    '''
    v = unit(v)
    w = _ortho(v, unit_=True)
    u = unit(crossProduct(v, w))
    return np.array([[v.x, v.y, v.z], [w.x, w.y, w.z], [u.x, u.y, u.z]])


def _transformBasis(q, mat):
    '''
        Transform the vector part of `q` to a new basis defined by `mat` (row vector formation)
        with scalar component kept.
    '''
    x, y, z = [dotProduct(q, np.quaternion(0, *mat[i, :])) for i in range(3)]
    return np.quaternion(q.w, x, y, z)