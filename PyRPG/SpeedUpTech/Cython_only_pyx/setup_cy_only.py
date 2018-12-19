from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

import numpy as np

sourcefiles = ['cy_only.pyx']

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("cython_pyx", sourcefiles, include_dirs=[np.get_include()])],
)