#!/usr/bin/python
# -*- coding: utf-8 -*-

import minime

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    readme = f.read()
with open('HISTORY.md') as f:
    history = f.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name=minime.__title__,
    description='MiniMe - An online URL shortener',
    long_description=readme,
    version=minime.__version__,
    author='bluecap-se',
    author_email='hello@bluecap.se',
    url='https://github.com/bluecap-se/minime',
    license='MIT',
    zip_safe=False,
    platforms='any',
    packages=['minime'],
    install_requires=requirements,
    scripts=['bin/minime'],
    keywords=['mini', 'minime', 'url', 'short', 'tiny'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ]
)