import sys

sys.path.append('../')

from PIL import Image
from qftpy.io import im2q
from qftpy.fft import qfft2, qfftshift

img = Image.open(r'F:\QFTPy\example\lena_color.jpg')
qimg = im2q(img)

import numpy as np

spec = qfft2(qimg)
spec = qfftshift(spec)
spec = np.abs(spec)
spec = np.log(spec)

import matplotlib.pyplot as plt

plt.figure()
plt.imshow(spec, cmap='gray')
plt.show()


spec = (spec - np.min(spec)) / (np.max(spec) - np.min(spec)) * 255.0
spec = np.array(spec, dtype=np.uint8)
Image.fromarray(spec, mode='L').save('okspec.bmp')