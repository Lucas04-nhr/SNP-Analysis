import pandas as pd
import numpy as np

# Load the data
result = pd.read_csv('result/analysis/snp_allocation/cov-as-phe_numeric_age_GZ_ori.csv')
bacteria_names = pd.read_csv('result/analysis/top_bacteria/cov_as_phe/phenotype_numeric_GZ.csv')

# Change the content
# Create a dictionary from the bacteria DataFrame for mapping
bacteria_dict = pd.Series(bacteria_names.iloc[:, 1].values, index=bacteria_names.iloc[:, 0]).to_dict()

# Replace the values in the 'Cov' column of the result DataFrame
result['Cov'] = result['Cov'].map(bacteria_dict)

# Save the result
result.to_csv('result/analysis/snp_allocation/cov-as-phe_numeric_age_GZ_rel.csv', index=False)
