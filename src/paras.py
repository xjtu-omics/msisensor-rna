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
from src.units import *


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
    # command detection
    parser_detection = subparsers.add_parser('detection', help='Microsatellite instability detection.')
    parser_detection.description = 'Microsatellite instability detection.'
    commands.append("detection")
    parser_detection.add_argument('-i', '--input', required=True, type=str, nargs=1,
                                  help="The path of input file [required]")
    parser_detection.add_argument('-o', '--output', required=True, type=str, nargs=1,
                                  help="The path of output file prefix [required]")
    parser_detection.add_argument('-m', '--model', required=True, type=str, nargs=1,
                                  help="The path of the microsatellite regions [required]")
    parser_detection.add_argument("-c", "--custom", required=False, type=bool, nargs=1,
                                  choices=[True, False], default=[False],
                                  help="Use custom model, default value [False].")
    parser_detection.add_argument("-cm", "--custom_model", type=str, nargs=1, default=["."],
                                  help="Path of custom model, required if --custom=True.")
    parser_detection.add_argument("-t", "--cancer_type", required=False, type=str, nargs=1,
                                  choices=["CRC", "STAD", "UCEC"], default=["CRC"],
                                  help="Cancer type of the sample.")

    # parser_detection.add_argument('-r', '--reference', required=True, type=str, nargs=1,
    #                               help="The path of reference file [required]")
    commands_parser["detection"] = parser_detection
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
                              help="The cancer type for this training. e.g. CRC, STAD, PanCancer etc. ")
    parser_train.add_argument('-c', '--classifier', required=False, type=str, nargs=1, default=["RandomForest"],
                              choices=["RandomForest", "LogisticRegression", "MLPClassifier", "GaussianNB",
                                       "AdaBoostClassifier"],
                              help="The machine learning classifier for MSI detection.")
    parser_train.add_argument('-di', '--input_description', required=False, type=str, nargs=1, default=["."],
                              help="The description of the input file!")
    parser_train.add_argument("-dm", "--model_description. ", required=False, type=str, nargs=1,
                              default=[""],
                              help="Description for this trained model!")
    commands_parser["train"] = parser_train

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
        # parser.print_help()
        # parser.parse_args()
        return False
    if len(os.sys.argv) == 2 and (os.sys.argv[1] in commands):
        commands_parser[os.sys.argv[1]].print_help()
        return False
    return parser.parse_args()
