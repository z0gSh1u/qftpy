'''
    Color image input and output for QFTPy.
    
    by z0gSh1u @ github.com/z0gSh1u/qftpy
'''

import numpy as np
import quaternion
from PIL import Image


def im2q(img):
    """
        Convert 3-channel color image to quaternion matrix. \\
        `img` can be PIL Image (HWC) or numpy array (CHW).
    """
    if isinstance(img, Image.Image):
        img = np.array(img).transpose((2, 0, 1))  # PIL Image has order HWC, convert to CHW
    assert len(img.shape) == 3, 'img does not have multi channels.'
    c, h, w = img.shape
    assert c == 3, 'img is not of 3 channels.'
    scala = np.zeros((h, w))
    img = np.stack((scala, *img), axis=0)  # append scala channel
    img = img.transpose((1, 2, 0))  # CHW to HWC, so that we get 0rgb0rgb... using flatten.
    return quaternion.as_quat_array(img.flatten()).reshape((h, w))


def q2im(qimg, pil=False):
    """
        Convert quaternion image to PIL image (`pil = True`, 24-bit RGB) or numpy array (CHW).
    """
    assert len(qimg.shape) == 2, 'qimg should be 2D.'
    vec = quaternion.as_vector_part(qimg)  # has HWC
    if pil:
        return Image.fromarray(vec.astype(np.uint8))
    return vec.transpose((2, 0, 1))  # to CHW numpy array
