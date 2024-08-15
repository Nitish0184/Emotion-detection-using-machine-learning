
import mlflow

mlflow.set_tracking_uri('https://dagshub.com/Nitish0184/mlops-project.mlflow')

import dagshub
dagshub.init(repo_owner='Nitish0184', repo_name='mlops-project', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
