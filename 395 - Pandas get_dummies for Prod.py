# -------------------------------------------------------------------------
# Demo of how to handle dummy variable in Production
# -------------------------------------------------------------------------

import pandas as pd

# Creating dataframes
X_train = pd.DataFrame({
    'name': ['Jitesh', 'Rahul', 'John', 'Bill'],
    'income': [40, 50, 60, 70],
    'education': ['Grad', 'Grad', 'Post-Grad', 'Post-Grad']})

# Create dummy variables
X_train_enc = pd.get_dummies(X_train)

# Extract column names as the index object
train_enc_cols = X_train_enc.columns

# Serialize the column index
import joblib

obj_file = './outputs/columns.pkl'

joblib.dump(
    value=train_enc_cols,
    filename=obj_file)

# -------------------------------------------------------------------------
# Production usage of index object
# -------------------------------------------------------------------------
ref_cols = joblib.load(obj_file)

# Example Input data for the webservice
X_deploy = pd.DataFrame({
    'name': ['Jitesh'],
    'income': [70],
    'education': ['Post-Grad1']})

# Create dummy variables of the production data
X_deploy_enc = pd.get_dummies(X_deploy)

# Extract column names of prod data
deploy_cols = X_deploy_enc.columns

# Get missing columns
missing_cols = ref_cols.difference(deploy_cols)

for cols in missing_cols:
    X_deploy_enc[cols] = 0
    
X_deploy_enc = X_deploy_enc[ref_cols]

# Unknown category
extra_cols = deploy_cols.difference(ref_cols)

if len(extra_cols):
    print('There is an unknown category')
