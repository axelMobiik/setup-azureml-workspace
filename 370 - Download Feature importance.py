# ------------------------------------------------------------------------
# Retrive/Download the feature importance values
# ------------------------------------------------------------------------
from azureml.interpret import ExplanationClient
from azureml.core import Workspace

# Access the workspace using config.json
ws = Workspace.from_config('./config')

# Access the run using run_id
new_run = ws.get_run('Explainer_Exp001_1720211039_a2900786')

# Define an Explanation Client
explain_client = ExplanationClient.from_run(new_run)

# Download the explanations using explain client
downloaded_explanations = explain_client.download_model_explanation()

# Get the feature importance in a dictionary
feature_importances = downloaded_explanations.get_feature_importance_dict()
