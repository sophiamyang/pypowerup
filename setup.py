# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [ 
    'scipy',
    'numpy',
    'innerscope'
]

setup_requirements = [ ]

test_requirements = [
    'pytest'
 ]

setup(
    name='pypowerup',
    author="Sophia Man Yang",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Power analysis tool for experimental and quasi-experimental designs",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='pypowerup',    
    packages=find_packages(include=['pypowerup']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sophiamyang/pypowerup',
    version='0.1.0',
    zip_safe=False,
)
