# -*- coding: utf-8 -*-

__author__ = 'sinlov'

from setuptools import setup

requires = [
    'requests>=2.18.4',
]

test_requirements = [
    'mock>=2.0.0',
    'pytest>=2.8.0',
    'pytest-cov',
    'pytest-mock',
    'pytest-xdist',
]

setup(
    name='testRequest',
    version='0.0.1',
    description='test request',
    # long_description=read('README.md'),
    license='',

    python_requires='>=2.6',
    # dependences
    install_requires=requires,
    tests_require=test_requirements,
    # if use console scripts must open below
    zip_safe=False,
    extras_require={

    },
)
