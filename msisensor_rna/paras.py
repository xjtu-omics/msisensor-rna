#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""==============================================================================
# Project: MSIRNA
# Script : paras.py
# Author : Peng Jia
# Date   : 2021.03.19
# Email  : pengjia@stu.xjtu.edu.cn
# Description: parameters of the software
=============================================================================="""
import logging

version_num = "1.0"  # build at 2021.03.19
paras_default = {

}

import os
import sys

curpath = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path.append(os.path.dirname(curpath))
import argparse
from msisensor_rna.units import *


def args_process():
    """
    argument procress
    """
    commands = []
    commands_parser = {}
    parser = argparse.ArgumentParser(description=default_general["name"] + ": " +
                                                 default_general["description"]
                                     )
    parser.usage = default_general["name"] + " <command> [options]"
    parser.add_argument('-V', '--version', action='version',
                        version=default_general["name"] + default_general["version"])
    subparsers = parser.add_subparsers(title="command", metavar="", dest='command')
    ###################################################################################################################

    # command genes
    parser_train = subparsers.add_parser('genes',
                                         help='Select informative genes for microsatellite instability detection.')
    parser_train.description = 'Select informative genes for microsatellite instability detection.'
    commands.append("genes")
    parser_train.add_argument('-i', '--input', required=True, type=str, nargs=1,
                              help="The path of input file. e.g. xxx.csv [required]")
    parser_train.add_argument('-o', '--output', required=True, type=str, nargs=1,
                              help="The output file of gene information. e.g. xxx.csv [required]")
    parser_train.add_argument('-thresh_t', '--threads', required=False, type=str, nargs=1,default=4,
                              help="The threads used to run this program. [default=4]")
    parser_train.add_argument('-thresh_cov', '--thresh_cov', required=False, type=str, nargs=1, default=0.5,
                              help="Threshold for coefficient of variation of gene expression value of all samples (Mean/Std). [default=0.5]")
    parser_train.add_argument('-thresh_p', '--thresh_p_ranksum', required=False, type=str, nargs=1, default=0.01,
                              help="Threshold for Pvalue of rank sum test between MSI-H and MSS samples. [default=0.01]")
    parser_train.add_argument('-thresh_auc', '--thresh_AUCscore', required=False, type=str, nargs=1, default=0.01,
                              help="Threshold for AUC score: AUC score was calculating by the sklearn package. [default=0.65]")

    # Pvalue_ranksum: Pvalue of rank sum test between MSI-H and MSS samples.
    # AUC score: AUC score was calculating by the sklearn package.
    # Random forest score: Random forest score of 5-fold cross validation.
    # SVM score: Support vector machine score of 5-fold cross validation.

    # parser_train.add_argument("-t", "--cancer_type", required=True, type=str, nargs=1,
    #                           help="The cancer type for this training. e.g. CRC, STAD, PanCancer etc.")
    # parser_train.add_argument('-c', '--classifier', required=False, type=str, nargs=1, default=["SVM"],
    #                           choices=["SVM", "RandomForest", "LogisticRegression", "MLPClassifier", "GaussianNB",
    #                                    "AdaBoostClassifier"],
    #                           help="The machine learning classifier for MSI detection. [default = SVM]")
    # parser_train.add_argument('-di', '--input_description', required=False, type=str, nargs=1, default=["."],
    #                           help="The description of the input file. [default = None]")
    # parser_train.add_argument("-dm", "--model_description", required=False, type=str, nargs=1,
    #                           default=["."],
    #                           help="Description for this trained model.")
    parser_train.add_argument("-p", "--positive_num", required=False, type=int, nargs=1,
                              default=[10],
                              help="The minimum  positive sample of MSI for training. [default = 10]")
    # parser_train.add_argument("-a", "--author", required=False, type=str, nargs=1,
    #                           default=["."],
    #                           help="The author who trained the model. [default = None]")
    # parser_train.add_argument("-e", "--email", required=False, type=str, nargs=1,
    #                           default=["."],
    #                           help="The email of the author. [default = None]")
    commands_parser["genes"] = parser_train

    ###################################################################################################################

    # command train
    parser_train = subparsers.add_parser('train',
                                         help='Train custom model for microsatellite instability detection.')
    parser_train.description = 'Train custom model for microsatellite instability detection.'
    commands.append("train")
    parser_train.add_argument('-i', '--input', required=True, type=str, nargs=1,
                              help="The path of input file. [required]")
    parser_train.add_argument('-m', '--model', required=True, type=str, nargs=1,
                              help="The trained model of the input file. [required]")
    parser_train.add_argument("-t", "--cancer_type", required=True, type=str, nargs=1,
                              help="The cancer type for this training. e.g. CRC, STAD, PanCancer etc.")
    parser_train.add_argument('-c', '--classifier', required=False, type=str, nargs=1, default=["SVM"],
                              choices=["SVM", "RandomForest", "LogisticRegression", "MLPClassifier", "GaussianNB",
                                       "AdaBoostClassifier"],
                              help="The machine learning classifier for MSI detection. [default = SVM]")
    parser_train.add_argument('-di', '--input_description', required=False, type=str, nargs=1, default=["."],
                              help="The description of the input file. [default = None]")
    parser_train.add_argument("-dm", "--model_description", required=False, type=str, nargs=1,
                              default=["."],
                              help="Description for this trained model.")
    parser_train.add_argument("-p", "--positive_num", required=False, type=int, nargs=1,
                              default=[10],
                              help="The minimum  positive sample of MSI for training. [default = 10]")
    parser_train.add_argument("-a", "--author", required=False, type=str, nargs=1,
                              default=["."],
                              help="The author who trained the model. [default = None]")
    parser_train.add_argument("-e", "--email", required=False, type=str, nargs=1,
                              default=["."],
                              help="The email of the author. [default = None]")
    commands_parser["train"] = parser_train

    ###################################################################################################################
    # command show
    parser_show = subparsers.add_parser('show', help='Show the information of the model and add more details.')
    parser_show.description = 'Show the information of the model and add more details.'
    commands.append("show")

    parser_show.add_argument('-m', '--model', required=True, type=str, nargs=1,
                             help="The trained model path. [required]")
    parser_show.add_argument("-t", "--cancer_type", required=False, type=str, nargs=1, default=["."],
                             help="Rename the cancer type. e.g. CRC, STAD, PanCancer etc. [default = None]")
    parser_show.add_argument('-di', '--input_description', required=False, type=str, nargs=1, default=["."],
                             help="Add description for the input file. [default = None]")
    parser_show.add_argument("-dm", "--model_description", required=False, type=str, nargs=1,
                             default=["."],
                             help="Add description for this trained model. [default = None]")
    parser_show.add_argument("-g", "--gene_list", required=False, type=str, nargs=1,
                             default=["."],
                             help="The path for the genes must be included for this model. [default = None]")

    commands_parser["show"] = parser_show
    ###################################################################################################################
    # command detection
    parser_detection = subparsers.add_parser('detection', help='Microsatellite instability detection.')
    parser_detection.description = 'Microsatellite instability detection.'
    commands.append("detection")
    parser_detection.add_argument('-i', '--input', required=True, type=str, nargs=1,
                                  help="The path of input file. [required]")
    parser_detection.add_argument('-o', '--output', required=True, type=str, nargs=1,
                                  help="The path of output file prefix. [required]")
    parser_detection.add_argument('-m', '--model', required=True, type=str, nargs=1,
                                  help="The path of the microsatellite regions. [required]")
    parser_detection.add_argument('-d', '--run_directly', required=False, type=bool, default=[False], nargs=1,
                                  help="Run the program directly without any Confirm. [default = False]")

    commands_parser["detection"] = parser_detection
    ###################################################################################################################

    if len(os.sys.argv) < 2:
        parser.print_help()
        return False

    if os.sys.argv[1] in ["-h", "--help", "-?", "--h", "-H", "--H"]:
        parser.print_help()
        return False
    if os.sys.argv[1] in ["-V", "-v", "--version", "-version", "--v"]:
        # parser.print_help()
        # parser.parse_args("-V")
        print(default_general["name"] + " " + default_general["version"])
        return False
    if os.sys.argv[1] not in commands:
        logger.error("Command Error! " + os.sys.argv[1] +
                     " is not the available command.\n"
                     "[Tips] Please input correct command such as " + ", ".join(commands) + "!")
        return False
    if len(os.sys.argv) == 2 and (os.sys.argv[1] in commands):
        commands_parser[os.sys.argv[1]].print_help()
        return False
    return parser.parse_args()
