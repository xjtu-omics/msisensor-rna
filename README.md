
![GitHub last commit](https://img.shields.io/github/last-commit/xjtu-omics/msisensor-rna)
[![GitHub Release Date](https://img.shields.io/github/release-date/xjtu-omics/msisensor-rna)](https://github.com/xjtu-omics/msisensor-rna/releases)
[![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/xjtu-omics/msisensor-rna?include_prereleases)](https://github.com/xjtu-omics/msisensor-rna/releases)
[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/pengjia1110/msisensor-rna)](https://hub.docker.com/repository/docker/pengjia1110/msisensor-rna)
![Docker Pulls](https://img.shields.io/docker/pulls/pengjia1110/msisensor-rna)
![GitHub all releases](https://img.shields.io/github/downloads/xjtu-omics/msisensor-rna/total?label="Github")

![PyPI](https://img.shields.io/pypi/v/msisensor-rna) 



# MSIsensor-RNA
MSIsensor-RNA is a member of MSIsensor family for microsatellite instability (MSI) detection using RNA sequencing data. MSIsensor-RNA compute MSI by the expression of MSI associated genes. MSIsensor-RNA shows efficient performance in AUC, sensitivity, specificity and robustness. 

---
## Authors
  * Pengjia (pengjia@stu.xjtu.edu.cn)
  * Xuanhao Yang (xuanhaoyang@stu.xjtu.edu.cn)
  * Xiaofei Yang (xfyang@xjtu.edu.cn)
  * Kai Ye (kaiye@xjtu.edu.cn)
 ---
## License

MSIsensor-RNA is free for non-commercial use
by academic, government, and non-profit/not-for-profit institutions. A
commercial version of the software is available and licensed through
Xi’an Jiaotong University. For more information, please contact with
Peng Jia (pengjia@stu.xjtu.edu.cn) or Kai Ye (kaiye@xjtu.edu.cn).

---
## Scopes of MSIsensor-RNA

Microsatellite Instability is an indispensable biomarker in cancer therapies and prognosis, 
particularly in immunotherapy. Our previous work for MSI detection based on 
next-generation-sequencing data, MSIsensor and 
[MSIsensor-pro](https://github.com/xjtu-omics/msisensor-pro), are widely used in clinical 
research projects. In particular, MSIsensor is the chosen MSI scoring method in the first 
FDA-approved pan cancer panel, MSK-IMPACT. However, most of those DNA-based methods, 
including MSIsensor and MSIsensor-pro, quantify MSI evaluation of genome mutations as 
consequence of MSI status rather than the direct cause of MSI, the deficiency of mismatch 
repair (MMR) system. In addition, selection of detected microsatellite sites and thresholds 
for different populations, sequencing panels and cancer types impedes the standardized 
detection of MSI in clinical. To solve these problems, we launched a new member for 
MSIsensor family, MSIsensor-RNA, a standalone software for MSI detection with MMR 
associated genes from tumor RNA sequencing data. MSIsensor-RNA shows efficient 
performance in AUC, sensitivity, specificity and robustness. MSIsensor-RNA also costs 
less in aspect of sequencing and computation, and does not need selection of 
microsatellite sites and threshold for different populations compared to the NGS-based 
methods, including MSIsensor and MSIsensor-pro.


---
## How to install MSIsensor-RNA?

### Install with pip3   
  ```shell script
    conda create -n myenv python>=3.6
    conda activate myenv
    pip3 install msisensor-rna
  ```
### Install with docker   
  ```shell script
      docker pull pengjia1110/msisensor-rna
      docker run -v /local/path:/docker/path pengjia1110/msisensor-rna msisensor-rna
  ```
--- 
## How to use MSI ? 

### Usage:   
   ```shell script
    msisensor-rna <command> [options]
```

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
                            The cancer type for this training. e.g. CRC, STAD,
                            PanCancer etc.
      -c {RandomForest,LogisticRegression,MLPClassifier,GaussianNB,AdaBoostClassifier}, --classifier {RandomForest,LogisticRegression,MLPClassifier,GaussianNB,AdaBoostClassifier}
                            The machine learning classifier for MSI detection.
                            [default = RandomForest]
      -di INPUT_DESCRIPTION, --input_description INPUT_DESCRIPTION
                            The description of the input file. [default = None]
      -dm MODEL_DESCRIPTION, --model_description MODEL_DESCRIPTION
                            Description for this trained model.
      -p POSITIVE_NUM, --positive_num POSITIVE_NUM
                            The minimum positive sample of MSI for training.
                            [default = 10]
      -a AUTHOR, --author AUTHOR
                            The author who trained the model. [default = None]
      -e EMAIL, --email EMAIL
                            The email of the author. [default = None]

	    ```

#### **show**
   * **Function**.     Show the information of the model and add more details.

   * **Parameters**  
     ```
      -h, --help            show this help message and exit
      -m MODEL, --model MODEL
                            The trained model path. [required]
      -t CANCER_TYPE, --cancer_type CANCER_TYPE
                            Rename the cancer type. e.g. CRC, STAD, PanCancer etc.
                            [default = None]
      -di INPUT_DESCRIPTION, --input_description INPUT_DESCRIPTION
                            Add description for the input file. [default = None]
      -dm MODEL_DESCRIPTION, --model_description MODEL_DESCRIPTION
                            Add description for this trained model. [default = None]
      -g GENE_LIST, --gene_list GENE_LIST
                            The path for the genes must be included for this
                            model. [default = None]

      ```


#### **detection**
  * **Function**. 	Microsatellite instability detection.

  * **Parameters**  
  
      ```
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            The path of input file. [required]
      -o OUTPUT, --output OUTPUT
                            The path of output file prefix. [required]
      -m MODEL, --model MODEL
                            The path of the microsatellite regions. [required]
      -d RUN_DIRECTLY, --run_directly RUN_DIRECTLY
                            Run the program directly without any Confirm. [default = False]
    ```

---
## Input and output

  * The input file for model training. (-i option in train command)
  
       You need to prepare your training file with a comma separated format (csv). 
       The first columns should be sample id, the second columns should be msi status, 
       and the third and other columns should be gene expression values. We recommend 
       you provide a normalized expression values. (like z-score normalization with log2(FPKM+1) )
       
       The following is an example:
       
    |  SampleID   | msi  | MLH1|LINC01006| ...| NHLRC1|
    |  ----  | ----  | ---- | ----|  ---- | ----|
    | NA0001  | MSI-H | 0.209|1.209|...|0.393|
    | CA0002  | MSS |5.690|0.620|...|4.902|
    | ...  | ... |...|...|...|...|
    | CA10 0  | MSS |9.960|0.920|...|5.002|
  * The trained model (-m option in train, show and detection command)
  
    The trained model is saved as pickle file. In train command, we recommend you add more 
    description by -di,-dm,-a,-e, so that others who used this model are able to get more information.
    In show command, you can get the information of your model , and changed some descriptions by -di and  -dm.
    you can also use -g option to output the genes list this model needed to a file. 
    In detection command, you must check the model and input Yes or No to continue the predict step use *-d True* 
    to ignore this reminder.      
  
  
   
  * The input file for the detection command (-i option in detection command)    
  
      You need to prepare your input file for MSI prediction with a comma separated format (csv). 
       The first columns should be sample id, the second and other columns should be gene expression values.
       The genes name must contain the genes in the model (use -g option of show command to see the genes 
       list of the model).  
       The following is an example:
       
    |  SampleID   | MLH1|LINC01006| ...| NHLRC1|
    |  ----  | ---- | ----|  ---- | ----|
    | NA0001|  0.209|1.209|...|0.393|
    | CA0002 |5.690|0.620|...|4.902|
    | ...   |...|...|...|...|
    | CA100|9.960|0.920|...|5.002|
  
---

## Contact

If you have any questions, please contact with Peng Jia (pengjia@stu.xjtu.edu.cn) or Kai Ye (kaiye@xjtu.edu.cn).


