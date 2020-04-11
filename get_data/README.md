# GraduationProject
Project for my Graduation paper

因为block和transaction等数据分别由block、receipt、trace三部分组成，只要分别请求或许这三部分原始数据，并进行数据处理清洗便可以得到可以用于用于后续处理的csv文件

Step1：getBlock.sh、getReceipt.sh
因为Block和NormalTransaction只需要block和receipt两个部分，所以只需要获取这两部分便可

获取的block数据结构有：result{author、difficulty、extraData、gasLimit、gasUsed、hash、logsBloom、miner、mixHash、nonce、number、parentHash、receiptsRoot、sealFields[,]、sha3Uncles、size、stateRoot、timestamp、totalDifficulty、transactions[{blockHash,blockNumber,chainId,condition,creates,from,gas,gasPrice,hash,input,nonce,publicKey,r,raw,s,standardV,to,transactionIndex,v,value},{}...]、transactionsRoot、uncles[]}

获取的receipt数据结构有：result[{blockHash、blockNumber、contractAddress、cumulativeGasUsed、from、gasUsed、logs[{address、blockHash、blockNumber、data、logIndex、removed、topics[,...]、transactionHash、transactionIndex、transactionLogIndex、type},{}...]、logsBloom、root、to、transactionHash、transactionIndex},{}...]

block文件夹和receipt文件夹分别是分类获取的数据文件夹

Step2：getDataset.cpp(头文件json.hpp)
根据.sh获取的源数据进行处理并且写入csv文件(Block.csv和Transaction.csv)