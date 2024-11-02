import numpy
import pandas

# 读取CSV文件
data = pandas.read_csv('E:/Project/data/export/FMGC.sp/beijing_1.csv')

# 获取列名
columns = data.columns

sample_ids = data.columns.tolist()

print(sample_ids)
# Load original data
data_covariate = pandas.read_csv('E:/Project/data/export/manifestotype.csv')
print(data_covariate.head())

data_covariate_test = data_covariate[data_covariate['Sample id'].isin(sample_ids)]
print(data_covariate_test)

data_phenotype = pandas.read_csv('E:/Project/data/export/abundance_bj.csv')
print(data_phenotype.head())

# Check the column names to find the correct one
print(data_phenotype.columns)

# Assuming the correct column name is 'Sample id'
data_phenotype_test = data_phenotype[data_phenotype['Genus'].isin(sample_ids)]
print(data_phenotype_test)

# Create phenotype data frame
phenotype = data_phenotype_test.rename(columns={'Genus': 'Family ID'})
phenotype['Individual ID'] = phenotype['Family ID']
phenotype = phenotype[['Family ID', 'Individual ID'] + [col for col in phenotype.columns if col not in ['Family ID', 'Individual ID']]]
print(phenotype.head())

# Save phenotype data to file
phenotype.to_csv('E:/Project/data/plink/Beijing/bj_phenotype.tsv', sep='\t', index=False)

# Create covariant data frame
covariant = data_covariate_test.rename(columns={'Sample id': 'Family ID'})
covariant['Individual ID'] = covariant['Family ID']
covariant = covariant[['Family ID', 'Individual ID'] + [col for col in covariant.columns if col not in ['Family ID', 'Individual ID']]]
print(covariant.head())

# Save covariate data to file
covariant.to_csv('E:/Project/data/plink/Beijing/bj_covariate.tsv', sep='\t', index=False)
