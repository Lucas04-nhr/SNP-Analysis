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

# Sort by Age
manifestotype_bj = manifestotype_bj.sort_values(by='Age')
manifestotype_gz = manifestotype_gz.sort_values(by='Age')
manifestotype_all = manifestotype_all.sort_values(by='Age')


# Dot plot of Beijing Age-Moisture relations
plt.figure(figsize=(12, 8), dpi=100)
plt.scatter(manifestotype_bj['Age'], manifestotype_bj['Moisture'], c='red', alpha=0.5, s=20)
plt.scatter(manifestotype_gz['Age'], manifestotype_gz['Moisture'], c='blue', alpha=0.5, s=20)
plt.title('Age-Moisture Relations of Samples in Beijing and Guangzhou')
plt.xlabel('Age')
plt.ylabel('Moisture')
ages = sorted(manifestotype_all['Age'].unique())
plt.gca().set_xticks(ages[::5]) # Set x-axis ticks to show every 5th age value
plt.gca().set_yticks([]) # Hide y-axis ticks
plt.legend(['Beijing', 'Guangzhou'], loc='lower right')

plt.savefig('result/essay/age_moisure.pdf')
# plt.show()
