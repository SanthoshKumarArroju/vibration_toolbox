#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup
import os

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='Vibration Toolbox',
      version='0.5b0',
      description='Educational code illustrating fundamentals of vibration for mechanical engineers.',
      author='Joseph C. Slater and Raphael Timbo',
      author_email='joseph.c.slater@gmail.com',
      url='https://github.com/vibrationtoolbox/pvtoolbox',
      download_url='https://github.com/josephcslater/array_to_latex/archive/0.5b0.tar.gz',
      packages=['vibration_toolbox'],
      long_description = read('README.rst'),
      keywords=['vibration','mechanical engineering'],
      install_requires=[
      'numpy',
      'scipy',
      'matplotlib'
      ]
      )