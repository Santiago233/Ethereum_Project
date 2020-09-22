# GraduationProject
Project for my Graduation paper

将get_data文件夹下代码自主拉取的ethereum数据导入csv文件并对csv文件进一步处理

本project中使用的ethereum数据文件为Block文件和NormalTransaction文件

本project中使用的本地同步ethereum的工具为parity

parity下载地址：https://github.com/openethereum/openethereum/releases

Step 0:getDataset.cpp(头文件json.hpp)
根据.sh获取的源数据进行处理并且写入csv文件(Block.csv和Transaction.csv)

Step 1:csv_readhead.py
防止csv文件过大无法打开查看表头

Step 2:block_add.py
给Block.csv文件的表头添加id、label标签

Step 3:transaction_get.py
根据Transaction.csv文件得到所有的交易节点

Step 4:transaction_add.py
给Transaction.csv文件的表头添加id、label标签
(使用部分Transaction数据，所以实则使用Transaction_tmp.csv文件)

Step 5:transaction_to_block.py
建立transaction和block的关系
(transaction -> block)

Step 6:client_to_transaction.py
建立client和transaction的关系
(包括in和out)


备注：代码生成的csv表头可能不符合neo4j使用import命令导入csv文件的格式，为了不再次生成便直接在最终的csv文件中进行了修改————

将nodes文件改成id:ID(block)、id:ID(transaction)、id:ID(client)的格式；
将relationships文件改成:START_ID(transaction),:END_ID(block),:TYPE之类的格式。

具体指令：./neo4j-admin import --database=graph.db --nodes ../import/Block_new.csv --nodes ../import/Clients_new.csv --nodes ../import/Transaction_new.csv --relationships ../import/Client_to_Transaction.csv --relationships ../import/Transaction_to_Block.csv --relationships ../import/Transaction_to_Client.csv