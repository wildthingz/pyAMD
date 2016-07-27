from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
	long_description = f.read()

setup(name = 'AMD',
	version = '0.1.0',
	description = 'A tool to find the optimal segmentation size for visualising macrosegregation -- An extension to MakeContour',
	long_description = long_description,
	url = 'https://github.com/wildthingz/AMD',
	author = 'Hatef Khadivinassab',
	author_email = 'hatef.hadivinassab@gmail.com',

	classifiers=[
		"Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Operating System :: Linux :: Linux Debian"
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
		'Programming Language :: Python :: 2.7',
		'Framework :: Spyder',
		'Intended Audience :: End Users/Desktop',
		'Natural Language :: English',
		],

	install_requires=['numpy','scipy','MakeContour'],
	license = 'Creative Commons Attribution-Noncommercial-Share Alike license',
	keywords = ['AMD', 'macrosegregation', 'segmenation', 'visaliziation', 'contour']

	)
