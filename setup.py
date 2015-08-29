#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import sys
import re
import imp
import subprocess
from setuptools import setup, find_packages

this_dir = os.path.dirname(os.path.abspath(__file__))


def get_version():
    version_file = os.path.join(this_dir, 'src/utaskweb/version.py')
    with open(version_file) as f:
        for line in f.readlines():
            line = line.strip()
            if re.match('^__version__ = .*', line):
                version = re.split('^__version__ = ', line)[-1].strip("'")
    return version

# publish helper
if sys.argv[-1] == 'publish':
    for cmd in [
            'python setup.py sdist upload',
            'git tag {}'.format(get_version()),
            'git push origin master --tag']:
        subprocess.check_call(cmd, shell=True)
    sys.exit(0)

setup(
    name='utaskweb',
    version=get_version(),
    package_dir={'': 'src'},
    packages=find_packages('src'),
    description='Utils for scraping and crawling UTask-web',
    long_description=open('README.rst').read(),
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    maintainer='Kentaro Wada',
    maintainer_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/utaskweb',
    install_requires=open('requirements.txt').readlines(),
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
