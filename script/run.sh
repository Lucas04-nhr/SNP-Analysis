../../bin/plink/plink --bfile converted_genotyped --linear --pheno phenotype.tsv --all-pheno --covar covariat
e.tsv --covar-number 5 --out result --noweb --allow-extra-chr --allow-no-sex