import numpy
import pandas
import matplotlib.pyplot as plt

# Load the dataset
full_data = pandas.read_csv('../data_export/manifestotype.csv')

# Filter the data
bj_data = full_data[full_data['Region'] == 'Beijing']

# Gloss data analysis - pie chart
plt.figure(figsize=(10, 5), dpi=300)
gloss_data = bj_data['Gloss'].value_counts()
gloss_data = bj_data['Gloss'].dropna().astype(float)
bins = [0, 2, 4, 6, 8, 10, float('inf')]
labels = ['0-2', '2-4', '4-6', '6-8', '8-10', '>10']
gloss_data_binned = pandas.cut(gloss_data, bins=bins, labels=labels, right=False)
gloss_data_binned_counts = gloss_data_binned.value_counts().sort_index()
gloss_data_binned_counts.plot.pie(autopct='%1.1f%%')
plt.title('Gloss Data Analysis')
plt.ylabel('')
plt.show()

