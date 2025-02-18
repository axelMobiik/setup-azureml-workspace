#---------------------------------------------------------------------------
# Import required classes from Azureml
#---------------------------------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset, Experiment

#---------------------------------------------------------------------------
# Access the Workspace, Datastore and Datasets
#---------------------------------------------------------------------------
path_config = "C:/Users/AxelCoronadoZepeda/Documents/Data Scients Certificate/DP-100 A-Z Machine Learning using Azure Machine Learning/setup-azure-machine-learning-workspace/config/.azureml/config.json"
ws = Workspace.from_config(path=path_config)
az_store = Datastore.get(ws, 'azure_sdk_blob01')
az_dataset = Dataset.get_by_name(ws, 'Loan Applications Using SDK')
az_default_store = ws.get_default_datastore()

#---------------------------------------------------------------------------
# Create/Access an experiment object
#---------------------------------------------------------------------------
experiment = Experiment(
    workspace=ws,
    name='Loan-SDK-Exp01')

#---------------------------------------------------------------------------
# Run an experiment using start_logging method
#---------------------------------------------------------------------------
new_run = experiment.start_logging(snapshot_directory=None)

#---------------------------------------------------------------------------
# Do your stuff here
#---------------------------------------------------------------------------
df = az_dataset.to_pandas_dataframe()
# Count the observations
total_observations = len(df)
# Get the null/missing values
nulldf = df.isnull().sum()


#---------------------------------------------------------------------------
# Log metrics and Complete an experiment run
#---------------------------------------------------------------------------
# Log the metrics to the workspace
new_run.log('Total Observations', total_observations)

# Log the missing data values
for columns in df.columns:
    new_run.log(columns, nulldf[columns])

new_run.complete()
