#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup
from src.i2cssh.version import version


setup(
    name="i2cssh",
    version=version(),
    author="Wouter de Bie",
    author_email="wouter@evenflow.nl",
    description="csshX like ssh tool for iTerm2",
    url="http://github.com/wouterdebie/i2cssh",
    entry_points={"console_scripts": ["i2cssh=i2cssh.main:main"]},
    license="MIT",
    keywords="ssh i2cssh csshX".split(),
    classifiers=[
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
        "Topic :: Terminals :: Terminal Emulators/X Terminals",
        "Topic :: Utilities",
    ],
    python_requires=">3.8",
    install_requires=[
        "click-option-group==0.5.6",
        "click==8.1.6",
        "iterm2==2.6",
        "PyYAML==6.0.1",
    ],
)
