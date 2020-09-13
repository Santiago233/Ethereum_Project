import pandas as pd

source_filename = "Transaction_new.csv"
dest_filename_in = "Client_to_Transaction.csv"
dest_filename_out = "Transaction_to_Client.csv"

#client to transaction
source_in = pd.read_csv(source_filename, usecols = ['id', 'from'], low_memory=False)
source_in['relationship'] = 'in'
source_in['from'] = source_in['from'].astype(str)
source_in['from'] = source_in['from'].apply(lambda x :'client' + x)
data_in = pd.DataFrame()
data_in = (source_in.loc[:,['from', 'id', 'relationship']])
newheader_in = ['clientid', 'transactionid', 'relationship']
data_in.to_csv(dest_filename_in, index = False, header = newheader_in)
print("relationship_from generated!")

#transaction_to_client存在client为空的情况(例如第55行数据)，这也导致出现有节点为client的情况
source_out = pd.read_csv(source_filename, usecols = ['id', 'to'], low_memory=False)
source_out['relationship'] = 'out'
source_out['to'] = source_out['to'].astype(str)
source_out['to'] = source_out['to'].apply(lambda x :'client' if x == 'nan' else('client' + x))
#data_out = pd.DataFrame()
#data_out = (source_out.loc[:,['id', 'to', 'relationship']])
newheader_out = ['transactionid', 'clientid', 'relationship']
#data_out.to_csv(dest_filename_out, index = False, header = newheader_out)
source_out.to_csv(dest_filename_out, index = False, header = newheader_out)
print("relationship_to generated!")