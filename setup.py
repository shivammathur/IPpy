#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os import path

requirements = [
    'pingparsing==0.6.0',
    'future>=0.16.0'
]

test_requirements = [
    'bumpversion>=0.5.3',
    'wheel>=0.29.0',
    'watchdog>=0.8.3',
    'tox>=3.13.2',
    'coverage>=4.1',
    'Sphinx>=1.4.8',
    'cryptography>=1.7',
    'PyYAML>=3.11',
    'pytest>=3.9.3',
    'twine>=1.13.0'
]

# read the contents of your README file

setup(
    name='ippy',
    version='0.3.5',
    description="Parallel testing of IP addresses and domains in python.",
    long_description='''[![PyPI version](https://badge.fury.io/py/ippy.svg)](https://pypi.python.org/pypi/ippy)
[![Build Status](https://travis-ci.org/shivammathur/IPpy.svg?branch=master)](https://travis-ci.org/shivammathur/IPpy)
[![Code Climate](https://codeclimate.com/github/shivammathur/IPpy/badges/gpa.svg)](https://codeclimate.com/github/shivammathur/IPpy)
[![Coverage Status](https://coveralls.io/repos/github/shivammathur/IPpy/badge.svg?branch=master)](https://coveralls.io/github/shivammathur/IPpy?branch=master)
[![codecov](https://codecov.io/gh/shivammathur/IPpy/branch/master/graph/badge.svg)](https://codecov.io/gh/shivammathur/IPpy)
[![License](https://img.shields.io/badge/license-MIT-428f7e.svg)](https://pypi.python.org/pypi/ippy)

<img src="https://shivammathur.com/IPpy.png" align="right" width="250">

# IPpy
Parallel testing of IP addresses and domains in python.
Reads IP addresses and domains from a CSV file and gives two lists of accessible and inaccessible ones.

## About
- Compatible with both Python 2 and 3.
- Testing of IPs and domains is done in parallel.
- By default there are 4 Workers.
- All Workers work on an input Queue and a output Queue.

## Modes
- verbose - if true, ping output will be displayed.
- output - `json` or `csv`

## Support
- Windows, Linux and macOS are supported.
- Supports both IPv4 and IPv6 IPs, and domain names.
```csv
# Examples
127.0.0.1
::1
localhost
```

## Install
```
$ pip install ippy
```

## Usage
```python
# Create IPpy instance
ippy_obj = ippy.Ippy()

# Set config - verbose, output, num_workers
# verbose - True or False
# output - csv or json
ippy_obj.set_config(True, 'csv', 4)

# Set Input File
ippy_obj.set_file(file='ip_list.csv')

# Run IPpy
ippy_obj.run()

# Get Results
output = ippy_obj.result()
print(output)
```
## Tests
To run the tests, first install tox.
```
$ pip install tox
```

then run tox from the project root directory.
```
$ tox
```
''',
    long_description_content_type='text/markdown',
    author="Shivam Mathur",
    author_email='shivam_jpr@hotmail.com',
    url='https://github.com/shivammathur/ippy',
    download_url='https://github.com/shivammathur/ippy/archive/0.3.5.tar.gz',
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
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
    ],
    test_suite='tests',
    tests_require=test_requirements
)
