#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""==============================================================================
# Project: MSIRNA
# Script : train.py
# Author : Peng Jia
# Date   : 2021.03.28
# Email  : pengjia@stu.xjtu.edu.cn
# Description: TODO
=============================================================================="""
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import svm, datasets
from sklearn.metrics import *
from sklearn.metrics import plot_roc_curve
from sklearn.metrics import plot_precision_recall_curve
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from imblearn.over_sampling import RandomOverSampler, SMOTE
from collections import Counter

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import os

# from sklearn.externals import joblib
import pickle


def build_classrfier(type="RandomForest"):
    random_state = np.random.RandomState(1)
    if type == "SVM":
        classifier = svm.SVC(kernel='linear', probability=True,
                             random_state=random_state)
    elif type == "LogisticRegression":
        classifier = LogisticRegression(C=1.0, penalty='l1', tol=0.0001, solver='saga')
    elif type == "MLPClassifier":
        classifier = MLPClassifier(solver='lbfgs', alpha=1e-6,
                                   hidden_layer_sizes=(20, 10, 5), random_state=1)
    elif type == "GaussianNB":
        classifier = GaussianNB()
    elif type == "RandomForest":
        classifier = RandomForestClassifier(n_estimators=700, oob_score=True)
    elif type == "AdaBoostClassifier":
        classifier = AdaBoostClassifier(n_estimators=1000)

    return classifier


def train_model(paras):
    input = paras.input[0]
    model_path = paras.model[0]
    cancer_type = paras.cancer_type[0]
    classifier = paras.classifier[0]
    input_description = paras.input_description[0]
    model_description = paras.model_description[0]
    input_df = pd.read_csv(input, index_col=0)
    genes = input_df.columns.to_list().remove("msi")
    msi_status = input_df["msi"].to_list()
    y_label = [1 if i.upper() in ["MSI", "MSI-H", "MSI_H"] else 0 for i in msi_status]
    print(Counter)
    x = input_df[genes]
    smo = SMOTE(random_state=42)
    x_balanced, y_label_balanced = smo.fit_resample(x, y_label)
