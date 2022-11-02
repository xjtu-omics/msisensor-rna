#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""==============================================================================
# Project: MSIRNA
# Script : train.py
# Author : Peng Jia
# Date   : 2021.03.28
# Email  : pengjia@stu.xjtu.edu.cn
# Description: Train a machine learning model for MSI detection
=============================================================================="""
import os
import pandas as pd
import numpy as np
import pickle
from sklearn import svm, datasets
from sklearn.metrics import *
from msisensor_rna.units import logger

import multiprocessing as mlp
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from scipy.stats import pearsonr
import scipy.stats as stats
from sklearn import metrics
from sklearn.metrics import *
from sklearn.model_selection import cross_val_score, ShuffleSplit

random_state = np.random.RandomState(1)

def get_stat(infos):
    [info, msi_sample, mss_sample, msisensor_scoer, clf_rf, clf_svm] = infos
    # print(info)
    # info = tcga_data[gene]
    median = np.median(info)
    mean = np.mean(info)
    std = np.std(info)
    mut = std / mean
    # info = (info - mean) / std
    info_p = info[msi_sample].tolist()
    info_n = info[mss_sample].tolist()
    median_p = np.median(info_p)
    mean_p = np.mean(info_p)
    std_p = np.std(info_p)
    mut_p = std_p / mean_p
    median_n = np.median(info_n)
    mean_n = np.mean(info_n)
    std_n = np.std(info_n)
    mut_n = std_n / mean_n
    if std_p == 0 and std_n == 0:
        p_MW = 1
    else:
        p_MW = stats.mannwhitneyu(info_p,info_n)[1]
    p_ranksums = stats.ranksums(info_p,info_n)[1]
    y = list(info_p) + list(info_n)
    y_pre = [1] * len(info_p) + [0] * len(info_n)
    auc = metrics.roc_auc_score(y_pre,y)
    auc = 1 - auc if auc < 0.5 else auc
    pearsonr_r, pearsonr_p = pearsonr(info,msisensor_scoer)
    X = np.array(info)
    X = X.reshape(-1,1)
    rf_score = np.mean(cross_val_score(estimator=clf_rf,X=X,y=msisensor_scoer,scoring="r2"))
    svm_score = np.mean(cross_val_score(estimator=clf_svm,X=X,y=msisensor_scoer,scoring="r2"))
    gene_stat = [median, mean, std, mut, median_p, mean_p, std_p, mut_p,
                 median_n, mean_n, std_n, mut_n, p_MW, p_ranksums, auc, pearsonr_r, pearsonr_p,
                 rf_score, svm_score]
    return gene_stat


def select_genes(paras):
    input = paras.input[0]
    positive_num = paras.positive_num[0]
    threads=paras.threads
    output=paras.output[0]
    # print(output)
    output_prefix=output[:-4]+".all.info.csv"
    # print(output_prefix)
    thresh_cov=paras.thresh_cov
    thresh_p=paras.thresh_p_ranksum
    thresh_auc=paras.thresh_AUCscore

    input_df = pd.read_csv(input, index_col=0).dropna()

    genes = input_df.columns.to_list()
    if "msi" not in genes:
        logger.error("Input Error! The input must contain 'msi' information.\n"
                     "[Tips] Please check your input data, make sure you have 'msi' and comma split format!")
    genes.remove("msi")
    msi= input_df["msi"]
    msi_sample = [i for i, j in msi.items() if j in [1, "1", "MSI-H", "MSI", "MSI_H"]]
    mss_sample = [i for i, j in msi.items() if j not in [1, "1", "MSI-H", "MSI", "MSI_H"]]
    # print(msi_status)
    y_label = [1 if f"{i}".upper() in ["MSI", "MSI-H", "MSI_H","1"] else 0 for i in msi]
    if len(msi_sample) < positive_num:
        logger.error("The No. of MSI sample lower than the minimum values, Please set with -p.")

    gene_info = pd.DataFrame(columns=["median", "mean", "std", "mut", "median_p", "mean_p", "std_p", "mut_p",
                                      "median_n", "mean_n", "std_n", "mut_n", "p_MW", "p_ranksums", "auc",
                                      "pearsonr_r", "pearsonr_p", "rf_score", "svm_score"])
    gene_num = 0
    clf_rf = RandomForestClassifier(n_estimators=20, max_depth=4, random_state=random_state)
    clf_svm = svm.SVC()
    win_info = []
    win_genes = []
    total_gene_num = len(genes)
    for gene in genes:
        gene_num += 1
        # print(gene_num, gene)
        info = input_df[gene]
        infos = [info, msi_sample, mss_sample, y_label, clf_rf, clf_svm]
        win_info.append(infos)
        win_genes.append(gene)
        if gene_num % (threads*10) == 0 or gene_num == total_gene_num:
            pool = mlp.Pool(int(f"{threads}"))
            res = pool.map(get_stat, win_info)
            pool.close()
            pool.join()
            for g, i in zip(win_genes, res):
                gene_info.loc[g] = i
            win_genes = []
            win_info = []
    gene_info.to_csv(f"{output_prefix}")
    gene_num = len(gene_info)
    # print(gene_num)
    # gene_info = gene_info.loc[all_tech_overlap_genes, :]
    gene_info["fold"] = np.log2(gene_info["mean_p"] / gene_info["mean_n"])
    rf_score_FQ = gene_info.sort_values("rf_score", ascending=False)["rf_score"].to_list()[gene_num // 4]
    svm_score_FQ = gene_info.sort_values("svm_score", ascending=False)["svm_score"].to_list()[gene_num // 4]
    # print(gene_info["p_ranksums"])
    gene_info = gene_info[
        (gene_info["p_ranksums"] < thresh_p) & (gene_info["p_MW"] < thresh_p)]
    gene_info = gene_info[(gene_info["rf_score"] > rf_score_FQ) & (
            gene_info["svm_score"] > svm_score_FQ)]
    gene_info = gene_info[(gene_info["fold"] > thresh_cov) | (gene_info["fold"] < -thresh_cov)]
    # gene_info = gene_info[gene_info["pearsonr_p"] < 0.001]
    gene_info = gene_info[gene_info["auc"] > thresh_auc]
    gene_info.to_csv(f"{output}")

