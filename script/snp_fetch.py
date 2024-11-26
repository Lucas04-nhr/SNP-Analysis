from Bio import Entrez, SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import requests
import argparse
import pandas as pd
import numpy as np

# 设置 Entrez 的电子邮件
Entrez.email = "lucas04@hust.edu.cn"

def read_snp_data(input_file):
  # Read SNP data from a CSV file
  data = pd.read_csv(input_file)
  snp_list = []
  for index, row in data.iterrows():
    snp_data = row["SNP"].split(":")
    snp["chromosome"] = snp_data[0]
    snp["position"] = int(snp_data[1])
    snp_list.append(snp)
  return snp_list

def fetch_known_snps(chromosome, position):
  # Fetch known SNPs from dbSNP
  handle = Entrez.esearch(db="snp", term=f"{chromosome}[Chromosome] AND {position}[Base Position]")
  record = Entrez.read(handle)
  if record["IdList"]:
    return True
  else:
    return False


def fetch_gene_annotations(chromosome, position):
  # Fetch gene annotations from NCBI
  url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&id={chromosome}&rettype=gb&retmode=text"
  response = requests.get(url)
  if response.status_code == 200:
    record = SeqIO.read(response.text, "genbank")
    for feature in record.features:
      if feature.type == "gene":
        if position in feature.location:
          gene_id = feature.qualifiers.get("db_xref", [None])[0]
          if gene_id:
              gene_id = gene_id.split(":")[1]
          taxon = feature.qualifiers.get("taxon", [None])[0]
          return gene_id, taxon
  return None, None


# Phase the arguments
parser = argparse.ArgumentParser(description="Fetch SNP data from a CSV file.")
parser.add_argument("--input-file", help="Input CSV file containing SNP data.", required=True)
parser.add_argument("--output-file", help="Output CSV file to save the results.", required=True)
args = parser.parse_args()

# Save the arguments
input_file = args.input_file
output_file = args.output_file

# Read SNP data from a CSV file
snp_data = read_snp_data(input_file)

for snp in snp_data:
  chromosome = snp["chromosome"]
  position = snp["position"]

  # Check if the SNP is a known SNP
  known_snp = fetch_known_snps(chromosome, position)

  if known_snp:
    snp_data["known_snp"] = "Yes"
  else:
    snp_data["known_snp"] = "No"

  # Fetch gene annotations
  gene_info = fetch_gene_annotations(chromosome, position)
  if gene_info:
    snp_data["gene_id"] = gene_info[0]
    snp_data["taxon"] = gene_info[1]
  else:
    snp_data["gene_id"] = None
    snp_data["taxon"] = None

# Save the results to a CSV file
output_data = pd.DataFrame(snp_data)
output_data.to_csv(output_file, index=False)




