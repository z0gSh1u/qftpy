# import unittest
# import quaternion

# import sys

# sys.path.append('../')

# from qftpy.conv import conv, conv2

# kl = [0, 1, 1, 1, 0, 3, 3, 3]
# sig = [0, 1.5, 2.5, 3.5, 0, 2, 3, 4, 0, 3, 3, 3]  # , 0, 3, 3, 3
# kr = [0, -1, -0.5, -1, 0, 1, 1, 1]

# import numpy as np

# kl = np.array([
#     [np.quaternion(0,1,2,3), np.quaternion(0,1,2,3)],
#     [np.quaternion(0,1.5,2.5,3.5), np.quaternion(0,3,3,3)],
#     [np.quaternion(0,5,4,1), np.quaternion(0,-4,-3,3.5)],
# ], dtype=np.quaternion)

# sig = np.array([
#     [np.quaternion(0,4,3,1), np.quaternion(0,1,2,3)],
#     [np.quaternion(0,1.5,2.5,3.5), np.quaternion(0,3.5,3,3)],
#     [np.quaternion(0,5,4,1), np.quaternion(0,-4,-3,6.5)],
#     [np.quaternion(0,5,4,1), np.quaternion(0,-4,-3,6.5)],

# ], dtype=np.quaternion)

# kr = np.array([
#     [np.quaternion(0,1,-2,3), np.quaternion(0,1,2,3)],
#     [np.quaternion(0,1.5,-2.5,3.5), np.quaternion(0,3,5,3)],
#     [np.quaternion(0,5,4,1), np.quaternion(0,-4,-3,3.5)],
# ], dtype=np.quaternion)

# res = conv2(sig, kl, kr)
# print(res)

import sys

sys.path.append('../')

from PIL import Image
from qftpy.io import im2q, q2im
from qftpy.fft import  AllOneAxis
from qftpy.conv import conv2
from qftpy.utils import unit, qzeros

img = Image.open(r'F:\QFTPy\example\phantom.jpg')
qimg = im2q(img)

import numpy as np

mu = unit(AllOneAxis)
R = np.exp(mu * np.pi / 4) / np.sqrt(8)
Sqrt2 = np.sqrt(2)

hL = np.array([
    [R, Sqrt2 * R, R],
    qzeros(3),
    np.conjugate([R, Sqrt2 * R, R]),
], dtype=np.quaternion).T

hR = np.conjugate(hL)

hor = conv2(qimg, hL, hR, keepShape=True)

horimg = q2im(hor, pil=True)

import matplotlib.pyplot as plt

print(horimg.size)

plt.figure()
plt.imshow(horimg)
plt.show()