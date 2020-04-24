from graph import graph

def higher_api():
	print("请选择具体查询方式(输入数字)：")
	print("1.查询图中可能发生洗钱交易的节点")
	print("2.查询图中可能被盗用账号的节点")
	print("3.查询图中可能作为避税港/资产转移地的节点")
	print("4.查询图中可能作为非法交易组织者的节点")
	print("5.查询图中可能作为犯罪分子销赃账号的节点")
	print("6.返回上一级")
	select_two = int(input())
	if(select_two == 1):
		print("TODO1")
	elif(select_two == 2):
		print("TODO2")
	elif(select_two == 3):
		print("TODO3")
	elif(select_two == 4):
		print("TODO4")
	elif(select_two == 5):
		print("TODO5")
	elif(select_two == 6):
		print("exit")
	else:
		print("Wrong!请重新选择具体查询方式(输入数字)")
		higher_api()
