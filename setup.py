#!/usr/bin/env python
import os
import numpy as np

from setuptools import setup, Extension

VERSION = "1.0.0"

README = open('README.md').read()

watershed_ext = Extension(
    name="fast_watershed._am_watershed",
    language="c++",
    sources=[os.path.join("fast_watershed", "src", _)
             for _ in "ws_alg.cpp", "ws_queue.cpp"] + [
             os.path.join("fast_watershed", "_am_watershed.pyx")],
    include_dirs=[os.path.join("fast_watershed", "src"), np.get_include()])

setup(
    name='fast_watershed',
    version=VERSION,
    packages=["fast_watershed"
              ],
    url="https://github.com/microns-ariadne/fast_watershed",
    description="Fast watershed for Connectome project's pipeline",
    long_description=README,
    install_requires=[
        "Cython>=0.24.0",
        "enum34>=1.0.0",
        "numpy>=1.9.3"],
    ext_modules=[watershed_ext],
    zip_safe=False
)
