# -*- coding: utf-8 -*-

"""
"""

__status__ = "alpha"
__version__ = "1.0.0a"
__maintainer__ = (u"James Michael DuPont <jamesmikedupont@gmail.com>", )
__author__ = (u"James Michael DuPont <jamesmikedupont@gmail.com>", )

# Setup tools
from setuptools import setup, find_packages


setup(
    name = 'openapi-specification-python',
    version = ":versiontools:openapi-specification-python:VERSION",
    packages = find_packages(),
    author = "James Michael DuPont <jamesmikedupont@gmail.com>",
    maintainer = "James Michael DuPont <jamesmikedupont@gmail.com>",
    description = "JSON Schema Toolkit",
    keywords = ['json', 'schema', 'validation', 'django', 'sql', 'postgresql', ],
    license = 'Apache',
    url = 'https://www.openapis.org/',
    download_url = "https://github.com/h4ck3rm1k3/OpenAPI-Specification/archive/master.zip",
    test_suite = 'openapi-specification-python.tests.test_suite',
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires = [
    ],
    setup_requires = [ 'versiontools >= 1.3.1', ],
    tests_require = [ 'unittest2 >= 0.5.1' ],
    zip_safe = True)

