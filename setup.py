#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, Extension, find_packages
import sysconfig

with open('README.rst') as f:
    readme = f.read()

with open('HISTORY.rst') as f:
    history = f.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pbpl-common',
    version='0.1.0',
    description='Python package containing things useful to other PBPL packages',
    long_description=readme + '\n\n' + history,
    author='Brian Naranjo',
    author_email='brian.naranjo@gmail.com',
    url='https://github.com/bnara/pbpl-common',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    keywords='UCLA PBPL units si mks cgs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points = {
        'console_scripts':
        ['pbpl-common-encode = pbpl.common.encode:main']
    },
    namespace_packages=['pbpl']
)
