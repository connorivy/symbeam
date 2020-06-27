"""Setup file for symbeam package
"""
# Import modules
# --------------
from setuptools import setup, find_packages
import os

# Get path of the package, where steup.py is located
here = os.path.abspath(os.path.dirname(__file__))

# Read the verison number
with open(os.path.join(here, 'VERSION')) as versionFile:
    version = versionFile.read().strip()

# Store the README.md file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    longDescription = f.read()

setup(
    # Project name
    name='symbeam',

    # Version from the version file
    version=version,

    # Short description
    description='A pedagogical package for bending diagrams',

    # Long descriptionf from README.md
    long_description=longDescription,
    long_description_content_type='text/markdown',

    # Github url
    url='https://github.com/amcc1996/symbeam',

    # Authors
    author='António Manuel Couto Carneiro, Rodrigo Pinto Carvalho @FEUP',
    author_email='amcc@fe.up.pt, rcarvalho@fe.up.pt',

    # Licensing
    licence='MIT',

    # Classifiers (selected from https://pypi.org/classifiers/)
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        # Python version obtained with https://pypi.org/project/check-python-versions/
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
    ],

    # Keywords
    keywords='bending beam deflection symbolic',

    # Project URLs
    project_urls={
        # 'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Source': 'https://github.com/amcc1996/symbeam',
        'Tracker': 'https://github.com/amcc1996/symbeam/issues',
    },

    # Python version compatibility
    python_requires='>=3.5, <3.9',

    install_requires=[
    ]
    )
