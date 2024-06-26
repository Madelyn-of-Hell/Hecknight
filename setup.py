from setuptools import setup
from Cython.Build import cythonize

setup(
    name='colourwork',
    ext_modules=cythonize("colourwork.pyx"),
)
setup(
    name='DSTSensor',
    ext_modules=cythonize("DSTSensor.pyx"),
)