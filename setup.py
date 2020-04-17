# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in estore/__init__.py
from estore import __version__ as version

setup(
	name='estore',
	version=version,
	description='Tienda Virtual para ERPNext',
	author='OVENUBE',
	author_email='juan.espinoza@ovenube.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
