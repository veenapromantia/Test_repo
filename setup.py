# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in aristo/__init__.py
from aristo import __version__ as version

setup(
	name='aristo',
	version=version,
	description='Aristo',
	author='sujay',
	author_email='sujay.j@promantia.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
