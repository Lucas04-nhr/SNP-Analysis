load("data/FMGC.sp.Rdata")
load("data/FMGC.ge.Rdata")

data_bj_sp = BJ.sp
data_bj_ge = BJ.ge

write.csv(data_bj, "./data_export/FMGC.sp/Beijing.csv", row.names = FALSE)
write.csv(data_bj_ge, "./data_export/FMGC.ge/Beijing.csv", row.names = FALSE)

data_gz = GZ.sp
data_gz_ge = GZ.ge

write.csv(data_gz, "./data_export/FMGC.sp/Guangzhou.csv", row.names = FALSE)
write.csv(data_gz_ge, "./data_export/FMGC.ge/Guangzhou.csv", row.names = FALSE)
