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
data = pd.DataFrame()
data = (source.loc[:,['transactionHash', 'blockNumber', 'relationship']])
data.to_csv(dest_filename, index = False)

print("relationship generated!")