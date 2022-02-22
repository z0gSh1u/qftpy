import setuptools

setuptools.setup(name="qftpy",
                 version="0.1",
                 author="z0gSh1u",
                 author_email="zx.cs@qq.com",
                 description="Quaternion Fourier Transform and Convolution",
                 url="https://github.com/z0gSh1u/qftpy",
                 packages=setuptools.find_packages(),
                 install_requires=['numpy', 'quaternion'])