#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import print_function
import sys
from setuptools import setup, find_packages


if sys.version_info < (2, 7):
    print('pyutils requires python version >= 2.7.', file=sys.stderr)
    sys.exit(1)

install_requires = [
    'requests>=2.2.1',
    'beautifulsoup4==4.3.2',
]

with open('README.rst') as f:
    long_desc = f.read()
version='0.1.2'

setup(
    name="utaskweb",
    version=version,
    description="Utils for scraping and crawling UTask-web",
    long_description=long_desc,
    author="Kentaro Wada",
    author_email='www.kentaro.wada@gmail.com',
    maintainer='Kentaro Wada',
    maintainer_email='www.kentaro.wada@gmail.com',
    url="http://github.com/wkentaro/utaskweb",
    install_requires=install_requires,
    packages=find_packages(),
    package_data={},
    license="MIT",
    keywords="crawling scraping utility",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='nose.collector',
)

