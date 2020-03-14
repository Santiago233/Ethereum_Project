#修改Block.csv，增加label:block一列
import pandas as pd

source_filename = "J:\\Block.csv"
dest_filename = "J:\\Block_new.csv"

source = pd.read_csv(source_filename, low_memory=False)
source['label'] = 'block'

source.to_csv(dest_filename, \
	#columns = ['blockNumber', 'timestamp', 'size', 'difficulty', 'transactionCount', 'minerAddress', 'minerExtra', 'gasLimit', 'gasUsed', 'minGasPrice', 'maxGasPrice', 'avgGasPrice', 'label'],\
	index = 0,\
	header = 1)

print("Success Edition!")

#代码得到的Block_new.csv的最后一列少一个空格，此处之后注意