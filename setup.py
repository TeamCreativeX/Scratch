# -*- coding: utf-8 -*-

# Learn more: https://github.com/TeamCreativeX/Scratch

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Scratch',
    version='0.0.1',
    description='A game by Team Creative X',
    long_description=readme,
    author='Team Creative X',
    url='https://github.com/TeamCreativeX/Scratch',
    license=license
)
