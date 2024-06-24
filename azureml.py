#---------------------------------------------------------------------------
# Import Workspace class
#---------------------------------------------------------------------------
from azureml.core import Workspace

#---------------------------------------------------------------------------
# Create the workspace
#---------------------------------------------------------------------------
ws = Workspace.create(
    name='Azureml-SDK-WS03',
    subscription_id='68c426c3-a30e-4615-8e9a-6143da75c563',
    resource_group='AzuremlSDKRG03',
    create_resource_group=True,
    location='eastus2')


#---------------------------------------------------------------------------
# Write the config.json file to local directory
#---------------------------------------------------------------------------
ws.write_config(path='./config')
