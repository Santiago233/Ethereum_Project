#修改Block.csv，增加label:block一列
import pandas as pd
import os
import sys
import csv

source_filename = "J:\\Block.csv"
dest_filename = "J:\\Block_new.csv"

#添加id的索引，方便后面生成关系的csv文件
with open(source_filename, 'r', encoding='UTF-8') as csvfile:
	reader = csv.DictReader(csvfile)
	Numbers = [row['blockNumber'] for row in reader]
	for index in range(len(Numbers)):
		Numbers[index] = "block" + Numbers[index]

source = pd.read_csv(source_filename, low_memory=False)
source['label'] = 'block'
source.insert(0, 'id', Numbers)

#去除列名自带的空格
tmpcolumns = source.columns
newcolumns = []
for column in tmpcolumns:
	newcolumns.append(column.replace(' ', ''))

source.to_csv(dest_filename, index = False, header = newcolumns)

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