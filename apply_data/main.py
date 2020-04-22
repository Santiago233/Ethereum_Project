# encoding='utf8'
import py2neo
from py2neo import Graph, Node, Relationship, PropertyDict
from basic import basic_api
from higher import higher_api

#print(py2neo.__version__)
#graph = Graph("http://127.0.0.1:7474", username="neo4j", password=",5d0_74f")
#graph = Graph("http://neo4j:,5d0_74f@localhost:7474/db/data")
graph = Graph("http:127.0.0.1:7474")
#graph.data的获取格式是list

if __name__ == '__main__':
	while 1:
		print("请选择查询方式(输入数字)：")
		print("1.basic\n2.higher\n3.exit")
		select_one = input()
		print("请选择具体查询方式(输入数字)：")
		if(select_one == 1):
			basic_api()
		else if(select_one == 2):
			higher_api()
		else if(select_one == 3):
			print("Thank you! Bye!")
			break;
		else:
			print("Wrong!")