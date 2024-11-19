library(data.table)

res = fread("data/plink/result.P5.assoc.linear", header = T)

colnames(res)
print(head(res))
