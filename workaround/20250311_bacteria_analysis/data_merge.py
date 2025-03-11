import pandas as pd
import sys

# Save data
def save_data():
  save_all = input("Do you want to save the merged data to 'result/analysis/merged_bac_age_all.csv'? (y/n): ").strip().lower()
  if save_all == 'y':
    merged_data.to_csv('result/analysis/merged_bac_age_all.csv', index=True)
    print("Merged data saved to 'result/analysis/merged_bac_age_all.csv'")
  elif save_all == 'n':
    print("Merged data not saved")
  else:
    print("Invalid input. Merged data not saved")
    raise ValueError("Invalid input")

  save_common = input("Do you want to save the common data to 'result/analysis/merged_bac_age.csv'? (y/n): ").strip().lower()
  if save_common == 'y':
    common_data.to_csv('result/analysis/merged_bac_age.csv', index=True)
    print("Common data saved to 'result/analysis/merged_bac_age.csv'")
  elif save_common == 'n':
    print("Common data not saved")
  else:
    print("Invalid input. Common data not saved")
    raise ValueError("Invalid input")
  print("Done")


# Import data
data = pd.read_csv('result/analysis/filtered_bac_age.csv')
anno = pd.read_csv('result/analysis/full_annotated_results.hg38_multianno.csv')

# Add SNP row of anno
anno['SNP'] = anno['Chr'].astype(str) + ':' + anno['Start'].astype(str)
data = data.set_index('SNP')
anno = anno.set_index('SNP')
anno.drop(columns=['Chr', 'Start', 'End'], inplace=True)

# Merge data
merged_data = pd.merge(data, anno, on='SNP', how='left')
nrow = merged_data.shape[0]
print(f'Merged data has {nrow} rows')

# Common data
common_data = merged_data.dropna(subset=['Func.refGene'])
nrow = common_data.shape[0]
print(f'Common data has {nrow} rows')

# Save data
save_data()
