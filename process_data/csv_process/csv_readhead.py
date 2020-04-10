#查看Block.csv和Transaction.csv的表头信息
import csv
import sys

filename = "J:\\Transaction.csv"

with open(filename,'rb') as csvfile:
	header = next(csvfile)
	header = header.strip()
	#header_list = header.split(",")
	#print(header_list)
	print(header)

'''
Header:
Block.csv:
blockNumber, timestamp, size, difficulty, transactionCount, minerAddress, minerExtra, gasLimit, gasUsed, minGasPrice, maxGasPrice, avgGasPrice
Transaction.csv:
blockNumber, timestamp, transactionHash, from, to, creates, value, gasLimit, gasPrice
'''