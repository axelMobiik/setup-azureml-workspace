#---------------------------------------------------------------------------
# Run a script in an Azureml environment
#---------------------------------------------------------------------------
# This code will submit the script provided in ScriptingRunConfig
# and create an Azureml environment on the local machine
# including the docker for Azureml
#---------------------------------------------------------------------------

# Import the Azureml classes
from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment
from azureml.core.environment import CondaDependencies

# Access the workspace using config.json
path_config = "C:/Users/AxelCoronadoZepeda/Documents/Data Scients Certificate/DP-100 A-Z Machine Learning using Azure Machine Learning/setup-azure-machine-learning-workspace/config/.azureml/config.json"
ws = Workspace.from_config(path=path_config)

# Create/access the experiment from workspace
new_experiment = Experiment(
    workspace=ws,
    name='Training_Script')

#---------------------------------------------------------------------------
# Create custom environment
myenv = Environment(name="MyEnvironment")

# Create the dependencies
myenv_dep = CondaDependencies.create(conda_packages=['scikit-learn'])
myenv.python.conda_dependencies = myenv_dep
myenv.python.user_managed_dependencies = True
myenv.register(ws)

# Register the environment
myenv.register(ws)

#---------------------------------------------------------------------------
# Create a script configuration for custom environment of myenv
script_config = ScriptRunConfig(
    source_directory='',
    script='200 - Training Script.py',
    environment=myenv)

# Submit a new run using the ScriptRunConfig
new_run = new_experiment.submit(config=script_config)

# Create a wait for completion of the script
new_run.wait_for_completion()

