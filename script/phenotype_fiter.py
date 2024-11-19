import pandas as pd
import numpy as np

# Load full data
full_data = pd.read_csv('data/plink/PandC/Beijing/phenotype_BJ.tsv', sep='\t')
print(full_data.head())
full_data = full_data.T

# Load the filtered data name
filter = pd.read_csv('data/avg_and_breadth/Beijing_Avg_Breadth_Filtered.csv')
print(filter['Species'].head())

filtered_head = full_data.iloc[:2, :]
filtered_data = full_data[full_data.index.isin(filter['Species'])]
# Keep only the first two rows and columns where the first row is in the filter's Species column
# Combine the head and the data
filtered_data = pd.concat([filtered_head, filtered_data])
filtered_data = filtered_data.T

print(filtered_data.head())

# Save the filtered data
filtered_data.to_csv('data/plink/PandC/Beijing/phenotype_BJ_filtered.tsv', sep='\t', index=False)
