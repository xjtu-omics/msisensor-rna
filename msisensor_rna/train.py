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
import os
import pandas as pd
import numpy as np
import pickle
from sklearn import svm, datasets
from sklearn.metrics import *
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import RandomOverSampler, SMOTE
from collections import Counter
from msisensor_rna.units import logger


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
    classifier_name = paras.classifier[0]
    input_description = paras.input_description[0]
    model_description = paras.model_description[0]
    positive_num = paras.positive_num[0]
    author = paras.author[0]
    email = paras.email[0]

    input_df = pd.read_csv(input, index_col=0).dropna()
    genes = input_df.columns.to_list()
    genes.remove("msi")
    msi_status = input_df["msi"].to_list()
    # print(msi_status)
    y_label = [1 if i.upper() in ["MSI", "MSI-H", "MSI_H"] else 0 for i in msi_status]
    class_num = Counter(y_label)
    if class_num[1] < positive_num:
        logger.error("The No. of MSI sample lower than the minimum values, Please set with -p.")
    x = input_df[genes]
    smo = SMOTE(random_state=1)
    x_balanced, y_label_balanced = smo.fit_resample(x, y_label)
    classifier = build_classrfier(type=classifier_name)
    classifier.fit(x_balanced, y_label_balanced)

    y_pre = classifier.predict(x)
    y_pre_pro = classifier.predict_proba(x)[:, 1]
    roc_auc = roc_auc_score(y_label, y_pre_pro)
    conf_matrix = confusion_matrix(y_label, y_pre, labels=None, sample_weight=None)
    TN = conf_matrix[0][0]
    FN = conf_matrix[1][0]
    TP = conf_matrix[1][1]
    FP = conf_matrix[0][1]
    sensitivity = TP / (TP + FN)
    precision = TP / (TP + FP)
    specificity = TN / (TN + FP)
    f_score1 = f1_score(y_label, y_pre)
    accuracy_score = (TP + TN) / (FN + FP + TN + TP)

    description = {}
    description["Cancer Type"] = cancer_type
    description["Classifier"] = classifier_name
    description["Input Description"] = input_description
    description["Model Description"] = model_description
    description["Available Trained Sample"] = len(input_df)
    description["Positive Sample"] = class_num[1]
    description["Negative Sample"] = class_num[0]
    description["Accuracy"] = accuracy_score
    description["AUC"] = roc_auc
    description["F1 Score"] = f_score1
    description["Sensitivity"] = sensitivity
    description["Specificity"] = specificity
    description["Precision"] = precision
    description["Model Path"] = os.path.abspath(model_path)
    description["Author"] = author
    description["Email"] = email
    for item, value in description.items():
        logger.info(item + ": {}".format(value))
    with open(model_path, 'wb') as f:
        pickle.dump(classifier, f)
        pickle.dump(description, f)
        pickle.dump(genes, f)
