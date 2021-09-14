#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""==============================================================================
# Project: msisensor_rna-rna
# Script : setup.py.py
# Author : Peng Jia
# Date   : 2021.03.29
# Email  : pengjia@stu.xjtu.edu.cn
# Description: TODO
=============================================================================="""
from setuptools import setup

from msisensor_rna.units import default_general

setup(
    name=default_general["name"],
    version=default_general["version"],
    description=default_general["name"] + " " + default_general["description"],
    url="https://github.com/xjtu-omics/msisensor-rna",
    author=default_general["author"],
    author_email=default_general["contact"],
    license='Custom License',
    keywords='Microsatellite instability, RNA-seq, Immunotherapy, Tumor only ',
    packages=['msisensor_rna'],
    install_requires=['pandas>=1.0', "numpy>=1.16",
                      "scikit-learn>=0.24", "imbalanced-learn>=0.8.0"],
    python_requires='>=3.6',
    entry_points={'console_scripts': ['msisensor-rna = msisensor_rna.msisensor_rna:main']},
)
