"""
easydecks
~~~~~~~~~
Wrapper for the genanki with benefits.
"""

from setuptools import setup, find_packages

setup(
    name="easydecks",
    version=__import__("easydecks").__version__,
    description="Wrapper for genanki with benefits",
    author="Oleg Butuzov",
    author_email="butuzov@made.ua",
    platforms=["OS Independent"],
    packages=find_packages(exclude=['tests']),
    install_requires=["genanki"],
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
