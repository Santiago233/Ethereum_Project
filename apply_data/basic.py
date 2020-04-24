from graph import graph
import time

def Client_get_transaction_by_property(address):
	transaction_in = graph.data('match(client {label:"client", address:"'+ address +'"})-[in]->(transaction) return transaction')
	transaction_out = graph.data('match(transaction)-[out]->(client {label:"client", address:"'+ address +'"}) return transaction')
	return transaction_in, transaction_out

def Client_get_transaction():
	#用于测试节点的address为0x5a8faf30a107f916c9adddfa0d285083355c9c92
	print("请输入节点的address")
	address = input()
	transaction_in, transaction_out = Client_get_transaction_by_property(address)
	return transaction_in, transaction_out
	

def Client_find_degree():
	transaction_in, transaction_out = Client_get_transaction()
	in_count = out_count = 0
	for transaction in transaction_in:
		in_count += 1
	for transaction in transaction_out:
		out_count += 1
	print("该节点的出度为：", in_count)
	print("该节点的入度为：", out_count)
	print("该节点的出入度比值为：%.3f" % (in_count/out_count))

def Client_find_with_many_transactions():
	clients = graph.data('match(client {label:"client"}) return client')
	clients_dict = {}
	number = 0
	for client in clients:
		print(number)
		number += 1
		if(client["client"]["id"] == "client"):
			continue
		address = client["client"]["address"]
		transaction_in, transaction_out = Client_get_transaction_by_property(address)
		count = len(transaction_in) + len(transaction_out)
		clients_dict[address] = count
	print(clients_dict)
	new_clients_dict = sorted(clients_dict.items(), key = lambda x: x[1])
	#取前万分之一作为交易量大的节点
	max_number = len(new_clients_dict) / 10000
	print(max_number)
	new_clients_dict = new_clients_dict[:max_number]
	print(new_clients_dict)
	print("以下是交易量较大的节点")
	for client in new_clients_dict:
		print("address:%s, 交易量为:%d", client[0], client[1])

def Client_caculate_frequence():
	transaction_in, transaction_out = Client_get_transaction()
	transactions = transaction_in + transaction_out
	#print(len(transaction_in), len(transaction_out), len(transactions))
	print("请输入查询时间(timestamp)段的下限")
	timestamp_min = eval(input())
	print("请输入查询时间(timestamp)段的上限")
	timestamp_max = eval(input())
	count = 0
	for transaction in transactions:
		timestamp = eval(transaction["transaction"]["timestamp"])
		if(timestamp >= timestamp_min and timestamp <= timestamp_max):
			count += 1
	print("该节点在该时间段的交易数目为：", count)
	#TODO：判断交易频率是否高低

def Client_caculate_starttime():
	transaction_in, transaction_out = Client_get_transaction()
	transactions = transaction_in + transaction_out
	starttime = 0xffffffff
	for transaction in transactions:
		timestamp = eval(transaction["transaction"]["timestamp"])
		if(timestamp < starttime):
			starttime = timestamp
	time_local = time.localtime(starttime)
	date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
	print("该节点最早发起交易的时间为：", date)

def Client_find_ObjectClient():
	transaction_in, transaction_out = Client_get_transaction()
	Objectaddress = []
	for transaction in transaction_in:
		address = transaction["transaction"]["to"]
		Objectaddress.append(address)
	for transaction in transaction_out:
		address = transaction["transaction"]["from"]
		Objectaddress.append(address)
	Objectaddress = list(set(Objectaddress))
	ObjectClient = []
	for address in Objectaddress:
		client_data = graph.data('match(client {address:"'+ address +'"}) return client')
		#print(type(client_data[0]["client"]))
		ObjectClient.append(dict(client_data[0]["client"]))
	print("该节点的交易对象有：")
	for client in ObjectClient:
		print("address:", client["address"])

def basic_api():
	print("请选择具体查询方式(输入数字)：")
	print("1.查询图中存在的环")
	print("2.查询图中某个节点的出入度")
	print("3.查询图中交易量较大的点")
	print("4.查询图中某个节点在某个时间段的交易频率")
	print("5.查询图中某个节点发起交易的时间")
	print("6.查询图中某个节点的交易对象")
	print("7.返回上一级")
	select_two = int(input())
	if(select_two == 1):
		print("TODO1")
	elif(select_two == 2):
		#print("TODO2")
		Client_find_degree()
	elif(select_two == 3):
		#print("TODO3")
		Client_find_with_many_transactions()
	elif(select_two == 4):
		#print("TODO4")
		Client_caculate_frequence()
	elif(select_two == 5):
		#print("TODO5")
		Client_caculate_starttime()
	elif(select_two == 6):
		#print("TODO6")
		Client_find_ObjectClient()
	elif(select_two == 7):
		print("exit")
	else:
		print("Wrong!请重新选择具体查询方式(输入数字)")
		basic_api()
