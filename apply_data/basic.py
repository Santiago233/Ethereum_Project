from graph import graph

def Client_find_degree():
	#label = "client"
	#print("请输入节点的id")
	#id = input()
	#print("请输入节点的address")
	#address = input()
	#client = graph.nodes.match('client', id = id, address = address, label = label).first()
	client = graph.nodes.match('client', address = "0x5a8faf30a107f916c9adddfa0d285083355c9c92").first()
	in_count = out_count = 0
	for rel in graph.match((client, ), r_type = "in"):
		in_count += 1
	for rel in graph.match((client, ), r_type = "out"):
		out_count += 1
	print(in_count, out_count)

def basic_api():
    print("请选择具体查询方式(输入数字)：")
    print("1.查询图中存在的环")
    print("2.查询图中某个节点的出入度")
    print("3.查询图中交易量较大的点")
    print("4.查询图中某个节点在某个时间段的交易频率")
    print("5.查询图中某个节点发起交易的时间")
    print("6.查询图中某个节点的交易对象")
    print("7.查询图中某个节点是否为新注册的节点")
    print("8.返回上一级")
	select_two = int(input())
	if(select_two == 1):
                print("TODO1")
	elif(select_two == 2):
		Client_find_degree()
	elif(select_two == 3):
                print("TODO3")
	elif(select_two == 4):
                print("TODO4")
	elif(select_two == 5):
                print("TODO5")
	elif(select_two == 6):
                print("TODO6")
	elif(select_two == 7):
                print("TODO7")
	elif(select_two == 8):
                print("exit")
		#nothing to do
	else:
		print("Wrong!请重新选择具体查询方式(输入数字)")
		basic_api()
