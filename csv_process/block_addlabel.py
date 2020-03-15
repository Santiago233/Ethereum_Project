#修改Block.csv，增加label:block一列
import pandas as pd
import os
import sys

source_filename = "J:\\Block.csv"
dest_filename = "J:\\Block_new.csv"

source = pd.read_csv(source_filename, low_memory=False)
source['label'] = 'block'

source.to_csv(dest_filename, index = 0, header = 1)
	#columns = ['blockNumber', 'timestamp', 'size', 'difficulty', 'transactionCount', 'minerAddress', 'minerExtra', 'gasLimit', 'gasUsed', 'minGasPrice', 'maxGasPrice', 'avgGasPrice', 'label']

#去除最后一行空行
'''
data = open(dest_filename, "rb+")
data.seek(-1, os.SEEK_END)
if data.__next__() == "\n":
	data.seek(-1, os.SEEK_END)
	data.truncate()
data.close()
'''
readFile = open(dest_filename, "rb")
Filedata = readFile.read()
readFile.close()
writeFile = open(dest_filename, "wb")
writeFile.write(Filedata.rstrip())
writeFile.close()

print("Success Edition!")

#代码得到的Block_new.csv的表头最后一列少一个空格，此处之后注意