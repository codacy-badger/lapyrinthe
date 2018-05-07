#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import lapyrinthe

setup(
    name='lapyrinthe',
    version=lapyrinthe.__version__,
    packages=find_packages(),
    author="Jeremy Collin",
    author_email="jeremy.collin.lnk@gmail.com",
    description="The Lapyrinthe",
#    long_description=open('README.rst').read(),
    install_requires=[
        "pygame==1.9.3",
        "nuitka==0.5.30",
        ],
    include_package_data=True,
    url='https://github.com/ashmonger/lapyrinthe',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Environment :: X11 Applications",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",  # noqa
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    entry_points={'console_scripts': ['lapyrinthe = lapyrinthe:main']},
    license="GPLv3",
)
