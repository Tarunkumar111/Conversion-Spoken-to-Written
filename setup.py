import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	  name = 'spoken2written',
      packages = ['spoken2written'],
      version='0.1',
      description='Convert Spoken English given as text to Written English ',
      author='Tarun KUmar',
      author_email='tarunkumarjee58@gmail.com',
      url='https://github.com/Tarunkumar111/Conversion-Spoken-to-Written',
      classifiers = [
     					 'Intended Audience :: Developers',
      					'Programming Language :: Python'
  				],
	  long_description=open_file('README.rst').read()

     )
