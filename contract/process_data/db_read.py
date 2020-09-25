#!/usr/bin/python
# -*- coding:UTF-8 -*-

import MySQLdb

def find():
	db = MySQLdb.connect("210.28.134.72", "root", "12345678", "ethereum", charset = 'utf8')

	cursor = db.cursor()
	sql = input("请输入查询语句:")

	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		return results
	except:
		print("Error:unable to fetch data")
	finally:
		db.close()

if __name__ == "__main__":
	results = find()

	'''
	for row in results:
		print(row)
	'''