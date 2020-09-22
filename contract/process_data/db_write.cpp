#include <vector>
#include <string>
#include <io.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
//#include "json.hpp"	//德国大牛的hpp，提供json类型
#include <mysql/mysql.h>

using namespace std;
//using json = nlohmann::json;

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

	string sql = "create table if not exists contract(Contract varchar(1000), blockNumber varchar(1000), Timestamp varchar(1000), transactionHash varchar(1000), tx_from varchar(1000), tx_to varchar(1000), input varchar(1000), value varchar(1000))";
	cout << sql << endl;
	bool ret2 = mysql_query(&mysql, (char *)sql.data());
	if(!ret2){
		cout << "创建数据表失败！" << endl;
	}else{
		cout << "创建数据表成功！" << endl;
	}
}