import sys

from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.1"
ext_modules = [
    Pybind11Extension("yamh",
            ["src/murmur3.cpp", "src/python.cpp"],
            # Example: passing in the version to the compiled code
            define_macros = [('VERSION_INFO', __version__)],
    ),
]

setup(
    name="yamh",
    version=__version__,
    author="mrnicegaius",
    author_email="78328014+mrnicegaius@users.noreply.github.com",
    url="https://github.com/mrnicegaius/yamh",
    description="Yet another murmur3 hash library",
    long_description="""
Provides an interface to the murumurv3 hash library, but allow for streaming of
data with a similar interface to the python hash libraries, ie:
```python
m = yamh.murmur3_32()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.digest()
```
""",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
)
