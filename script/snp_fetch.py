from Bio import Entrez, SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import requests
import argparse
import pandas as pd
import numpy as np

# Set the email address for NCBI Entrez
Entrez.email = "lucas04@hust.edu.cn"

def internet_check():
  # Check Internet connection
  try:
    requests.get("http://cp.cloudflare.com/generate_204")
  except requests.ConnectionError:
    print("No Internet connection. Please check your network settings.")
    exit(1)
  print("Internet connection is OK.")

def read_snp_data(input_file):
  # Read SNP data from a CSV file
  data = pd.read_csv(input_file)
  snp_list = []
  for index, row in data.iterrows():
    snp_data = row["SNP"].split(":")
    snp = {}
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
  position = int(position)
  # Fetch gene annotations from NCBI
  base_url = "https://rest.ensembl.org/overlap/region/human/"
  position_below_threshold = (position // 100) * 100
  position_above_threshold = position_below_threshold + 100
  other_args = "feature=gene;content-type=application/json"
  url = f"{base_url}{chromosome}:{position_below_threshold}-{position_above_threshold}?{other_args}"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    if data:
      return data[0]["gene_id"]
    else:
      return None
  else:
    return None


# Phase the arguments
parser = argparse.ArgumentParser(description="Fetch SNP data from a CSV file.")
parser.add_argument("--input-file", help="Input CSV file containing SNP data.", required=True)
parser.add_argument("--output-file", help="Output CSV file to save the results.", required=True)
args = parser.parse_args()

# Save the arguments
input_file = args.input_file
output_file = args.output_file

# Check Internet connection
internet_check()


# Read SNP data from a CSV file
print(f"Reading SNP data from {input_file}")
snp_data = read_snp_data(input_file)
print(f"Found {len(snp_data)} SNPs.")

count = 0
for snp in snp_data:
  chromosome = snp["chromosome"]
  position = snp["position"]
  count += 1
  print(f"Processing SNP {count}/{len(snp_data)}: {chromosome}:{position}...")
  # Check if the SNP is a known SNP
  print("Checking if the SNP is a known SNP...")
  known_snp = fetch_known_snps(chromosome, position)
  if known_snp:
    print("The SNP is a known SNP.")
    snp["known_snp"] = 1
  else:
    print("The SNP is not a known SNP.")
    snp["known_snp"] = 0

  # Fetch gene annotations
  print("Fetching gene annotations...")
  gene_info = fetch_gene_annotations(chromosome, position)
  if gene_info is not None:
    print(f"Gene ID: {gene_info}")
    snp["gene_id"] = gene_info
  else:
    print("No gene annotations found.")
    snp["gene_id"] = None

# Post-process the data
print("Post-processing the data...")
snp_data = pd.DataFrame(snp_data)
# Combine the SNP chromosome and position into a single column
snp_data["SNP"] = snp_data["chromosome"] + ":" + snp_data["position"].astype(str)

# Save the results to a CSV file
print(f"Saving the results to {output_file}")
snp_data.to_csv(output_file, index=False)
print("Done.")
