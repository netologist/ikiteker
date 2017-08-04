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
    test_suite='tests',
    install_requires= [
        'tornado',
        'requests'
    ],
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
