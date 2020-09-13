import pandas as pd
import os
import sys
import csv

source_filename = "Contract.csv"

print("请输入contract address")
address = input("input:")
flag = 0

with open(source_filename, "r", encoding = "utf-8") as file:
	reader = csv.reader(file)
	characters = next(reader)
	#print(characters)
	csv_reader = csv.DictReader(file, fieldnames = characters)

	data = []
	for row in csv_reader:
		line = {}
		for k, v in row.items():
			line[k] = v
		#print(line)
		data.append(line)
	#print(data)

	for num in range(len(data)):
		if(data[num].get("Contract") == address):
			flag += 1
			blockNumber = data[num].get("blockNumber")
			Timestamp = data[num].get("Timestamp")
			transactionHash = data[num].get("transactionHash")
			tx_from = data[num].get("from")
			tx_to = data[num].get("to")
			tx_input = data[num].get("input")
			value = data[num].get("value")
			print("使用contract address的交易参数为:")
			print("blockNumber:" + blockNumber + ";")
			print("Timestamp:" + Timestamp + ";")
			print("transactionHash:" + transactionHash + ";")
			print("from:" + tx_from + ";")
			print("to:" + tx_to + ";")
			print("input:" + tx_input + ";")
			print("value:" + value + "\n")

if(flag == 0):
	print("未使用该contract address")