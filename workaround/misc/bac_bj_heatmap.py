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
bacteria_bj = pd.read_csv('data/export/FMGC.ge/Beijing.csv', index_col=0)
bacteria_bj = bacteria_bj.apply(pd.to_numeric, errors='coerce').fillna(0)
print(bacteria_bj.head())

# Draw the heatmap
plt.figure(figsize=(8, 8), dpi=100)
plt.imshow(bacteria_bj, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap of Bacteria in Beijing')
plt.xlabel('Samples')
plt.ylabel('Bacteria')
# plt.savefig('result/essay/bacteria_bj_heatmap.pdf')
plt.show()
