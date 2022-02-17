from qftpy.io import im2q, q2im
from qftpy.fft import *
from PIL import Image
import quaternion
import numpy as np

arr = [0, 1, 1, 1, 0, 2, 2, 2, 0, 1, 3, 3, 0, 5, 2, 3]
qarr = quaternion.as_quat_array(arr)
print(qarr)
ax = quaternion.quaternion(0, 1, 1, 1)
ft = qfft(qarr, ax)
# print(ft)
ar = iqfft(ft, ax)
print(ar)
