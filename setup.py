#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
import imp
import subprocess
from setuptools import setup, find_packages


def get_version():
    try:
        file_, path, desc = imp.find_module('__version__', ['src/utaskweb'])
        version = imp.load_module('__version__', file_, path, desc).version
    finally:
        if file_ is not None:
            file_.close()
    return version


version = get_version()

# publish helper
if sys.argv[-1] == 'publish':
    for cmd in [
            'python setup.py sdist upload',
            'git tag {}'.format(version),
            'git push origin master --tag']:
        subprocess.check_call(cmd, shell=True)
    sys.exit(0)

with open('README.rst') as f:
    long_desc = f.read()

setup(
    name='utaskweb',
    version=version,
    package_dir={'': 'src'},
    description='Utils for scraping and crawling UTask-web',
    long_description=long_desc,
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    maintainer='Kentaro Wada',
    maintainer_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/utaskweb',
    install_requires=['requests', 'beautifulsoup4'],
    packages=find_packages(),
    package_data={},
    license='MIT',
    keywords='crawling scraping utility',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='nose.collector',
)
