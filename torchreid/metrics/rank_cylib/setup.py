import numpy as np
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext


def numpy_include():
    try:
        numpy_include = np.get_include()
    except AttributeError:
        numpy_include = np.get_numpy_include()
    return numpy_include

ext_modules = cythonize(
    [
        Extension('rank_cy', ['rank_cy.pyx'], include_dirs=[numpy_include()],)
    ],
    compiler_directives={"language_level": "3"},
)

setup(
    name='Cython-based reid evaluation code',
    cmdclass = {'build_ext': build_ext},
    ext_modules=cythonize(ext_modules)
)
