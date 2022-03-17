import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="encodingdotcom_api",
    version="0.5.0",
    description="Encoding.com Python3 API",
    license="",
    keywords="encoding.com transcoding",
    url="",
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests", "*.examples", "example*"]),
    long_description=read('README.md'),
    install_requires=[
        "requests", "lxml", "urllib3"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: No Input/Output (Daemon)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7"
    ],
)
