#include<vector>
#include<string>
#include<io.h>
#include<iostream>
#include <fstream>
#include<string>
#include <ctime>
#include "json.hpp"

using namespace std;
using namespace nlohmann;

int diyicengLength = 1000;
int diercengLength = 1000;
string shuchu = "Block_queMinnerReward_cpp.csv";
string shuchu2 = "NormalTransaction_cpp.csv";


FILE * fp1;
FILE * fp2;


void dayin(string wenzi) {
	time_t now = time(0);
	char* dt = ctime(&now);
	cout << dt << " " << wenzi << endl;
}

bool isAxiaoyuB(string & a, string & b) {
	int asize = a.size();
	int bsize = b.size();
	
	if(asize < bsize)
		return true;
	else if(asize > bsize)
		return false;
	else{
		for(int i=0;i<asize;++i)
			if((int)a.at(i) < (int)b.at(i) )
				return true;
		return false;
	}
}


void duqufenxi(int diyiceng, int blockNumber) {
	
	string dir = "block/"+to_string(diyiceng*1000)+"/"+to_string(blockNumber)+".txt";
	
	json data;
	ifstream fin(dir.data());
	fin >> data;
	json & miaomi = data["result"];

	string timestamp_str = miaomi["timestamp"].get<string>();

	int timestamp = 0;     
	sscanf(timestamp_str.data(), "%x", &timestamp);   

	int minGasPrice = -1;
	int maxGasPrice = -1;
	int sumGasPrice = -1;
	int avgGasPrice = -1;

	int changdu =  miaomi["transactions"].size() ;
	
	for(int i=0; i<changdu; ++i ) {
		int thisGasPrice;
		json & zhegetx = miaomi["transactions"][i];
		sscanf(zhegetx["gasPrice"].get<string>().data(), "%x", &thisGasPrice); 
		/*
		cout << thisGasPrice << endl;
		cin >> thisGasPrice;*/

		if(i==0) {
			minGasPrice = thisGasPrice;
			maxGasPrice = thisGasPrice;
			sumGasPrice = thisGasPrice;
			continue;
		}
		
		if(thisGasPrice < minGasPrice)
			minGasPrice = thisGasPrice;
		if(thisGasPrice > maxGasPrice)
			maxGasPrice = thisGasPrice;
		sumGasPrice += thisGasPrice;
	
		string hash = zhegetx["hash"].get<string>();
		string from = zhegetx["from"].get<string>();
		string to = "";
		string creates = "";
		string value = "";
		
		if(!zhegetx["to"].is_null())
			to = zhegetx["to"].get<string>();
		if(!zhegetx["creates"].is_null())
			creates = zhegetx["creates"].get<string>();
		if(!zhegetx["value"].is_null())
			value = zhegetx["value"].get<string>();
		
		fprintf(fp2, "%d,%d,%s,%s,%s,%s,%s\n", blockNumber, timestamp, hash.data(), from.data(), to.data(), creates.data(), value.data());
	}

	if(sumGasPrice!=-1)
		avgGasPrice = sumGasPrice/changdu;

	int size;
		sscanf(miaomi["size"].get<string>().data(), "%x", &size);   
	int difficulty;
		sscanf(miaomi["totalDifficulty"].get<string>().data(), "%x", &difficulty);   

	int transactionCount = changdu;
		
	string minerAddress = miaomi["miner"].get<string>();
		
	int gasLimit;
		sscanf(miaomi["gasLimit"].get<string>().data(), "%x", &gasLimit);   
		
	int gasUsed;
		sscanf(miaomi["gasUsed"].get<string>().data(), "%x", &gasUsed);   

	fprintf(fp1, "%d,%d,%d,%d,%d,%s,%d,%d,%d,%d,%d\n", blockNumber, timestamp, size, difficulty, transactionCount, minerAddress.data(), gasLimit, gasUsed, minGasPrice, maxGasPrice, avgGasPrice);
}


int main()
{
	fp1 = fopen(shuchu.data(), "w+");
	fp2 = fopen(shuchu2.data(), "w+");
	
	fprintf(fp1, "%s",  "blockNumber, timestamp, size, difficulty, transactionCount, minerAddress, gasLimit, gasUsed, minGasPrice, maxGasPrice, avgGasPrice\n" );
	fprintf(fp2, "%s",  "blockNumber, timestamp, transactionHash, from, to, creates, value\n");

    string path = "D:\\washParity\\block";
    

    for(int diyiceng=0; diyiceng<1000; ++ diyiceng) {
    	for(int dierceng=0; dierceng<1000; ++dierceng) {
			int blockNumber = diyiceng*1000+dierceng;
			duqufenxi(diyiceng, blockNumber);
		}
		dayin(to_string(diyiceng));
    }
	return 0;
}
