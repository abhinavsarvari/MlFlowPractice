import mlflow
from mlflow_utils import get_mlflow_experiment

if __name__=='__main__':
    experiment = get_mlflow_experiment(experiment_name='testing_mlflow1')
    print(f'Name: {experiment.name}')
    print(f'Experiment_id: {experiment.experiment_id}')
    print(f'Artifact_Location: {experiment.artifact_location}')
    print(f'LifeCycle Stage: {experiment.lifecycle_stage}')
    print(f'Creation Time: {experiment.creation_time}')
