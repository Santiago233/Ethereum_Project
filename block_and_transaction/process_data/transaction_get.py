#从Transaction.csv中获取交易双方节点并且去重处理
import csv
import pandas as pd
import os

filename = "Transaction.csv"
tmpfilename = "Transaction_tmp.csv"
destfilename = "Clients_new.csv"

#csv文件太大，影响读取速度，选择csv文件部分读取

tmpdata = pd.read_csv(filename, low_memory=False,nrows=5000000)
#去除列名自带的空格
tmpcolumns = tmpdata.columns
newcolumns = []
for column in tmpcolumns:
	newcolumns.append(column.replace(' ', ''))
tmpdata.to_csv(tmpfilename, index = 0, header = newcolumns)
print("Step 0!")

with open(tmpfilename, 'r') as csvfile_from:
	reader_from = csv.DictReader(csvfile_from)
	column_from = [row['from'] for row in reader_from]
with open(tmpfilename, 'r') as csvfile_to:
	reader_to = csv.DictReader(csvfile_to)
	column_to = [row['to'] for row in reader_to]
	#assert(0)
	print("Step 1!")
	#column_clients = list(set(column_from + column_to)) #remove duplicates
	column_to.extend(column_from)
	column_clients = list(set(column_to))
	#column_clients = {}.fromkeys(column_from).keys()
	print("Step 2!")
	#print(column_clients)

	last_clients = []
	number = 0
	for every_client in column_clients:
		every_client_list = []
		every_client_list.append(every_client)
		#print(every_client_list)
		every_client_list.insert(0,"client" + every_client)
		#print(every_client_list)
		every_client_list.append("client")
		last_clients.append(every_client_list)
	#print(last_clients)

	name = ['id', 'address', 'label']
	dest = pd.DataFrame(columns = name, data = last_clients)
	dest.to_csv(destfilename, index = False)
	print("Step 3!")

	#去除最后一行空行
	readFile = open(destfilename, "rb")
	Filedata = readFile.read()
	readFile.close()
	writeFile = open(destfilename, "wb")
	writeFile.write(Filedata.rstrip())
	writeFile.close()
	print("Step 4!")

#代码得到的Transaction_tmp.csv和Client_new.csv的最后一行是空行，此处之后注意