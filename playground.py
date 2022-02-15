from qftpy.io import im2q, q2im
from PIL import Image
import quaternion
import numpy as np

q = quaternion.quaternion(1,1,0,1)
print(np.abs(q))