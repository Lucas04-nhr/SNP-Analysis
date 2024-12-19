import pandas as pd
import numpy as np

snp_file = 'result/analysis/gene_allocation/bac_age_significant_snps_BJ.csv'
gene_file = 'result/analysis/snp_allocation/bac_age_BJ_snp.csv'

snp_df = pd.read_csv(snp_file)

gene_df = pd.read_csv(gene_file)


# Remove the first column of snp_df
snp_df = snp_df.iloc[:, 1:]

# Remove "CHR" and "BP" columns from snp_df
snp_df = snp_df.drop(columns=['CHR', 'BP'])

# Rename the "Bacteria_new" column to "Bacteria"
snp_df = snp_df.rename(columns={'Bacteria_new': 'Bacteria'})

# Merge the two dataframes, only keep the rows in the original snp_df
snp_df = pd.merge(snp_df, gene_df, on='SNP', how='left')

# Remove the rows with duplicated SNPs
snp_df = snp_df.drop_duplicates()

# Save the dataframe to a csv file
snp_df.to_csv('result/analysis/gene_allocation/bac_age_BJ_snp_gene.csv', index=False)