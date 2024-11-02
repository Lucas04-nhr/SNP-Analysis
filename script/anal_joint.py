import gwaslab as gl
import numpy as np
import pandas as pd
import os
import argparse
import re

# Get the list of files
file_list = os.listdir('data/plink/filtered/c05')
file_list = [f for f in file_list if f.endswith('.assoc.linear')]


# Loop through multiple files and draw plots
for file_name in file_list:
  print (f'Processing {file_name}')
  file_path = os.path.join('data/plink/filtered/c05', file_name)
  
  # Load data
  data = pd.read_table(file_path, sep='\s+')
  
  # Draw the plot
  stats = gl.Sumstats(
    data,
    snpid="SNP",
    chrom="CHR",
    pos="BP",
    p="P",
    verbose=False
  )
  
  # Extract the number from the file name
  i = re.search(r'\d+', file_name).group()
  output_path = f'result/filtered/c05/joint_mqq_plot_P{i}.png'
  stats.plot_mqq(
    save=output_path,
    save_args={"dpi": 300, "facecolor": "white"}
  )
