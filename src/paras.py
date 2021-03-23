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


# from src.benchmark import *
# from src.genotype import *
# from src.qc import *
# from src.benchmark_merge import benchmark_merge

# logger.info(" ".join(sys.argv))


def args_process():
    """
    argument procress
    """
    # defaultPara =
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
    # add arguments for genotype module
    parser_detection = subparsers.add_parser('detection', help='Microsatellite instability detection.')
    parser_detection.description = 'Microsatellite instability detection.'
    commands.append("detection")
    ##################################################################################
    # group input and output
    # input_and_output = parser_detection.add_argument_group(title="Input and output")
    parser_detection.add_argument('-i', '--input', required=True, type=str, nargs=1,
                                  help="The path of input file [required]")
    parser_detection.add_argument('-o', '--output', required=True, type=str, nargs=1,
                                  help="The path of output file prefix [required]")
    parser_detection.add_argument("-c", "--custom", required=False, type=str, nargs=1,
                                  choices=[True, False],
                                  help="Use custom model, default value [False].")
    parser_detection.add_argument("-cm", "--custom_model", type=str, nargs=1,
                                  help="Path of custom model, required if --custom=True.")
    parser_detection.add_argument("-t", "--cancer_type", required=False, type=str, nargs=1,
                                  choices=["CRC", "STAD", "UCEC"],
                                  help="Cancer type of the sample.")
    parser_detection.add_argument('-m', '--model', required=False, type=str, nargs=1,
                                  help="The path of the microsatellite regions [required]")
    # parser_detection.add_argument('-r', '--reference', required=True, type=str, nargs=1,
    #                               help="The path of reference file [required]")
    commands_parser["detection"] = parser_detection
    ##################################################################################

    if len(os.sys.argv) < 2:
        parser.print_help()
        return False

    if os.sys.argv[1] in ["-h", "--help", "-?"]:
        parser.print_help()
        return False
    if os.sys.argv[1] in ["-V", "-v", "--version"]:
        # parser.print_help()
        parser.parse_args()
        return False
    if os.sys.argv[1] not in commands:
        logger.error("Command Error! " + os.sys.argv[1] +
                     " is not the available command.\n"
                     "[Tips] Please input correct command such as " + ", ".join(commands) + "!")
        parser.print_help()
        # parser.parse_args()
        return False
    if len(os.sys.argv) == 2 and (os.sys.argv[1] in commands):
        commands_parser[os.sys.argv[1]].print_help()
        return False
    return parser.parse_args()
