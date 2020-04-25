from graph import graph
import basic

def Client_whether_theft():
	print("请输入节点的address")
	address = input()
	transaction_in, transaction_out = basic.Client_get_transaction_by_property(address)
	transactions = []
	for transaction in transaction_in:
		concrete_transaction = {}
		concrete_transaction["time"] = transaction["transaction"]["timestamp"]
		concrete_transaction["value"] = transaction["transaction"]["value"]
		concrete_transaction["way"] = "from"
		transactions.append(concrete_transaction)
	for transaction in transaction_out:
		concrete_transaction = {}
		concrete_transaction["time"] = transaction["transaction"]["timestamp"]
		concrete_transaction["value"] = transaction["transaction"]["value"]
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

def Client_whether_illegal_transaction():
	transaction_in, transaction_out = basic.Client_get_transaction()
	in_count = out_count = 0
	for transaction in transaction_in:
		in_count += 1
	for transaction in transaction_out:
		out_count += 1
	counts = in_count + out_count
	percent = out_count / counts
	if(counts >= 200 and percent >= 0.85):
		object_counts = 0
		for transaction in transaction_out:
			address = transaction["transaction"]["from"]
			object_in, object_out = basic.Client_get_transaction_by_property(address)
			if(len(object_in) + len(object_out) <= 5):
				object_counts += 1
		new_percent = object_counts / out_count
		if(new_percent >= 0.85):
			print("该节点可能作为非法交易组织者")
			return
	print("该节点应该未作为非法交易组织者")

def higher_api():
	print("请选择具体查询方式(输入数字)：")
	print("1.查询图中某个节点是否可能发生洗钱交易")
	print("2.查询图中某个节点是否可能被盗用账号")
	print("3.查询图中某个节点是否可能作为避税港/资产转移地")
	print("4.查询图中某个节点是否可能作为非法交易组织者")
	print("5.查询图中某个节点是否可能作为犯罪分子的销赃账号")
	print("6.返回上一级")
	select_two = int(input())
	if(select_two == 1):
		print("TODO1")
	elif(select_two == 2):
		#print("TODO2")
		Client_whether_theft()
	elif(select_two == 3):
		#print("TODO3")
		Client_whether_tax_evasion()
	elif(select_two == 4):
		#print("TODO4")
		Client_whether_illegal_transaction()
	elif(select_two == 5):
		print("TODO5")
	elif(select_two == 6):
		print("exit")
	else:
		print("Wrong!请重新选择具体查询方式(输入数字)")
		higher_api()
