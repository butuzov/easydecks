"""
easydecks
~~~~~~~~~
Wrapper for the genanki (with benefits).
"""

from setuptools import setup, find_packages
from os import path

directory = path.abspath(path.dirname(__file__))
with open(path.join(directory, "readme.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="easydecks",
    version=__import__("easydecks").__version__,
    description="Wrapper for the genanki (with benefits).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Oleg Butuzov",
    author_email="butuzov@made.ua",
    platforms=["OS Independent"],
    python_requires='>=3.6',
    packages=find_packages(exclude=['tests']),
    install_requires=["genanki"],
    license="Apache License 2.0",
    classifiers=[
        "Intended Audience :: Education",
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Education",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
