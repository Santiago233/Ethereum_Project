#修改Transaction.csv，增加label:transaction一列
import pandas as pd
import os
import sys

source_filename = "J:\\Transaction_tmp.csv"
dest_filename = "J:\\Transaction_new.csv"

source = pd.read_csv(source_filename, low_memory=False)
source['label'] = 'transaction'

source.to_csv(dest_filename, index = 0, header = 1)

readFile = open(dest_filename, "rb")
Filedata = readFile.read()
readFile.close()
writeFile = open(dest_filename, "wb")
writeFile.write(Filedata.rstrip())
writeFile.close()

print("Success Edition!")

#代码得到的Transaction_new.csv的表头最后一列少一个空格，此处之后注意