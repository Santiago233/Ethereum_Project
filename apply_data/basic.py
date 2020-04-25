from graph import graph
import time

def Client_get_transaction_by_property(address):
	transaction_in = graph.data('match(client {label:"client", address:"'+ address +'"})-[in]->(transaction) return transaction')
	transaction_out = graph.data('match(transaction)-[out]->(client {label:"client", address:"'+ address +'"}) return transaction')
	return transaction_in, transaction_out

def Client_get_transaction():
	#用于测试节点address为0x5a8faf30a107f916c9adddfa0d285083355c9c92
	#用于测试节点一个to节点address为0x3cb9f9ee387168077aa3bcd9ea6e43cd7c79c540
	#用于测试节点一个from节点address为0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5
	print("请输入节点的address")
	address = input()
	transaction_in, transaction_out = Client_get_transaction_by_property(address)
	return transaction_in, transaction_out

def Client_find_degree_by_transaction():
	transaction_in, transaction_out = Client_get_transaction()
	in_count = out_count = 0
	for transaction in transaction_in:
		in_count += 1
	for transaction in transaction_out:
		out_count += 1
	return in_count, out_count

def Client_find_path_with_loop():
	print("请输入节点的address")
	address = input()
	print("请指定环的最大长度")
	max_number = input()
	paths = []
	data = graph.data('match path = (client1 {label:"client", address:"'+ address +'"})-[:in|:out*..'+ max_number +']->(client2 {label:"client", address:"'+ address +'"}) unwind nodes(path) as n with path, size(collect(distinct n)) as number where number = length(path) return nodes(path) as path_list')
	for data_ in data:
		concrete_path = data_["path_list"]
		abstract_path = []
		for node in concrete_path:
			abstract_path.append(node["id"])
		paths.append(abstract_path)
	if(len(paths) != 0):
		print("以下是该节点指定长度内存在的环")
		for path in paths:
			print(path)
	else:
		print("该节点不存在指定长度内的环")

def Client_find_degree():
	in_count, out_count = Client_find_degree_by_transaction()
	print("该节点的出度为：", in_count)
	print("该节点的入度为：", out_count)
	if(out_count != 0):
		print("该节点的出入度比值为：%.3f" % (in_count/out_count))

def Client_find_with_many_transactions():
	'''
	clients = graph.data('match(client {label:"client"}) return client')
	clients_dict = {}
	for client in clients:
		if(client["client"]["id"] == "client"):
			continue
		address = client["client"]["address"]
		transaction_in, transaction_out = Client_get_transaction_by_property(address)
		count = len(transaction_in) + len(transaction_out)
		clients_dict[address] = count
	'''
	client_in = graph.data('match(client {label:"client"})-[in]->(transaction {label:"transaction"}) return client')
	client_out = graph.data('match(transaction {label:"transaction"})-[out]->(client {label:"client"}) return client')
	clients = client_in + client_out
	clients_dict = {}
	for client in clients:
		if(client["client"]["id"] == "client"):
			continue
		address = client["client"]["address"]
		if address in clients_dict.keys():
			count = clients_dict[address]
			del clients_dict[address]
			clients_dict[address] = count + 1
		else:
			clients_dict[address] = 1

	new_clients_dict_max = sorted(clients_dict.items(), key = lambda x: x[1], reverse = True)
	new_clients_dict_min = sorted(clients_dict.items(), key = lambda x: x[1])
	#取前万分之一作为交易量大的节点，后万分之一作为交易量小的节点(虽然实际大部分都是1)
	number = len(new_clients_dict_max) // 10000
	#取前100作为交易量大的节点，取后100作为交易量小的节点
	#number = 100
	new_clients_dict_max = new_clients_dict_max[:number]
	print("以下是交易量较大的节点")
	for client in new_clients_dict_max:
		print("address:%s, 交易量为:%d" %(client[0], client[1]))
	new_clients_dict_min = new_clients_dict_min[:number]
	print("以下是交易量较小的节点")
	for client in new_clients_dict_min:
		print("address:%s, 交易量为:%d" %(client[0], client[1]))

def Client_caculate_frequence():
	print("请输入查询时间(timestamp)段的下限")
	timestamp_min = eval(input())
	print("请输入查询时间(timestamp)段的上限")
	timestamp_max = eval(input())
	transaction_in, transaction_out = Client_get_transaction()
	transactions = transaction_in + transaction_out
	#print(len(transaction_in), len(transaction_out), len(transactions))
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
	if(len(ObjectClient) != 0):
		print("该节点的交易对象有：")
		for client in ObjectClient:
			print("address:", client["address"])

def basic_api():
	print("请选择具体查询方式(输入数字)：")
	print("1.查询图中是否存在某个节点的环")
	print("2.查询图中某个节点的出入度")
	print("3.查询图中交易量较大和较小的节点")
	print("4.查询图中某个节点在某个时间段的交易频率")
	print("5.查询图中某个节点发起交易的时间")
	print("6.查询图中某个节点的交易对象")
	print("7.返回上一级")
	select_two = int(input())
	if(select_two == 1):
		#print("TODO1")
		Client_find_path_with_loop()
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
