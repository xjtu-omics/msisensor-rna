# MSIsensor-RNA
MSIsensor-RNA is a member of MSIsensor family for microsatellite instability (MSI) detection using RNA sequencing data. MSIsensor-RNA compute MSI by the expression of MSI associated genes. MSIsensor-RNA shows efficient performance in AUC, sensitivity, specificity and robustness. 

## License

MSIsensor-RNA is free for non-commercial use
by academic, government, and non-profit/not-for-profit institutions. A
commercial version of the software is available and licensed through
Xi’an Jiaotong University. For more information, please contact with
Peng Jia (pengjia@stu.xjtu.edu.cn) or Kai Ye (kaiye@xjtu.edu.cn).


## Scopes of MSIsensor-RNA

Microsatellite Instability is an indispensable biomarker in cancer therapies and prognosis, particularly in immunotherapy. Our previous work for MSI detection based on next-generation-sequencing data, MSIsensor and [MSIsensor-pro](https://github.com/xjtu-omics/msisensor-pro), are widely used in clinical research projects. In particular, MSIsensor is the chosen MSI scoring method in the first FDA-approved pan cancer panel, MSK-IMPACT. However, most of those DNA-based methods, including MSIsensor and MSIsensor-pro, quantify MSI evaluation of genome mutations as consequence of MSI status rather than the direct cause of MSI, the deficiency of mismatch repair (MMR) system. In addition, selection of detected microsatellite sites and thresholds for different populations, sequencing panels and cancer types impedes the standardized detection of MSI in clinical. To solve these problems, we launched a new member for MSIsensor family, MSIsensor-RNA, a standalone software for MSI detection with MMR associated genes from tumor RNA sequencing data. MSIsensor-RNA shows efficient performance in AUC, sensitivity, specificity and robustness. MSIsensor-RNA also costs less in aspect of sequencing and computation, and does not need selection of microsatellite sites and threshold for different populations compared to the NGS-based methods, including MSIsensor and MSIsensor-pro.



## How to install MSIsensor-RNA?
  ```
    pip3 install msisensor-rna
  ```
 
## How to use MSI ? 

### Usage:   
   
      msisensor-rna <command> [options]

### Key Commands:

#### **train**
	  
   * **Function**. Train custom model for microsatellite instability detection.
   * **Parameters**     
   	```  
	 -h, --help            show this help message and exit  
	  -i INPUT, --input INPUT  
				The path of input file. [required]  
	  -m MODEL, --model MODEL  
				The trained model of the input file. [required]
	  -t CANCER_TYPE, --cancer_type CANCER_TYPE
				The cancer type for this training. e.g. CRC, STAD, and PanCancer etc.
	  -c {RandomForest,LogisticRegression,MLPClassifier,GaussianNB,AdaBoostClassifier}, --classifier {RandomForest,LogisticRegression,MLPClassifier,GaussianNB,AdaBoostClassifier}
				The machine learning classifier for MSI detection.				[default=RandomForest]
	  -di INPUT_DESCRIPTION, --input_description INPUT_DESCRIPTION
				The description of the input file.
	  -dm MODEL_DESCRIPTION, --model_description MODEL_DESCRIPTION
				Description for this trained model.
	  -p POSITIVE_NUM, --positive_num POSITIVE_NUM
				The minimum positive sample of MSI for training.
				[default=10]
	  -a AUTHOR, --author AUTHOR
				The author who trained the model.
	  -e EMAIL, --email EMAIL
				The email of the author.

	```

#### **show**

    Show the information of the model and add more details.

#### **detection**

	Microsatellite instability detection.


### input and output.

tdb


## Contact

If you have any questions, please contact with Peng Jia (pengjia@stu.xjtu.edu.cn) or Kai Ye (kaiye@xjtu.edu.cn).


