import pandas as pd
import matplotlib.pyplot as plt

# Import data
data_merged_filtered = pd.read_csv('result/analysis/merged_bac_age.csv')
bac_alloc = pd.read_csv('result/analysis/bacteria_allocation_full.csv')
data_merged_filtered = data_merged_filtered.set_index('SNP')

# Change the Cov row to bacteria name
bac_alloc = bac_alloc.set_index('Cov')
data_merged_filtered['Cov'] = data_merged_filtered['Cov'].map(bac_alloc['Species'])

# Change the column order and name
order = ['CHR', 'Cov', 'Ref', 'Alt', 'FDR_BY',
       'Func.refGene', 'Gene.refGene', 'UNADJ', 'GC', 'BONF', 'HOLM', 'SIDAK_SS', 'SIDAK_SD', 'FDR_BH', 
       'GeneDetail.refGene', 'ExonicFunc.refGene', 'AAChange.refGene',
       'CLNALLELEID', 'CLNDN', 'CLNDISDB', 'CLNREVSTAT', 'CLNSIG', 'ONCDN',
       'ONCDISDB', 'ONCREVSTAT', 'ONC', 'SCIDN', 'SCIDISDB', 'SCIREVSTAT',
       'SCI', 'avsnp150', 'ALL.sites.2015_08']
data_merged_filtered = data_merged_filtered[order]
data_merged_filtered = data_merged_filtered.rename(columns={'Cov': 'Bacteria'})

# Drop the rows which CHR is not a number
data_merged_filtered = data_merged_filtered[data_merged_filtered['CHR'].apply(lambda x: x.isnumeric())]
data_merged_filtered['CHR'] = data_merged_filtered['CHR'].astype(int)
data_merged_filtered = data_merged_filtered.sort_values(by=['CHR', 'FDR_BY'], ascending=[True, True])

# Save the data
data_merged_filtered.to_csv('result/analysis/merged_bac_age_filtered.csv', index=True)
