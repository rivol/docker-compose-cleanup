#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0,<7',
    'colorama>=0.3.9,<1',
    'docker>=2.6,<3',
]
setup_requirements = []
test_requirements = []

setup(
    author="Rivo Laks",
    author_email='code@rivolaks.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Helps you cleanup Docker images of multiple Docker Compose projects.",
    entry_points={
        'console_scripts': [
            'docker-compose-cleanup=docker_compose_cleanup.cli:main',
            'doco-cleanup=docker_compose_cleanup.cli:main',
        ],
    },
    install_requires=requirements,
    license="ISC license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='docker-compose-cleanup',
    name='docker-compose-cleanup',
    packages=find_packages(include=['docker_compose_cleanup']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rivol/docker-compose-cleanup',
    version='1.0.0',
    zip_safe=False,
)
