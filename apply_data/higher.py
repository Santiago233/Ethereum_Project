from graph import graph
import basic
import pandas as pd
import math

def Client_whether_launder_many_transaction():
	#first_case:短时间大量交易，其中短时间定义为1天指标&邻近2天指标
	transaction_in, transaction_out = basic.Client_get_transaction()
	counts = len(transaction_out)
	print("请输入检查的比例")
	percent = float(input())
	if(counts >= 100):
		transactions = []
		for transaction in transaction_out:
			transactions.append(eval(transaction["transaction"]["timestamp"]))
		new_transactions = sorted(transactions)
		min = new_transactions[0]
		max = new_transactions[counts - 1]
		day_len = 60 * 60 * 24
		days = math.ceil((max - min) / day_len)
		print(days)
		days_counts = [0] * days
		print(days_counts)
		for transaction in new_transactions:
			day_number = math.floor((transaction - min) / day_len)
			days_counts[day_number] += 1
		for day_number in range(days):
			if(days_counts[day_number] >= counts * percent):
				print("该节点可能发生了洗钱交易")
				return True
			else:
				if(day_number >= 1 and days_counts[day_number - 1] + days_counts[day_number] >= counts * percent * 2):
					print("该节点可能发生了洗钱交易")
					return True
				if(day_number <= days - 2 and days_counts[day_number] + days_counts[day_number + 1] >= counts * percent * 2):
					print("该节点可能发生了洗钱交易")
					return True
	return False

def Client_whether_launder_with_block():
	#second_case:查找因洗钱存在的环，其中环的最大长度定义为n
	print("TODO")

def Client_whether_launder():
	first_case = Client_whether_launder_many_transaction()
	if(first_case == False):
		print("first_case不满足")
		Client_whether_launder_with_block()

def Client_whether_theft():
	transaction_in, transaction_out = basic.Client_get_transaction()
	transactions = []
	for transaction in transaction_in:
		concrete_transaction = {}
		concrete_transaction["time"] = transaction["transaction"]["timestamp"]
		concrete_transaction["value"] = len(transaction["transaction"]["value"])
		concrete_transaction["way"] = "from"
		transactions.append(concrete_transaction)
	for transaction in transaction_out:
		concrete_transaction = {}
		concrete_transaction["time"] = transaction["transaction"]["timestamp"]
		concrete_transaction["value"] = len(transaction["transaction"]["value"])
		concrete_transaction["way"] = "to"
		transactions.append(concrete_transaction)
	new_transactions = sorted(transactions, key = lambda e:e["time"])
	#判断数值中的异常

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