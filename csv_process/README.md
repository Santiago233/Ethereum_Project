# CSV文件的处理流程

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