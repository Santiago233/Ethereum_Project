#include <vector>
#include <string>
#include <io.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include "json.hpp"	//德国大牛的hpp，提供json类型

using namespace std;
using json = nlohmann::json;

int first_num = 7000;
int second_num = 1000;

string contract = "Contract.csv";
FILE * f;

void get(int, int);

int main(){
	f = fopen(contract.data(), "w+");
	fprintf(f, "%s\n", "Contract,blockNumber,Timestamp,transactionHash,from,to,input,value");

	for(int i = 0; i < first_num; i++){
		for(int j = 0; j < second_num; j++){
			get(i, j);
		}
	}

	fclose(f);
	return 0;
}

void get(int first, int second){
	int blockNumber = first * second_num + second;
	string block = "block/" + to_string(first * second_num) + "/" + to_string(blockNumber) + ".txt";
	string receipt = "receipt/" + to_string(first * second_num) + "/" + to_string(blockNumber) + ".txt";

	json blockdata;
	ifstream finblock(block.data());
	finblock>>blockdata;
	json & blockresult = blockdata["result"];

	json receiptdata;
	ifstream finreceipt(receipt.data());
	finreceipt>>receiptdata;
	json & receiptresult = receiptdata["result"];
	//cout << receiptresult[0] << endl;

	string timestamp = blockresult["timestamp"].get<string>();
	string number = blockresult["number"].get<string>();
	//cout << timestamp << " " << number << endl;

	int transactionCount = blockresult["transactions"].size();
	for(int i = 0 ; i < transactionCount; i++){
		string status = receiptresult[i]["status"];
		//cout << status << endl;
		if(status == "0x1"){
			string hash = blockresult["transactions"][i]["hash"].get<string>();
			string from = blockresult["transactions"][i]["from"].get<string>();
			string input = blockresult["transactions"][i]["input"].get<string>();
			string to = "";	//可能to数据是null
			if(!blockresult["transactions"][i]["to"].is_null())
				to = blockresult["transactions"][i]["to"].get<string>();
			string value = blockresult["transactions"][i]["value"].get<string>();
			fprintf(f, "%s,%s,%s,%s,%s,%s,%s,%s\n", to.data(), number.data(), timestamp.data(), hash.data(), from.data(), to.data(), input.data(), value.data());
		}
	}
	cout << "Block" << blockNumber << " finished" << endl;
}