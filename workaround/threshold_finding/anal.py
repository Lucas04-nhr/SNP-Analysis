import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split

# Import data
data = pd.read_csv("data/plink/result/plink_anno_merged.csv", sep=",")


