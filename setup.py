#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

try:
    import multiprocessing  # noqa
except ImportError:
    pass

setup(
    name='warp10client',
    version='1.0.1',
    description="OVH Python Warp10 Client",
    author="OVH",
    description_file="README.md",

    packages=[
        'warp10client',
        'warp10client/common',
    ]
)
