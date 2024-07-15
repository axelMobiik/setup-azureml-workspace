# --------------------------------------------------------------------------
# Create the serialized object using joblin dump
# --------------------------------------------------------------------------
import pandas as pd

# Read the data
df = pd.read_csv('./data/adultincome trunc.csv')

# Create a copy of df
data1 = df.copy()

# MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

# Get the numeric columns from data1
columns = data1.select_dtypes(include='number').columns

# Fit the data to the scaler object
scaler_fitted = scaler.fit(data1[columns])

# Transform the data using the fitted scaler object
data1[columns] = scaler_fitted.transform(data1[columns])

# Create the serialised object of the fitted scaler object
import joblib

# Specify the path for the serialised file
obj_file = './outputs/scaler.pkl'

# Dump the object
joblib.dump(value=scaler_fitted, filename=obj_file)