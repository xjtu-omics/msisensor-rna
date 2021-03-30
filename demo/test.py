# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""==============================================================================
# Project: MSIRNA
# Script : test.py
# Author : Peng Jia
# Date   : 2021.03.28
# Email  : pengjia@stu.xjtu.edu.cn
# Description: TODO
=============================================================================="""
import pandas as pd

df = pd.read_csv("/mnt/project/ProjectMSI/MSI_RNA/software/MSIRNA/demo/TCGA.STAD.independent.mean.100.csv", index_col=0)
df_case = pd.read_csv("/mnt/project/ProjectMSI/MSI_RNA/software/MSIRNA/demo/caseinfo.TCGA.STAD.csv", index_col=0)
df["msi"] = df_case["msi"]
df.to_csv("/mnt/project/ProjectMSI/MSI_RNA/software/MSIRNA/demo/input.csv")

print(df)
