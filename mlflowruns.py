import mlflow
if __name__=='__main__':
    '''mlflow.start_run()

    mlflow.log_param('learning_rate',0.01)

    mlflow.end_run()
'''
    mlflow.set_experiment('testing_mlflow')
    with mlflow.start_run(run_name='first_run'):
        mlflow.log_param('learning_rate',0.01)
