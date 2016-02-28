"""
This module provides the setup guidelines.
"""

import os

from setuptools import find_packages
from setuptools import setup

from recordata import __version__

## The absolute directory path:
HERE = os.path.abspath(os.path.dirname(__file__))

## The README file contents:
README = open(os.path.join(HERE, "README.md")).read()

## The LICENSE file contents:
LICENSE = open(os.path.join(HERE, "LICENSE")).read()

## Requirements for installation:
REQUIRED_LIBRARIES = [
    "Django==1.9.2",
    "django-filter==0.12.0",
    "djangorestframework==3.3.2",
    "django-cors-headers==1.1.0",
    "Markdown==2.6.5",
]

## Setup now:
setup(
    name="recordata",
    version=__version__,
    description="Sample Django/Ember Application",
    long_description=README,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Framework :: Django",
        "License :: MIT",
    ],
    keywords="django rest API",
    author="Vehbi Sinan Tunalioglu",
    author_email="vst@vsthost.com",
    url="http://www.vsthost.com",
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRED_LIBRARIES,
    dependency_links=[],
)
