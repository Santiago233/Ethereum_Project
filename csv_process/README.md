# CSV文件的处理流程

Step 1:csv_readhead.py
防止csv文件过大无法打开查看表头

Step 2:block_addlabel.py
给Block.csv文件的表头添加label标签

Step 3:transaction_getclients.py
根据Transaction.csv文件得到所有的交易节点

Step 4:transaction_addlabel.py
给Transaction.csv文件的表头添加label标签
(使用部分Transaction数据，所以实则使用Transaction_tmp.csv文件)

Step 5:transaction_to_block.py
建立transaction和block的关系
(transaction -> block)

Step 6:clients_to_transaction.py