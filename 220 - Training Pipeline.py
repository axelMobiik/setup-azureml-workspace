#---------------------------------------------------------------------------
# Model training step of the pipeline run
#---------------------------------------------------------------------------

# Import required classes from Azureml
from azureml.core import Run
import argparse

# Get the context of the experiment run
new_run = Run.get_context()

# Access the workspace
ws = new_run.experiment.workspace

# Get parameters
parser = argparse.ArgumentsParser()
parser.add_arguments('--datafolder', type=str)
args = parser.parse_args()

#---------------------------------------------------------------------------
# Do your stuff here
#---------------------------------------------------------------------------
# Read the data from the previous step
import os
import pandas as pd

path = os.path.join(args.datafolder, 'defaults_preps.csv')
dataPrep = pd.read_csv(path)

# Create X and Y - Similar to "edit columns" in Train Module
X = dataPrep.drop(['Default Next Month_Yes'], axis=1)
y = dataPrep[['Default Next Month_Yes']]

# Split Data - X and y datasets are training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=1234,
    stratify=y)

# Build the Logistic Regression model
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

# Fit the data to the LogisticRegression object - Train Model
lr.fit(X_train, y_train)

# Predict the outcome using Test data - Score Model
# Scored Label
y_predict = lr.predict(X_test)

# Get the probability score - Scored Probabilities
y_prob = lr.predict(X_test)[:, 1]

# Get Confusion matrix and the accuracy/score - Evaluate
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predict)
score = lr.score(X_test, y_test)

#---------------------------------------------------------------------------
# Log metrics and Complete an experiment run
#---------------------------------------------------------------------------

# Create the confusion matrix dictionary
cm_dict = {
    'schema_type': 'confusion_matrix',
    'schema_version': 'v1',
    'data': {
        'class_labels': ['N', 'Y'],
        'matrix': cm.tolist()}}

new_run.log('TotalObservations', len(dataPrep))
new_run.log_confusion_matrix('ConfusionMatrix', cm_dict)
new_run.log('Score', score)

# Create the Scored Dataset and upload to outputs
#---------------------------------------------------------------------------
# Test data - X_test
# Actual y - y_test
# Scored label
# Scored probabilities

X_test = X_test.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)

y_prob_df = pd.DataFrame(y_prob, columns=['Scored Probabilities'])
y_predict_df = pd.DataFrame(y_predict, columns=['Scored Label'])

scored_dataset = pd.concat(
    [X_test, y_test, y_predict_df, y_prob_df],
    axis=1)

# Upload the scored dataset
scored_dataset.to_csv(
    './outputs/defaults_scored.csv',
    index=False)

# Complete the run
new_run.complete()
















