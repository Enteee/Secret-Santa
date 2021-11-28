#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='secretsanta',
    version='1.0',
    # Modules to import from other scripts:
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'dev': [
            'ipdb',
        ]
    },
    # Executables
    scripts=["secretsanta.py"],
)
