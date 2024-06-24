#---------------------------------------------------------------------------
# Run a script in an Azureml environment
#---------------------------------------------------------------------------
# This code will submit the script provided in ScriptingRunConfig
# and create an Azureml environment on the local machine
# including the docker for Azureml
#---------------------------------------------------------------------------

# Import the Azureml classes
from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment

# Access the workspace using config.json
path_config = "C:/Users/AxelCoronadoZepeda/Documents/Data Scients Certificate/DP-100 A-Z Machine Learning using Azure Machine Learning/setup-azure-machine-learning-workspace/config/.azureml/config.json"
ws = Workspace.from_config(path=path_config)

new_experiment = Experiment(
    workspace=ws,
    name='Loan_Script')

env = Environment(name="user-managed-env")
env.python.user_managed_dependencies = True

script_config = ScriptRunConfig(
    source_directory='Documents/Data Scients Certificate/DP-100 A-Z Machine Learning using Azure Machine Learning/setup-azure-machine-learning-workspace',
    script='180 - Script To Run.py',
    environment=env)

# Submit a new run using the ScriptRunConfig
new_run = new_experiment.submit(config=script_config)

# Create a wait for completion of the script
new_run.wait_for_completion()

