import gwaslab as gl
import numpy as np
import pandas as pd

# Load data
data = pd.read_table('data/plink/result.P5.assoc.linear', sep='\s+')
print(data.head())
