import pandas as pd

source_filename = "J:\\Transaction_new.csv"
dest_filename = "J:\\Transaction_to_Block.csv"

'''
source = pd.read_csv(source_filename, usecols=[' transactionHash', 'blockNumber'], low_memory=False)
source['relationship'] = 'belong'
source.to_csv(dest_filename, index = False)
'''

source = pd.read_csv(source_filename, low_memory=False)
source['relationship'] = 'belong'
source['blockNumber'] = source['blockNumber'].astype(str)
source['blockNumber'] = source['blockNumber'].apply(lambda x :'block' + x)
data = pd.DataFrame()
data = (source.loc[:,['id', 'blockNumber', 'relationship']])
newheader = ['transactionid', 'blockid', 'relationship']
data.to_csv(dest_filename, index = False, header = newheader)

print("relationship generated!")