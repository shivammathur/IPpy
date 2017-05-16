#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [
    'pingparsing==0.6.0'
]

test_requirements = [
    'bumpversion>=0.5.3',
    'wheel>=0.29.0',
    'watchdog>=0.8.3',
    'tox>=2.3.1',
    'coverage>=4.1',
    'Sphinx>=1.4.8',
    'cryptography>=1.7',
    'PyYAML>=3.11',
    'pytest>=2.9.2'
]

setup(
    name='ippy',
    version='0.2.3',
    description="Parallel testing of IP addresses and domains in python.",
    author="Shivam Mathur",
    author_email='shivam_jpr@hotmail.com',
    url='https://github.com/shivammathur/ippy',
    download_url='https://github.com/shivammathur/ippy/archive/0.2.3.tar.gz',
    packages=[
        'ippy',
    ],
    package_dir={'ippy':
                 'ippy'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='ippy',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
    ],
    test_suite='tests',
    tests_require=test_requirements
)
