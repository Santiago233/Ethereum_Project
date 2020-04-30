from graph import graph
import basic
import pandas as pd
import math

def Client_whether_launder_many_transaction(address):
	#first_case:短时间大量交易，其中短时间定义为1天指标&邻近2天指标
	transaction_in, transaction_out = basic.Client_get_transaction_by_property(address)
	counts = len(transaction_out)
	#print(counts)
	if(counts >= 100):
		transactions = []
		for transaction in transaction_out:
			transactions.append(eval(transaction["transaction"]["timestamp"]))
		new_transactions = sorted(transactions)
		time_min = new_transactions[0]
		time_max = new_transactions[counts - 1]
		day_len = 60 * 60 * 24
		days = math.ceil((time_max - time_min) / day_len)
		#print(days)
		days_counts = [0] * days
		for transaction in new_transactions:
			day_number = math.floor((transaction - time_min) / day_len)
			days_counts[day_number] += 1
		#print(days_counts)
		#print("请输入检查的比例")
		#percent = float(input())
		for day_number in range(days):
			if(days_counts[day_number] >= counts * 0.3):
				print("该节点可能发生了洗钱交易")
				return True
			else:
				if(day_number >= 1 and days_counts[day_number - 1] + days_counts[day_number] >= counts * 0.5):
					print("该节点可能发生了洗钱交易")
					return True
				if(day_number <= days - 2 and days_counts[day_number] + days_counts[day_number + 1] >= counts * 0.5):
					print("该节点可能发生了洗钱交易")
					return True
	return False

def Client_whether_launder_with_block(address):
	#second_case:查找因洗钱存在的环，其中环的最大长度定义为step
	step = 20
	address = address
	data = graph.data('match path = (client1 {label:"client", address:"'+ address +'"})-[:in|:out*..'+ step +']->(client2 {label:"client", address:"'+ address +'"}) unwind nodes(path) as n with path, size(collect(distinct n)) as number where number = length(path) return nodes(path) as path_list')
	if(len(data) != 0):
		give = 0
		gas = 0
		get = 0
		for data_ in data:
			concrete_path = data_["path_list"]
			give += eval(concrete_path[1]["value"])
			get += eval(concrete_path[len(concrete_path) - 2]["value"])
			for node in concrete_path:
				if(node["label"] == "transaction"):
					gas += eval(node["gasPrice"])
		if(get == give + gas):
			print("该节点可能发生了洗钱交易")
			return
	print("该节点应该未进行洗钱交易")

def Client_whether_launder():
	print("请输入节点的address")
	address = input()
	first_case = Client_whether_launder_many_transaction(address)
	if(first_case == False):
		Client_whether_launder_with_block(address)

def Client_whether_theft():
	transaction_in, transaction_out = basic.Client_get_transaction()
	transactions = []
	for transaction in transaction_in:
		concrete_transaction = {}
		concrete_transaction["time"] = eval(transaction["transaction"]["timestamp"])
		concrete_transaction["value"] = len(transaction["transaction"]["value"])
		concrete_transaction["way"] = "from"
		transactions.append(concrete_transaction)
	for transaction in transaction_out:
		concrete_transaction = {}
		concrete_transaction["time"] = eval(transaction["transaction"]["timestamp"])
		concrete_transaction["value"] = len(transaction["transaction"]["value"])
		concrete_transaction["way"] = "to"
		transactions.append(concrete_transaction)
	new_transactions = sorted(transactions, key = lambda e:e["time"])
	#判断数值中的异常——时间、频率、金额、对象——分组的per和avg进行比较
	time_min = new_transactions[0]["time"]
	time_max = new_transactions[len(new_transactions) - 1]["time"]
	value_avg = 0
	way_avg = 0
	if(len(transaction_out) != 0):
		way_avg = len(transaction_in) / len(transaction_out)
	for transaction in new_transactions:
		value_avg += transaction["value"]
	if(len(transaction_out) != 0):
		value_avg = value_avg / (len(new_transactions))
	day_len = 60 * 60 *24
	days_counts = math.ceil((time_max - time_min) / day_len)
	if(days_counts != 0):
		count_avg = len(new_transactions) / days_counts
	#print("以下为平均情况(数目、金额、交易对象)")
	#print(count_avg, value_avg, way_avg)

	for days in range(days_counts):
		value_per = 0
		count_per = 0
		way_per = 0
		way_from = 0
		way_to = 0
		for transaction in new_transactions:
			if(transaction["time"] >= time_min + days * day_len and transaction["time"] < time_min + (days + 1) * day_len):
				value_per += transaction["value"]
				count_per += 1
				if(transaction["way"] == "from"):
					way_from += 1
				else:
					way_to += 1
		if(count_per != 0):
			value_per = value_per / count_per
		if(way_to != 0):
			way_per = way_from / way_to
		#print("以下为单个情况(数目、金额、交易对象)")
		#print(count_per, value_per, way_per)
		if(count_per < count_avg * 0.85 or count_per > count_avg * 1.15):
			if(abs(count_per - count_avg) > 20):
				print("该节点交易时间&频率出现异常，可能发生了盗用")
				return
		if(value_per < value_avg * 0.85 or value_per > value_avg * 1.15):
			if(value_per != 0):
				print("该节点交易金额出现异常，可能发生了盗用")
				return
		if(way_per < way_avg * 0.85 or way_per > way_avg * 1.15):
			if(abs(count_per) > 30):
				print("该节点交易对象出现异常，可能发生了盗用")
				return
	print("该节点尚未发生盗用")

