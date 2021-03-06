# QFTPy

<img align="left" src="https://github.com/z0gSh1u/qftpy/actions/workflows/run-unit-tests.yml/badge.svg?branch=master"></img>

<br />

Quaternion Fourier Transform and Convolution

<img src="https://latex.codecogs.com/svg.image?\mathcal{X}^{\rm&space;D}(u,v)=\sum_{m=0}^{M-1}\sum_{n=0}^{N-1}W_M^{mu}x(m,n)W_N^{nv},\quad&space;W_N={\rm&space;exp}(-{\bf&space;\mu}\frac{2\pi}{N}),\quad\mu=\frac{1}{\sqrt{3}}(\rm&space;{i&plus;j&plus;k})" title="\mathcal{X}^{\rm D}(u,v)=\sum_{m=0}^{M-1}\sum_{n=0}^{N-1}W_M^{mu}x(m,n)W_N^{nv},\quad W_N={\rm exp}(-{\bf \mu}\frac{2\pi}{N}),\quad\mu=\frac{1}{\sqrt{3}}(\rm {i+j+k})" />

## Quick Start

- Install `QFTPy` using `pip` from [PyPI](https://pypi.org/project/QFTPy/)

  ```sh
  pip install QFTPy
  ```

  or via wheel file in [Releases](https://github.com/z0gSh1u/qftpy/releases)

  ```sh
  pip install /path/to/latest/release.whl
  ```

- Dependencies include numpy and [numpy-quaternion](https://github.com/moble/quaternion). The latter one enables quaternion in numpy like:

  ```python
  import numpy as np
  import quaternion
  
  q = np.quaternion(w, x, y, z)
  ```

  QFTPy internal uses it as quaternion support.

- QFTPy provides more than

  - `conv`, `conv2` for quaternion convolution (`qftpy.conv`)
  - `qfft`, `qfft2` and shift and inverse for Quaternion Fourier Transform (`qftpy.fft`)
  - `q2im`, `im2q` for color image I/O (`qftpy.io`)
  - And more in `qftpy.utils`.

## Documentation

- [**README**](https://github.com/z0gSh1u/qftpy/blob/master/README.md) as a quick start guide.
- [**API References**](https://zxuuu.tech/QFTPy)
- [**Examples**](https://github.com/z0gSh1u/qftpy/tree/master/example) in Jupyter Notebook.
- And it couldn't be better if you star or cite this repository when it helps to your works.

## Road Map

I'm going to enhance data validation (mainly shape and dtype) in the near future. Contributions are always welcome.

## References

Convolution and Fourier Transform definitions follow paper works and software from Sangwine.

```
[1] Todd A. Ell, Nicolas Le Bihan, Stephen J. Sangwine. Quaternion Fourier Transforms for Signal and Image Processing[M]. WILEY. 2014.
[2] Salem Said, Nicolas Le Bihan, Stephen J. Sangwine. Fast complexified quaternion Fourier transform[J]. arXiv:math/0603578. 2008.
[3] S.J. Sangwine. Colour image edge detector based on quaternion convolution[J]. Electronics Letters Online. 1998.
[4] n-le_bihan, sangwine. Quaternion toolbox for Matlab[CP/OL]. 2021. https://sourceforge.net/projects/qtfm.
```

## License

MIT
