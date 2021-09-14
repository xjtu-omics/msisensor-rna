#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""==============================================================================
# Project: MSIRNA
# Script : show.py
# Author : Peng Jia
# Date   : 2021.03.29
# Email  : pengjia@stu.xjtu.edu.cn
# Description: TODO
=============================================================================="""

import pickle

from msisensor_rna.units import logger


def show_model(paras):
    model_path = paras.model[0]
    cancer_type = paras.cancer_type[0]
    input_description = paras.input_description[0]
    model_description = paras.model_description[0]
    gene_list_path = paras.gene_list[0]
    with open(model_path, 'rb') as f:
        classifier = pickle.load(f)
        description = pickle.load(f)
        genes = pickle.load(f)
    write_stat = False
    if cancer_type != ".":
        description["Cancer Type"] = cancer_type
        write_stat = True
    elif input_description != ".":
        description["Input Description"] = input_description
        write_stat = True
    elif model_description != ".":
        description["Model Description"] = model_description
        write_stat = True
    if write_stat:
        with open(model_path, 'wb') as f:
            pickle.dump(classifier, f)
            pickle.dump(description, f)
            pickle.dump(genes, f)
    for item, value in description.items():
        logger.info(item + ": {}".format(value))
    if gene_list_path != ".":
        with open(gene_list_path, "w") as f:
            f.write("\n".join(genes))
