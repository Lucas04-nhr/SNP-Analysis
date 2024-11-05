import pandas as pd
import subprocess

# Local
sample_path = "data/plink/anal/converted_genotyped"
known_snp = "data/plink/anal/Skin_A_autosome.tsv"
filtered_snp = "data/plink/anal/filtered_sample"


# Server
# sample_path = "/mnt/raid6/bacphagenetwork/data/12_plink/Guangzhou/converted_genotyped"
# known_snp = "/mnt/raid6/bacphagenetwork/data/11_Known_SNPs/Skin_A_autosome.tsv"
# filtered_snp = "/mnt/raid6/bacphagenetwork/data/12_plink/Guangzhou/results/filtered_sample"

# 提取已知SNP位置
input_file = known_snp
data = pd.read_csv(input_file, sep='\t', header=0)
known_data = data[['chromosome', 'base_pair_location']]

# 将元素转换为适当类型
known_data['chromosome'] = known_data['chromosome'].astype(str)
known_data['base_pair_location'] = known_data['base_pair_location'].astype(int)
known_data['base_pair_end_location'] = known_data['base_pair_location']

# 保存为新的txt文件
output_file = "data/plink/anal/knownSNPa.csv"
known_data.to_csv(output_file, sep=',', header=False, index=False)

print(f"Filtered known SNP saved to {output_file}")
print(known_data.head())

output_filtered = "data/plink/anal/knownSNP_chr1.csv"
known_data[known_data['chromosome'] == '1'].to_csv(output_filtered, sep=',', header=False, index=False)

print(f"Filtered known SNP saved to {output_filtered}")
print(known_data[known_data['chromosome'] == '1'].head())

# 定义plink
plink_path = "bin/plink/plink"
plink_command = f"{plink_path} --bfile {sample_path} --extract {output_filtered} --allow-extra-chr --recode --out {filtered_snp}"

# 检查命令
print(f"PLINK command: \n {plink_command}")

# 运行PLINK命令
subprocess.run(plink_command, shell=True)