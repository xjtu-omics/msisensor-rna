#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""==============================================================================
# Project: MSIRNA
# Script : detection.py
# Author : Peng Jia
# Date   : 2021.03.22
# Email  : pengjia@stu.xjtu.edu.cn
# Description: TODO
=============================================================================="""
from src.units import logger

def detection_msi(paras):
    input_path=paras.input[0]
    output_path=paras.output[0]
    custom=paras.custom[0]
    custom_model=paras.custom_model[0]
    cancer_type=paras.cancer_type[0]
    model_path=paras.model[0]
    logger.info("The input expression data: {}".format(input_path))
    logger.info("The output MSI result: {}".format(output_path))



    # print(input_path)
