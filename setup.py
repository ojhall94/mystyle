#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages

setup(name='mystyle',
      version='1.0.0',
      description="Matplotlib Custom Style",
      author='Oliver J. Hall',
      author_email='ojh251@student.bham.ac.uk',
      license='MIT',
      packages=find_packages(),
      install_requires=['matplotlib'],
      package_data = {'mystyle':['mystyle.mplstyle']},
      include_package_data=True)
