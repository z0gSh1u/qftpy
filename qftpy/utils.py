import numpy as np
import quaternion

EPS = np.finfo(np.float32).eps  # quaternion library internal uses float64. We relax epsilon to float32 here.
X_AXIS = np.quaternion(0, 1, 0, 0)
Y_AXIS = np.quaternion(0, 0, 1, 0)
Z_AXIS = np.quaternion(0, 0, 0, 1)


def unit(q):
    """
        Normalize q (a single quaternion or a quaternion matrix) to unit modulus (1).
    """
    len_ = np.abs(q)
    assert np.min(q) > EPS, 'The modulus of q is too short.'
    u = q / len_
    return u


def isPure(q):
    return abs(q.w) < EPS


def crossProduct(a, b):
    """
        Calculate the cross product (vector product, outer product) of two pure quaternions.
    """
    assert isPure(a) and isPure(b), 'a and b must be pure quaternions.'
    x = a.y * b.z - a.z * b.y
    y = a.z * b.x - a.x * b.z
    z = a.x * b.y - a.y * b.x
    return np.quaternion(0, x, y, z)


def isParallel(a, b):
    return crossProduct(a, b) < EPS


def ortho(v):
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
        # Now only two vectors (not parallel) is sufficient to consider.
        candidates = [np.quaternion(0, 1, 1, 1), np.quaternion(0, 1, 1, 0)]
        w = candidates[1] if isParallel(candidates[0], v) else candidates[0]
    # The cross product of (v, w) is right the answer.
    return unit(crossProduct(v, w))


def orthoNormalBasis(v):
    w = ortho(v)
    u = unit(crossProduct(v, w))
    return v, w, u

def changeBasis(q, B):
    v1 = np.quaternion(B[0, 0], B[0, 1], B[0, 2])
    v2 = np.quaternion(B[1, 0], B[1, 1], B[1, 2])
    v3 = np.quaternion(B[2, 0], B[2, 1], B[2, 2])
    x = crossProduct(q, v1)
    y = crossProduct(q, v2)
    z = crossProduct(q, v3)
    return np.quaternion(0, x, y, z)