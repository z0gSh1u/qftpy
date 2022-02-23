

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