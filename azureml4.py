#---------------------------------------------------------------------------
# Import required classes from azureml
#---------------------------------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset

#---------------------------------------------------------------------------
# Access the workspace by name
#---------------------------------------------------------------------------
ws = Workspace.from_config(path='./config/.azureml')

#---------------------------------------------------------------------------
# List all the workspaces within a subscription
#---------------------------------------------------------------------------
ws_list = Workspace.list(
    subscription_id='68c426c3-a30e-4615-8e9a-6143da75c563')

ws_list = list(ws_list)

#---------------------------------------------------------------------------
# Access the default datastore from workspace
#---------------------------------------------------------------------------
az_default_store = ws.get_default_datastore()
az_default_store

#---------------------------------------------------------------------------
# List all the datastores
#---------------------------------------------------------------------------
store_list = list(ws.datastores)


#---------------------------------------------------------------------------
# Get the dataset by name from a workspace
#---------------------------------------------------------------------------
az_dataset = Dataset.get_by_name(ws, 'Adult Income Using SDK')
az_dataset

az_dataset_loan_applications = Dataset.get_by_name(ws, 'Loan Applications Using SDK')
az_dataset_loan_applications

#---------------------------------------------------------------------------
# List datasets from a workspace
#---------------------------------------------------------------------------
ds_list = list(ws.datasets.keys())
for items in ds_list:
    print(items)
