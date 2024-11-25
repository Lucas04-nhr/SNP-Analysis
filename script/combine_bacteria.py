import pandas as pd
import numpy as np

# Load the data
result = pd.read_csv('result/analysis/merged_c004_GZ.csv')
bacteria_names = pd.read_csv('result/analysis/bacteria_GZ.csv')

# Change the content
# Create a dictionary from the bacteria DataFrame for mapping
bacteria_dict = pd.Series(bacteria_names.iloc[:, 1].values, index=bacteria_names.iloc[:, 0]).to_dict()

# Replace the values in the 'bacteria' column of the result DataFrame
result['Bacteria'] = result['Bacteria'].map(bacteria_dict)

# Save the result
result.to_csv('result/analysis/04_age_GZ.csv', index=False)
