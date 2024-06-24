#---------------------------------------------------------------------------
# Import the workspace and Datastore class
#---------------------------------------------------------------------------
from azureml.core import Workspace, Datastore

#---------------------------------------------------------------------------
# Access the workspace from the config.json (view the file azureml.py)
#---------------------------------------------------------------------------
ws = Workspace.from_config(path='./config')

#---------------------------------------------------------------------------
# Create a datastore pulling container information from a storage account
#---------------------------------------------------------------------------
az_store = Datastore.register_azure_blob_container(
    workspace=ws,
    datastore_name='azure_sdk_blob01',
    account_name='axelstorage001',
    container_name='storage',
    account_key='PvzEeTgfDp6EwBXT68K+6VrIIlmVkwMZVrPl1MNLbvsYZZwUh2MYI1KR7mToRWSU9tBt1Ij2JRgE+AStYOp47Q==')
