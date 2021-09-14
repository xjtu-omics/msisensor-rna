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
import pickle
import pandas as pd
from msisensor_rna.units import logger


def detection_msi(paras):
    input_path = paras.input[0]
    output_path = paras.output[0]
    model_path = paras.model[0]
    directly_run = paras.run_directly[0]
    logger.info("The input expression data: {}".format(input_path))
    logger.info("The output MSI result: {}".format(output_path))
    logger.info("The model path: {}".format(model_path))
    with open(model_path, 'rb') as f:
        classifier = pickle.load(f)
        description = pickle.load(f)
        genes = pickle.load(f)
    logger.info("======================================================")
    for item, value in description.items():
        logger.info("Model description -- " + item + ": {}".format(value))
    if not directly_run:
        run_next = input("Please check the Model description! Are you sure to use this model to predict MSI? [Yes/No] ")
        if run_next.upper() not in ["YES", "Y"]:
            logger.info("Exit by the user")
    logger.info("Check the input file!")
    df_input = pd.read_csv(input_path, index_col=0).fillna(0)
    genes_this = df_input.columns.to_list()
    if len(set(genes) - set(genes_this)) > 0:
        logger.error("Please provide the fallowing genes' expression!")
        print(",".join(set(genes) - set(genes_this)))
        exit()
    x = df_input[genes]
    x_name = df_input.index.to_list()
    y_pre = classifier.predict(x)
    y_pre_pro = classifier.predict_proba(x)[:, 1]
    output_file = open(output_path, "w")
    output_file.write("sample_id,msi_status,probability_of_MSI-H\n")
    for sample, msi, msi_pro in zip(x_name, y_pre, y_pre_pro):
        output_file.write("{sample},{msi},{msi_pro}\n".format(sample=sample, msi="MSI-H" if msi == 1 else "MSI",
                                                              msi_pro=round(msi_pro, 4)))
    output_file.close()
    logger.info("Finished!")
