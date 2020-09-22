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

string Block = "Block.csv";
string Transaction = "Transaction.csv";

int first_num = 9000;
int second_num = 1000;

FILE * f1;
FILE * f2;

void import(int, int);
string long2hex(long);

int main(){
	f1 = fopen(Block.data(), "w+");
	f2 = fopen(Transaction.data(), "w+");

	fprintf(f1, "%s\n", "blockNumber, timestamp, size, difficulty, transactionCount, minerAddress, gasLimit, gasUsed, minGasPrice, maxGasPrice, avgGasPrice");	//少一个minerExtra
	fprintf(f2, "%s\n", "blockNumber, timestamp, transactionHash, from, to, creates, value, gasLimit, gasPrice");

	for(int first = 0; first < first_num; first++){
		for(int second = 0; second < second_num; second++){
			import(first, second);
		}
		cout<<"finish"<<" "<<first<<"line"<<endl;
	}
	fclose(f1);
	fclose(f2);
	//import(0, 0);
	return 0;
}

void import(int first, int second){
	int blockNumber = first * second_num + second;
	string block = "block/" + to_string(first * second_num) + "/" + to_string(blockNumber) + ".txt";
	//cout<<block.data()<<endl;
	//string receipt = "./receipt/" + to_string(first) + "/" + to_string(blockNumber) + ".txt";

	json blockdata;
	ifstream finblock(block.data());
	finblock>>blockdata;
	//cout<<blockdata<<endl;
	json & blockresult = blockdata["result"];

	/*json receiptdata;
	ifstream finreceipt(receipt.data());
	finreceipt >> receiptdata;
	json & receiptresult = receiptdata["result"];
	*/
	string timestamp = blockresult["timestamp"].get<string>();
	string size = blockresult["size"].get<string>();
	string difficulty = blockresult["difficulty"].get<string>();
	int transactionCount = blockresult["transactions"].size();
	string minerAddress = blockresult["miner"].get<string>();
	string gasLimit = blockresult["gasLimit"].get<string>();
	string gasUsed = blockresult["gasUsed"].get<string>();
	//cout<<blockNumber<<" "<<timestamp<<" "<<size<<" "<<difficulty<<" "<<transactionCount<<" "<<minerAddress<<endl;
	string minGasPrice_string = "0x", maxGasPrice_string = "0x", avgGasPrice_string = "0x";
	if(transactionCount > 0){
		long minGasPrice = 0, maxGasPrice = 0, avgGasPrice = 0, sumGasPrice = 0;
		for(int i = 0; i < transactionCount; i++){
			string transactionHash = blockresult["transactions"][i]["hash"].get<string>();
			string from = blockresult["transactions"][i]["from"].get<string>();
			string to = "", creates = "", value = "";
			if(!blockresult["transactions"][i]["to"].is_null())
				to = blockresult["transactions"][i]["to"].get<string>();
			if(!blockresult["transactions"][i]["creates"].is_null())
				creates = blockresult["transactions"][i]["creates"].get<string>();
			if(!blockresult["transactions"][i]["value"].is_null())
				value = blockresult["transactions"][i]["value"].get<string>();
			string gasLimit = blockresult["transactions"][i]["gas"].get<string>();
			string gasPrice = blockresult["transactions"][i]["gasPrice"].get<string>();
			//cout<<blockNumber<<" "<<timestamp<<" "<<transactionHash<<" "<<from<<" "<<to<<" "<<creates<<" "<<value<<" "<<gasLimit<<" "<<gasPrice<<endl;
			fprintf(f2, "%d,%s,%s,%s,%s,%s,%s,%s,%s\n", blockNumber, timestamp.data(), transactionHash.data(), from.data(), to.data(), creates.data(), value.data(), gasLimit.data(), gasPrice.data());

			long gasPrice_long = strtol(gasPrice.data(), NULL, 16);
			if(i == 0){
				minGasPrice = gasPrice_long;
				maxGasPrice = gasPrice_long;
			}else{
				if(gasPrice_long < minGasPrice){
					minGasPrice = gasPrice_long;
				}
				if(gasPrice_long > maxGasPrice){
					maxGasPrice = gasPrice_long;
				}
			}
			sumGasPrice += gasPrice_long;
		}
		avgGasPrice = sumGasPrice / transactionCount;
		minGasPrice_string = minGasPrice_string.append(long2hex(minGasPrice));
		maxGasPrice_string = maxGasPrice_string.append(long2hex(maxGasPrice));
		avgGasPrice_string = avgGasPrice_string.append(long2hex(avgGasPrice));
	}else{
		minGasPrice_string = "0x0";
		maxGasPrice_string = "0x0";
		avgGasPrice_string = "0x0";
	}
	fprintf(f1, "%d,%s,%s,%s,%d,%s,%s,%s,%s,%s,%s\n", blockNumber, timestamp.data(), size.data(), difficulty.data(), transactionCount, minerAddress.data(), gasLimit.data(), gasUsed.data(), minGasPrice_string.data(), maxGasPrice_string.data(), avgGasPrice_string.data());
}

string long2hex(long number){
	stringstream input;
	string number_string;
	input<<resetiosflags(ios::uppercase)<<hex<<number;
	input>>number_string;
	return number_string;
}