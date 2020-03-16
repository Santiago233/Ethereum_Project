#修改Transaction.csv，增加label:transaction一列
import pandas as pd
import os
import sys
import csv

source_filename = "J:\\Transaction_tmp.csv"
dest_filename = "J:\\Transaction_new.csv"

#添加id的索引，方便后面生成关系的csv文件
with open(source_filename, 'r', encoding='UTF-8') as csvfile:
	reader = csv.DictReader(csvfile)
	Hashes = [row['transactionHash'] for row in reader]
	for index in range(len(Hashes)):
		Hashes[index] = "transaction" + Hashes[index]

source = pd.read_csv(source_filename, low_memory=False)
source['label'] = 'transaction'
source.insert(0, 'id', Hashes)

source.to_csv(dest_filename, index = 0, header = 1)

readFile = open(dest_filename, "rb")
Filedata = readFile.read()
readFile.close()
writeFile = open(dest_filename, "wb")
writeFile.write(Filedata.rstrip())
writeFile.close()

print("Success Edition!")