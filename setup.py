# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
	try:
		with open('README.rst') as f:
			return f.read()
	except:
		pass

setup(name='cmail',
	version='1.0.0',
	classifiers=[
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
	keywords='email sender smtp',
	description='A simple command-line email client!',
	long_description=readme(),
	url='https://github.com/nikhilkumarsingh/cmail',
	author='Nikhil Kumar Singh',
	author_email='nikhilksingh97@gmail.com',
	license='MIT',
	packages=['cmail'],
	install_requires=['pyqt5', 'tabulate'],
	include_package_data=True,
	entry_points="""
	[console_scripts]
	cmail = cmail.cmail:main
	""",
	zip_safe=False)
