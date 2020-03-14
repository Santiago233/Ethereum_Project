#从Transaction.csv中获取交易双方节点并且去重处理
import csv
import pandas as pd

filename = "J:\\Transaction.csv"
tmpfilename = "J:\\Transaction_tmp.csv"
'''
tmpdata = pd.read_csv(filename, low_memory=False,nrows=5000000)
tmpdata.to_csv(tmpfilename, index = 0, header = 1)
print("Step 0!")
'''
with open(tmpfilename, 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	column_from = [row[' from'] for row in reader]
	column_to = [row[' to'] for row in reader]
	print("Step 1!")
	column_clients = list(set(column_from + column_to)) #remove duplicates
	print("Step 2!")
	#print(column_clients)

	last_clients = []
	number = 0
	for every_client in column_clients:
		every_client_list = []
		every_client_list.append(every_client)
		print(every_client_list)
		every_client_list.insert(0,"client" + str(number)).append("client")
		last_clients.append(every_client_list)
		number += 1
	print(last_clients)