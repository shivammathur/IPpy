#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pingparsing==0.6.0'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='ippy',
    version='0.1.1',
    description="Parallel testing of IP addresses and domains in python.",
    long_description=readme + '\n\n' + history,
    author="Shivam Mathur",
    author_email='shivam_jpr@hotmail.com',
    url='https://github.com/shivammathur/ippy',
    download_url = 'https://github.com/shivammathur/ippy/archive/0.1.1.tar.gz',
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
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries'
        'Software Development :: Libraries :: Python Modules'
        'System :: Networking'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
