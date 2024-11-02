import numpy as np
import pandas as pd

# Test IDs
data = pd.read_csv('data/export/FMGC.sp/Beijing.csv')
test_ids = data.columns.tolist()

# Load original data
data_covariate = pandas.read_csv('data/export/manifestotype.csv')
print(data_covariate.head())

data_covariate_test = data_covariate[data_covariate['Sample id'].isin(test_ids)]
print(data_covariate_test)

data_phenotype = pandas.read_csv('data/export/abundance_bj.csv')
print(data_phenotype.head())

# Check the column names to find the correct one
print(data_phenotype.columns)

# Assuming the correct column name is 'Sample id'
data_phenotype_test = data_phenotype[data_phenotype['Genus'].isin(test_ids)]
print(data_phenotype_test)

# Create phenotype data frame
phenotype = data_phenotype_test.rename(columns={'Genus': 'Family ID'})
phenotype['Individual ID'] = phenotype['Family ID']
phenotype = phenotype[['Family ID', 'Individual ID'] + [col for col in phenotype.columns if col not in ['Family ID', 'Individual ID']]]
print(phenotype.head())

# Save phenotype data to file
phenotype.to_csv('data/plink/phenotype.tsv', sep='\t', index=False)

# Create covariant data frame
covariant = data_covariate_test.rename(columns={'Sample id': 'Family ID'})
covariant['Individual ID'] = covariant['Family ID']
covariant = covariant[['Family ID', 'Individual ID'] + [col for col in covariant.columns if col not in ['Family ID', 'Individual ID']]]
print(covariant.head())

# Save covariate data to file
covariant.to_csv('data/plink/covariate.tsv', sep='\t', index=False)
