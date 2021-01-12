from distutils.core import setup
from Cython.Build import cythonizec
setup(name='target_encoding_v4', ext_modules=cythonize('target_encoding_v4.pyx'),)