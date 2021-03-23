#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""==============================================================================
# Project: MSIRNA
# Script : msirna.py
# Author : Peng Jia
# Date   : 2021.03.19
# Email  : pengjia@stu.xjtu.edu.cn
# Description: TODO
=============================================================================="""
import sys
import os

# sys.path.append("/public/ProjectBaseCall/code/ProjectBaseCall/0_data_preprocessing")
curpath = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path.append(os.path.dirname(curpath))

from src.paras import *
from src.detection import *


def main():
    parase = args_process()
    if parase:
        print(parase)
        if parase.command == "detection":
            detection_msi()

    pass


if __name__ == "__main__":
    # print("hhh")
    main()
    pass
