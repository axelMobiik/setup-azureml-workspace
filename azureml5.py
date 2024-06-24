#---------------------------------------------------------------------------
# Import required classes from Azureml
#---------------------------------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset

#---------------------------------------------------------------------------
# Access the Workspace, Datastore and Dataset
#---------------------------------------------------------------------------
ws = Workspace.from_config(path='./config/.azureml')
az_store = Datastore.get(ws, 'azure_sdk_blob01')
az_dataset = Dataset.get_by_name(ws, 'Adult Income Using SDK')
az_dataset_loan = Dataset.get_by_name(ws, 'Loan Applications Using SDK')
az_default_store = ws.get_default_datastore()

#---------------------------------------------------------------------------
# Load the Azureml Dataset into the pandas dataframe
#---------------------------------------------------------------------------
df = az_dataset.to_pandas_dataframe()
df_loan = az_dataset_loan.to_pandas_dataframe()

#---------------------------------------------------------------------------
# Upload the dataframe to the azureml dataset
#---------------------------------------------------------------------------
df_loan_sub = df_loan[['Married', 'Gender', 'Loan_Status']]

az_ds_from_df = Dataset.Tabular.register_pandas_dataframe(
    dataframe=df_loan_sub,
    target=az_store,
    name='Loan Dataset From Dataframe')
