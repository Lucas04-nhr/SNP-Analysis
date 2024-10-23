#! /bin/bash
#SBATCH --job-name=plink_test
#SBATCH --output=./test_log.%j.out
#SBATCH --error=./test_log.%j.err
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G

# Initialize the environment
echo "THIS IS A TEST SCRIPT FOR PLINK CONVERTING."
echo "IF YOU RUN THIS SCRIPT BY MISSTAKE, PLEASE PRESS CTRL+C TO TERMINATE THE JOB."
sleep 5
echo "=============================="
echo "Initializing the environment..."

# Load conda
source /home/bacphagenetwork/.bashrc
conda activate snp_analysis

# Set the paths of the output files
export JAVA_HOME='/mnt/raid6/bacphagenetwork/tools/jdk-22.0.1'
export JAVA_BIN='/mnt/raid6/bacphagenetwork/tools/jdk-22.0.1/bin/java'
export LDFLAGS='-L/mnt/raid6/bacphagenetwork/tools/jdk-22.0.1/lib/server'
export CPPFLAGS='-I/mnt/raid6/bacphagenetwork/tools/jdk-22.0.1/include'
export BASE_PATH="/mnt/raid6/bacphagenetwork/data/test"

export GATK_OLD_BIN="/mnt/raid6/bacphagenetwork/tools/gatk-4.3.0.0/gatk"
export GATK_NEW_BIN="/mnt/raid6/bacphagenetwork/tools/gatk-4.5.0.0/gatk"
export PLINK_BIN="/mnt/raid6/bacphagenetwork/tools/plink-1.07-x86_64/plink"

export INDEXING_PATH="$BASE_PATH/../00_bwa_index/GRCh38"
export INDEXING_FILE="$INDEXING_PATH/Homo_sapiens.GRCh38.dna.toplevel.fa"

export KNOWN_SITES_BASE_PATH="$BASE_PATH/../00_bwa_index/GRCh38/known-sites"
export KNOWN_SITES_1000G="$KNOWN_SITES_BASE_PATH/1000g/hg38_v0_1000G_phase1.snps.high_confidence.hg38.modified.vcf"
export KNOWN_SITES_DBSNP="$KNOWN_SITES_BASE_PATH/dbsnp138/hg38_v0_Homo_sapiens_assembly38.dbsnp138.modified.vcf"
export KNOWN_SITES_HAPMAP="$KNOWN_SITES_BASE_PATH/hapmap/hg38_v0_hapmap_3.3.hg38.modified.vcf"
export KNOWN_SITES_OMNI="$KNOWN_SITES_BASE_PATH/omni/hg38_v0_1000G_omni2.5.hg38.modified.vcf"

export SORTED_DATA_PATH="$BASE_PATH"
export RECALIBRATED_DATA_PATH="$BASE_PATH"
export APPLYBQSR_DATA_PATH="$BASE_PATH"
export HAPLOTYPECALLER_DATA_PATH="$BASE_PATH/07_HaplotypeCaller"
export GENOTYPE_GVCF_PATH="$BASE_PATH/08_GenotypeGVCF"
export VARIANTRECALIBRATOR_DATA_PATH="$BASE_PATH/09_VariantRecalibrator"
export APPLYVQSR_DATA_PATH="$BASE_PATH/10_ApplyVQSR"
export TEST_VCF_PATH="$BASE_PATH/11_ConvertedVCF"
export PLINK_BASE_PATH="$BASE_PATH/12_plink"

echo "The sorted *.bam files are located in $SORTED_DATA_PATH."
echo "The indexing data is located in $INDEXING_PATH."
echo "The indexing genome data is $INDEXING_FILE."
echo "The recalibrated *.bam files are located in $RECALIBRATED_DATA_PATH."
echo "The ApplyBQSR results are located in $APPLYBQSR_DATA_PATH."
echo "The HaplotypeCaller results are located in $HAPLOTYPECALLER_DATA_PATH."
echo "The GenotypeGVCF results are located in $GENOTYPE_GVCF_PATH."
echo "The VariantRecalibrator results are located in $VARIANTRECALIBRATOR_DATA_PATH."
echo "The ApplyVQSR results are located in $APPLYVQSR_DATA_PATH."
echo "The converted VCF files are located in $TEST_VCF_PATH."
echo "The plink files will be located in $PLINK_BASE_PATH."

echo "Initializing completed."
echo "=============================="



