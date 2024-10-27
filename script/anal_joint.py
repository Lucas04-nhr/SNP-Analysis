import gwaslab as gl
import numpy as np
import pandas as pd

# Load data
data = pd.read_table('data/plink/result.P5.assoc.linear', sep='\s+')

# Draw the plot
stats = gl.Sumstats(
  data,
  snpid="SNP",
  chrom="CHR",
  pos="BP",
  p="P",
  verbose=False
  )

stats.plot_mqq()
