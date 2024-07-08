#---------------------------------------------------------------------------
# This is the Job Script/Run Configuration script for
# building a pipeline and running it in an experiment
#---------------------------------------------------------------------------
try:
    from azureml.core import Workspace
except ImportError as e:
    print(f"Error importing Azure ML modules: {e}")
    raise

# Access the Workspace
ws = Workspace.from_config('./config')

#---------------------------------------------------------------------------
# Create custom environment
try:
    from azureml.core import Environment
    from azureml.core.environment import CondaDependencies
except ImportError as e:
    print(f"Error importing Azure ML modules: {e}")
    raise

# Create the environment
myenv = Environment(name='MyEnvironment')

# Create the dependencies object
myenv_dep = CondaDependencies.create(
    conda_packages=['scikit-learn', 'pandas'],
    pip_packages=['azureml', 'azureml-sdk', 'azureml-core', 'azureml-dataset-runtime'])
myenv.python.conda_dependencies = myenv_dep


# Register the environment
myenv.register(ws)

#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# Create a compute cluster for pipeline
#---------------------------------------------------------------------------
cluster_name = 'pipeline-cluster'

try:
    from azureml.core.compute import AmlCompute
except ImportError as e:
    print(f"Error importing Azure ML modules: {e}")
    raise

compute_config = AmlCompute.provisioning_configuration(
    vm_size='STANDARD_D11_V2',
    max_nodes=2)

try:
    from azureml.core.compute import ComputeTarget
except ImportError as e:
    print(f"Error importing Azure ML modules: {e}")
    raise

compute_cluster = ComputeTarget.create(ws, cluster_name, compute_config)

compute_cluster.wait_for_completion()

#---------------------------------------------------------------------------
# Create Run Configurations for the steps
try:
    from azureml.core.runconfig import RunConfiguration
except ImportError as e:
    print(f"Error importing Azure ML modules: {e}")
    raise

run_config = RunConfiguration()

run_config.target = compute_cluster
run_config.environment = myenv

#---------------------------------------------------------------------------
# Define Pipeline steps
try:
    from azureml.pipeline.steps import PythonScriptStep
    from azureml.pipeline.core import PipelineData
except ImportError as e:
    print(f"Error importing Azure ML modules: {e}")
    raise

input_ds = ws.datasets.get('Defaults')

dataFolder = PipelineData(
    'datafolder', 
    datastore=ws.get_default_datastore())

# Step 01 - Data Preparation
dataPrep_step = PythonScriptStep(
    name='01 Data Preparation',
    source_directory='./',
    script_name='220 - Dataprep Pipeline2.py',
    inputs=[input_ds.as_named_input('raw_data')],
    outputs=[dataFolder],
    runconfig=run_config,
    arguments=['--datafolder', dataFolder])

# Step 02 - Train the model
train_step = PythonScriptStep(
    name='02 Train the model',
    source_directory='./',
    script_name='220 - Training Pipeline2.py',
    inputs=[dataFolder],
    runconfig=run_config,
    arguments=['--datafolder', dataFolder])

# Config and build the pipeline
steps = [dataPrep_step, train_step]

try:
    from azureml.pipeline.core import Pipeline
except ImportError as e:
    print(f"Error importing Azure ML modules: {e}")
    raise

new_pipeline = Pipeline(
    workspace=ws,
    steps=steps)

# Create the experiment and run the pipeline
try:
    from azureml.core import Experiment
except ImportError as e:
    print(f"Error importing Azure ML modules: {e}")
    raise

new_experiment = Experiment(
    workspace=ws,
    name='PipelineExp01')

new_pipeline_run = new_experiment.submit(new_pipeline)
new_pipeline_run.wait_for_completion(
    show_output=True)

