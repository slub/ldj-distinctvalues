"""
A Python3 program that extracts the occurence of distinct values of a given path in a line-delimited json file.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='ldj_distinctvalues',
      version='0.0.1',
      description='a Python3 program that extracts some statistics regarding field coverage from an elasticsearch index',
      url='https://github.com/slub/ldj-distinctvalues',
      author='Bernhard Hering',
      author_email='bernhard.hering@slub-dresden.de',
      license="Apache 2.0",
      packages=[
          'ldj_distinctvalues',
      ],
      package_dir={'ldj_distinctvalues': 'ldj_distinctvalues'},
      install_requires=[
          'argparse>=1.4.0'
      ],
      entry_points={
          "console_scripts": ["ldj-distinctvalues=ldj_distinctvalues.ldj_distinctvalues:run"]
      }
      )
