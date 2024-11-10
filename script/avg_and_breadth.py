import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
avg_data = pd.read_csv('data/avg_and_breadth/Beijing_Avg.csv')
breadth_data = pd.read_csv('data/avg_and_breadth/Beijing_breadth.csv')

# Merge data
data = pd.merge(avg_data, breadth_data, on='Species', how='inner')
print(data.head())
count = data[(data['Avg'] > 0.005) & (data['Breadth'] > 150)].shape[0]
print(f"Count of data with Avg > 0.005 and Breadth > 150: {count}")

# Save the data
data_filtered = data[(data['Avg'] > 0.005) & (data['Breadth'] > 150)]
data_filtered.to_csv('data/avg_and_breadth/Beijing_Avg_Breadth_Filtered.csv', index=False)

# Plot
plt.figure(figsize=(10, 10), dpi=300)
plt.scatter(data_filtered['Avg'], data_filtered['Breadth'], color='blue', alpha=0.5)
plt.xlabel('Average abundance')
plt.ylabel('Breadth')
plt.title('Average abundance and Breadth of Species in Beijing')
plt.savefig('result/avg_and_breadth_in_BJ.pdf')
