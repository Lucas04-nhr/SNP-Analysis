import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Set the font
plt.rcParams['font.sans-serif'] = ['Roobert']
plt.rcParams['font.serif'] = ['FandolSong']
plt.rcParams['font.monospace'] = ['Maple Mono NF CN']
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 0.5

# Load the data
manifestotypes = pd.read_csv('data/export/manifestotype.csv')

# Filter out the age column by the First 2 letters of "Sample id"
manifestotype_bj = manifestotypes[manifestotypes['Sample id'].str[:2] == 'BJ']
manifestotype_gz = manifestotypes[manifestotypes['Sample id'].str[:2] == 'GZ']
manifestotype_all = pd.concat([manifestotype_bj, manifestotype_gz])

# Set age groups
bins = [18, 25, 35, 45, 55, np.inf]
labels = ['18-24', '25-34', '35-44', '45-54', '55+']

# Convert the 'Age' column to numeric values, forcing errors to NaN
manifestotype_bj['Age'] = pd.to_numeric(manifestotype_bj['Age'], errors='coerce')
manifestotype_gz['Age'] = pd.to_numeric(manifestotype_gz['Age'], errors='coerce')
manifestotype_all['Age'] = pd.to_numeric(manifestotype_all['Age'], errors='coerce')

# Drop rows with NaN values in 'Age' column
manifestotype_bj = manifestotype_bj.dropna(subset=['Age'])
manifestotype_gz = manifestotype_gz.dropna(subset=['Age'])
manifestotype_all = manifestotype_all.dropna(subset=['Age'])

# Create a new column with the age group
manifestotype_bj['Age_group'] = pd.cut(manifestotype_bj['Age'], bins=bins, labels=labels)
manifestotype_gz['Age_group'] = pd.cut(manifestotype_gz['Age'], bins=bins, labels=labels)
manifestotype_all['Age_group'] = pd.cut(manifestotype_all['Age'], bins=bins, labels=labels)

# Create a pie chart of the age distribution for Beijing
age_distribution_bj = manifestotype_bj['Age_group'].value_counts().sort_index()
plt.figure(figsize=(12, 8), dpi=100)
plt.pie(age_distribution_bj, labels=age_distribution_bj.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Age Distribution of Samples in Beijing')
plt.legend(age_distribution_bj.index, loc="lower right", title="Age Range")
plt.axis('equal')
plt.savefig('result/essay/age_distribution_bj.pdf')
# plt.show()

# Create a pie chart of the age distribution for Guangzhou
age_distribution_gz = manifestotype_gz['Age_group'].value_counts().sort_index()
plt.figure(figsize=(12, 8), dpi=100)
plt.pie(age_distribution_gz, labels=age_distribution_gz.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Age Distribution of Samples in Guangzhou')
plt.legend(age_distribution_gz.index, loc="lower right", title="Age Range")
plt.axis('equal')
plt.savefig('result/essay/age_distribution_gz.pdf')
# plt.show()

# Create a pie chart of the age distribution for all samples
age_distribution_all = manifestotype_all['Age_group'].value_counts().sort_index()
plt.figure(figsize=(12, 8), dpi=100)
plt.pie(age_distribution_all, labels=age_distribution_all.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Age Distribution of All Samples')
plt.legend(age_distribution_all.index, loc="lower right", title="Age Range")
plt.axis('equal')
plt.savefig('result/essay/age_distribution_all.pdf')
# plt.show()
