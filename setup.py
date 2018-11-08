from os.path import abspath, dirname, join
from setuptools import Command, setup

from dracolearn import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(name='dracolearn',
      version=__version__,
      description='Learning weights for Draco',
      long_description=long_description,
      author='Dominik Moritz, Chenglong Wang',
      author_email='domoritz@cs.washington.edu, clwang@cs.washington.edu',
      license='BSD-3',
      url='https://github.com/uwdata/draco-learn',
      packages = ['dracolearn'],
      extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
      },
     )
