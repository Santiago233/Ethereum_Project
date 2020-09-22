# GraduationProject
Project for my Graduation paper

因为block和transaction等数据分别由block、receipt、trace三部分组成，只要分别请求或许这三部分原始数据，并进行数据处理清洗便可以得到可以用于用于后续处理的csv文件

getBlock.sh、getReceipt.sh
因为Block和NormalTransaction只需要block和receipt两个部分，所以只需要获取这两部分便可(实际上运行getBlcok.sh得到的数据便够用)

数据获取前需要parity(官网下载即可)在本地节点同步数据，同时运行脚本时保持parity运行状态，否则获取到的都是null数据

获取的block数据结构有：result{author、difficulty、extraData、gasLimit、gasUsed、hash、logsBloom、miner、mixHash、nonce、number、parentHash、receiptsRoot、sealFields[,]、sha3Uncles、size、stateRoot、timestamp、totalDifficulty、transactions[{blockHash,blockNumber,chainId,condition,creates,from,gas,gasPrice,hash,input,nonce,publicKey,r,raw,s,standardV,to,transactionIndex,v,value},{}...]、transactionsRoot、uncles[]}

获取的receipt数据结构有：result[{blockHash、blockNumber、contractAddress、cumulativeGasUsed、from、gasUsed、logs[{address、blockHash、blockNumber、data、logIndex、removed、topics[,...]、transactionHash、transactionIndex、transactionLogIndex、type},{}...]、logsBloom、status、to、transactionHash、transactionIndex},{}...]

block文件夹和receipt文件夹分别是分类获取的数据文件夹(为了方便测试，选取了部分重复数据，blockNumber为0xb7acf)