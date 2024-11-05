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
known_data = data[['chromosome', 'base_pair_location', 'base_pair_location']]

# 将元素转换为适当类型
known_data['chromosome'] = known_data['chromosome'].astype(str)
known_data['base_pair_location'] = known_data['base_pair_location'].astype(int)

# 保存为新的txt文件
output_file = "data/plink/anal/knownSNPa.csv"
known_data.to_csv(output_file, sep=',', header=True, index=False)

print(f"Filtered known SNP saved to {output_file}")

print(known_data.head())

# 定义plink命令
plink_command = f"plink --bfile {sample_path} --extract range {output_file} --allow-extra-chr --recode --out {filtered_snp}"

# 检查命令
print(f"PLINK command: {plink_command}")

# 运行PLINK命令
subprocess.run(plink_command, shell=True)