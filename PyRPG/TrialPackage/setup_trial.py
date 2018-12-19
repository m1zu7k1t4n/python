from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

import numpy as np

sourcefiles = ['.pyx']

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("cython_trial", sourcefiles, include_dirs=[np.get_include()])],
)