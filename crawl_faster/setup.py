from distutils.core import setup
from Cython.Build import cythonize

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        "dis_func_cyth.pyx", annotate=True
    )  # enables generation of the html annotation file
)
