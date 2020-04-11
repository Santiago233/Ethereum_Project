#include <vector>
#include <string>
#include <io.h>
#include <iostream>
#include <fstream>
#include <ctime>
#include "json.hpp"	//德国大牛的hpp，提供json类型

using namespace std;
using namespace nlohmann;

string Block = "Blcok.csv";
string Transaction = "Transaction.csv"

int first_num = 7000;
int second_num = 1000;

void import(int, int);

int main(){
	f1 = fopen(Block.data(), "w+");
	f2 = fopen(Transaction.data(), "w+");

	fprintf(f1, "%s", "blockNumber, timestamp, size, difficulty, transactionCount, minerAddress, minerExtra, gasLimit, gasUsed, minGasPrice, maxGasPrice, avgGasPrice\n");	//minerExtra不一定需要
	fprintf(f2, "%s", "blockNumber, timestamp, transactionHash, from, to, creates, value, gasLimit, gasPrice\n");

	for(int first = 0; first < first_num; first++)
		for(int second = 0; second < second_num; second++)
			import(first, second);
	return 0;
}

void import(int first, int second){
	int blockNumber = first * second_num + second;
	string block = "block/" + to_string(first) + "/" + to_string(blockNumber);
	string receipt = "receipt/" + to_string(first) + "/" + to_string(blockNumber);

	json blockdata, receiptdata;
	ifstream fin(block.data())
	fin >> blockdata;
	ifstream fin(receipt.data())
	fin >> receiptdata;
	json & blockresult = blockdata["result"];
	json & receiptresult = receiptdata["result"];

	string timestamp = blockdata["timestamp"].get<string>();
	string size = blockdata["size"].get<sting>();
	string difficulty = blockdata["difficulty"].get<string>();
	int transactionCount = blockdata["Transactions"].size();
	string minerAddress = blockdata["miner"].get<string>();
}