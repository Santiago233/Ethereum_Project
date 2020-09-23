#include <vector>
#include <string>
#include <io.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include "json.hpp"	//德国大牛的hpp，提供json类型
#include <mysql/mysql.h>

using namespace std;
using json = nlohmann::json;

int first_num = 1500;
int second_num = 1000;

void get(int, int, string, MYSQL);

int main(){
	const char user[] = "root";
	const char pswd[] = "root";
	const char host[] = "localhost";
	const char database[] = "ethereum";
	unsigned int port = 3306;

	MYSQL mysql;
	mysql_init(&mysql);

	MYSQL *ret1 = mysql_real_connect(&mysql, host, user, pswd, database, port, NULL, 0);
	if(!ret1){
		cout << "连接数据库失败！" << endl;
	}else{
		cout << "连接数据库成功！" << endl;
	}

	string table_name = "contract";

	string sql = "create table if not exists " + table_name + "(Contract varchar(1000), \
		blockNumber varchar(1000), \
		Timestamp varchar(1000), \
		transactionHash varchar(1000), \
		tx_from varchar(1000), \
		tx_to varchar(1000), \
		input varchar(1000), \
		value varchar(1000))";
	//cout << sql << endl;
	bool ret2 = mysql_query(&mysql, (char *)sql.data());
	if(ret2){
		cout << "创建数据表失败！" << endl;
	}else{
		cout << "创建数据表成功！" << endl;
	}

	for(int i = 0; i < first_num; i++){
		for(int j = 0; j < second_num; j++){
			get(i, j, table_name, mysql);
		}
		cout << i * second_num << "Block finished！" << endl;
	}

	return 0;
}

void get(int first, int second, string table_name, MYSQL mysql){
	int blockNumber = first * second_num + second;
	string block = "block/" + to_string(first * second_num) + "/" + to_string(blockNumber) + ".txt";
	string receipt = "other/receipt/" + to_string(first * second_num) + "/" + to_string(blockNumber) + ".txt";

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
		if(!receiptresult[i]["status"].is_null()){
			string status = receiptresult[i]["status"];
			//cout << status << endl;
			if(status == "0x1"){
				string hash = blockresult["transactions"][i]["hash"].get<string>();
				//cout << hash << endl;
				string from = blockresult["transactions"][i]["from"].get<string>();
				//cout << from << endl;
				string input = blockresult["transactions"][i]["input"].get<string>();
				//cout << input << endl;
				string to = "";	//可能to数据是null
				if(!blockresult["transactions"][i]["to"].is_null())
					to = blockresult["transactions"][i]["to"].get<string>();
				//cout << to << endl;
				string value = blockresult["transactions"][i]["value"].get<string>();
				//cout << value << endl;

				char sql[65536] = "";
				sprintf(sql, "insert into %s(Contract, blockNumber, Timestamp, transactionHash, tx_from, tx_to, input, value) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');",\
					(char *)table_name.data(), (char *)to.data(), (char *)number.data(), (char *)timestamp.data(), (char *)hash.data(), (char *)from.data(), (char *)to.data(), (char *)input.data(), (char *)value.data());
				//cout << sql <<endl;
				/*bool ret = mysql_query(&mysql, sql);
				if(ret){
					cout << "写入数据失败！" << endl;
				}else{
					cout << "写入数据成功！" << endl;
				}*/
				mysql_query(&mysql, sql);
			}
		}
	}
	//cout << "Block" << blockNumber << " finished" << endl;
}