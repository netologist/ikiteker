#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import ikiteker

setup(
    name='ikiteker',
    version=ikiteker.__version__,
    description=ikiteker.__doc__,
    long_description=ikiteker.__doc__,
    author='Hasan  Ozgan',
    author_email='hasanozgan@gmail.com',
    url='https://github.com/hasanozgan/ikiteker',
    download_url='https://github.com/hasanozgan/ikiteker/downloads',
    packages=find_packages(exclude=['tests', 'tests.*']),
    test_suite='ikiteker.tests',
    install_requires= [
        'tornado'
    ],
    tests_require=[
        'PyHamcrest'
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Communications', 'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        ]
    )
