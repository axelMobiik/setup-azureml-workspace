from azureml.core import Run

new_run = Run.get_context()
ws = new_run.experiment.workspace
# ws = new_run.get_metrics()
# output_dir = new_run.get_file_names()

def data_prep():
    input_ds = ws.datasets.get('AdultIncome').to_pandas_dataframe()
    input_ds = input_ds.drop(['fw', 'edu_num'], axis=1)
    input_ds = input_ds.iloc[:1000, :]
    return input_ds

