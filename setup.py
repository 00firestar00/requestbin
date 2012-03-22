#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='requestbin',
    version='1.1.0',
    author='Jeff Lindsay',
    author_email='jeff.lindsay@twilio.com',
    description='HTTP request collector and inspector',
    packages=find_packages(),
    install_requires=['ginkgo', 'feedparser'],
    data_files=[],
)
