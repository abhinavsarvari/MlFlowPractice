import mlflow
from typing import Any
import mlflow_utils

'''if __name__=='__main__':
    mlflow.create_experiment(
        name='testing_mlflow',
        artifact_location="testing_mlflow_location",
        tags={'env':'dev','version':'1.0.0'}
    )
'''

experiment_id= mlflow_utils.create_mlflow_experiment(experiment_name='testing_mlflow1',artifact_location='testing_mlflow_location',tags={'env':'dev','version':'1.0.0'})
print(f'Experiment_id: {experiment_id}')