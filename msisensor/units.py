#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""==============================================================================
# Project: MSIRNA
# Script : units.py
# Author : Peng Jia
# Date   : 2021.03.19
# Email  : pengjia@stu.xjtu.edu.cn
# Description: TODO
=============================================================================="""
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s]\t %(message)s')
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

default_general = {
    "version": "0.1.4",
    "name": "msisensor-rna",
    "description": "Microsatellite Instability (MSI) detection with RNA sequencing data.",
    "author": "Peng Jia, Xuanhao Yang et al.",
    "contact": "pengjia@stu.xjtu.edu.cn"
}
default_detection = {
    "custom_model": False
}
