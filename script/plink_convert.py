import numpy as np
import pandas as pd

data_bj = pd.read_csv("data/plink/filtered_p_and_c/bacteriaFilteredData/BJ_phenotype.csv", sep=',', header=0)
data_gz = pd.read_csv("data/plink/filtered_p_and_c/bacteriaFilteredData/GZ_phenotype.csv", sep=',', header=0)

# rename the first row
data_bj.rename(columns={data_bj.columns[0]: "Family ID"}, inplace=True)
data_gz.rename(columns={data_gz.columns[0]: "Family ID"}, inplace=True)

# duplicate the first column, insert it as the first column
data_bj.insert(0, "Duplicate Family ID", data_bj.iloc[:, 0])
data_gz.insert(0, "Duplicate Family ID", data_gz.iloc[:, 0])

# rename the new first row to "Individual ID"
data_bj.rename(columns={data_bj.columns[0]: "Individual ID"}, inplace=True)
data_gz.rename(columns={data_gz.columns[0]: "Individual ID"}, inplace=True)



# export to tsv

data_bj.to_csv("data/plink/filtered_p_and_c/bacteriaFilteredData/phenotype_BJ.tsv", sep='\t', header=True, index=False)
data_gz.to_csv("data/plink/filtered_p_and_c/bacteriaFilteredData/phenotype_GZ.tsv", sep='\t', header=True, index=False)
