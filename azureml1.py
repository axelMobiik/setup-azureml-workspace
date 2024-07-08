#---------------------------------------------------------------------------
# Import Workspace class
#---------------------------------------------------------------------------
from azureml.core import Workspace
from azureml.core.authentication import InteractiveLoginAuthentication

#---------------------------------------------------------------------------
# Create the workspace
#---------------------------------------------------------------------------
# interactive_auth = InteractiveLoginAuthentication(tenant_id="ec11da7c-17f5-4a75-b455-963cef89c864")

ws = Workspace.create(
    name='Azureml-SDK-WS01',
    subscription_id='9a619830-ec3d-4a92-8c55-a134a3a0bd56',
    resource_group='AzuremlSDKRG01',
    create_resource_group=True,
    location='eastus2')


#---------------------------------------------------------------------------
# Write the config.json file to local directory
#---------------------------------------------------------------------------
ws.write_config(path='./config')
