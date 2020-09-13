from basic import basic_api
from higher import higher_api

if __name__ == '__main__':
	while 1:
		print("请选择查询方式(输入数字)：")
		print("1.basic\n2.higher\n3.exit")
		select_one = int(input())
		if(select_one == 1):
			basic_api()
		elif(select_one == 2):
			higher_api()
		elif(select_one == 3):
			print("Thank you! Bye!")
			break;
		else:
			print("Wrong!")