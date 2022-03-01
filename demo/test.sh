msisensor-rna train -i ./train.csv -m demo.pkl -t CRC 
msisensor-rna show -m demo.pkl -g genes.list 
msisensor-rna detection -i ./test.csv -m demo.pkl -o test.output.csv
