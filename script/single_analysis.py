# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Load FMGC.ge data
data = pd.read_csv('../data_export/FMGC.ge/Beijing.csv')
print(data.head())

# Only keep the first two columns that are from BJ001
data_bj001 = data.iloc[:, 0:2]
# Sort the data by the second column, descending
data_bj001 = data_bj001.sort_values(by=data_bj001.columns[1], ascending=False)
print(data_bj001.head())


# Plot the barplot
plt.figure(figsize=(10, 10), dpi=30)
plt.bar(data_bj001.iloc[0:10, 0], data_bj001.iloc[0:10, 1])
plt.xlabel('Genius Data')
plt.ylabel('Abundance')
plt.xticks(rotation=45)
plt.title('Top 10 most frequent values in BJ001')
plt.show()
