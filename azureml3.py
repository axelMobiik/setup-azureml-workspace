#---------------------------------------------------------------------------
# Import required azureml classes
#---------------------------------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset

#---------------------------------------------------------------------------
# Access the workspace from the config.json
#---------------------------------------------------------------------------
ws = Workspace.from_config(path='./config/.azureml')

# Access
az_store = Datastore.get(ws, 'azure_sdk_blob01')

# Create the path of the csv file
csv_path = [(az_store, 'UI/2024-06-11_202234_UTC/adultincome+first+100.csv')]
csv_path_loan_approval = [(az_store, 'Loan Data/Loan Approval Prediction.csv')]

# Create the dataset
adult_income_dataset = Dataset.Tabular.from_delimited_files(path=csv_path)
loan_approval_dataset = Dataset.Tabular.from_delimited_files(path=csv_path_loan_approval)

# Register the dataset
adult_income_dataset = adult_income_dataset.register(
    workspace=ws, 
    name='Adult Income Using SDK',
    create_new_version=True)

loan_approval_dataset = loan_approval_dataset.register(
    workspace=ws,
    name='Loan Applications Using SDK',
    create_new_version=True)