def Client_whether_tax_evasion():
	in_count, out_count = basic.Client_find_degree_by_transaction()	#出度是in_count，入度是out_count
	counts = in_count + out_count
	percent = out_count / counts
	#涉及偷税的节点至少有200笔交易并且入度占到90%以上
	if(counts >= 200 and percent >= 0.9):
		print("该节点可能作为避税港/资产转移地")
	else:
		print("该节点应该不是避税港/资产转移地")

def Client_whether_transfer_money():
	transaction_in, transaction_out = basic.Client_get_transaction()
	values = []
	for transaction in transaction_in:
		#value数据普遍位数较多，故使用长度作为判断
		value = len(transaction["transaction"]["value"])
		#print(value)
		values.append(value)
	values_p = pd.Series(values).describe()
	Q1 = values_p['25%']
	Q3 = values_p['75%']
	IQR = Q3 - Q1
	values_upper = Q3 + 1.5 * IQR
	#print(values_upper)
	for value in values:
		if(value - values_upper >= 1.5):
			print("该节点可能发生资产转移行为")
			return
	print("该节点应该尚未发生资产转移行为")

def Client_whether_illegal_transaction():
	transaction_in, transaction_out = basic.Client_get_transaction()
	in_count = out_count = 0
	for transaction in transaction_in:
		in_count += 1
	for transaction in transaction_out:
		out_count += 1
	counts = in_count + out_count
	percent = out_count / counts
	if(counts >= 200 and percent >= 0.9):
		object_counts = 0
		for transaction in transaction_out:
			address = transaction["transaction"]["from"]
			object_in, object_out = basic.Client_get_transaction_by_property(address)
			number = len(object_in) + len(object_out)
			#print("number:", number)
			if(number <= 5):
				object_counts += 1
		#print(object_counts)
		new_percent = object_counts / out_count
		if(new_percent >= 0.9):
			print("该节点可能作为非法交易组织者")
			return
	print("该节点应该未作为非法交易组织者")

def higher_api():
	print("请选择具体查询方式(输入数字)：")
	print("1.查询图中某个节点是否可能发生洗钱交易")
	print("2.查询图中某个节点是否可能被盗用账号")
	print("3.查询图中某个节点是否可能作为避税港/资产转移地")
	print("4.查询图中某个节点是否可能发生资产转移行为")
	print("5.查询图中某个节点是否可能作为非法交易组织者")
	print("6.返回上一级")
	select_two = int(input())
	if(select_two == 1):
		#print("TODO1")
		Client_whether_launder()
	elif(select_two == 2):
		#print("TODO2")
		Client_whether_theft()
	elif(select_two == 3):
		#print("TODO3")
		Client_whether_tax_evasion()
	elif(select_two == 4):
		#print("TODO4")
		Client_whether_transfer_money()
	elif(select_two == 5):
		#print("TODO4")
		Client_whether_illegal_transaction()
	elif(select_two == 6):
		print("exit")
	else:
		print("Wrong!请重新选择具体查询方式(输入数字)")
		higher_api()

#存在情况：考虑节点A专门向节点B交易的情况