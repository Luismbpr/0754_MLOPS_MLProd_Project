# import logging
# import pandas as pd
# from zenml import step

# @step
# def evaluate_model(df: pd.DataFrame) -> None:
#     pass


import logging
import pandas as pd
import numpy as np
from zenml import step

from src.evaluation import MSE, RMSE, R2
from sklearn.base import RegressorMixin
from typing import Tuple
from typing_extensions import Annotated

### Experiment tracking
import mlflow
from zenml.client import Client
#experiment_tracker = Client().active_stack.experiment_tracker
#@step(experiment_tracker=experiment_tracker.name)
## On terminal zenml experiment-tracker list
#experiment_tracker_name = "mlflow_tracker_customer"
#@step(enable_cache=False, experiment_tracker=experiment_tracker_name)
#@step
#experiment_tracker = Client().active_stack.experiment_tracker
#@step(experiment_tracker=experiment_tracker.name)
#import zenml.integrations.mlflow
experiment_tracker = Client().active_stack.experiment_tracker
@step(experiment_tracker=experiment_tracker.name)
def evaluate_model(model: RegressorMixin,
                   X_test: pd.DataFrame,
                   y_test: pd.Series) -> Tuple[
                         Annotated[float, "r2_score"],
                         Annotated[float, "rmse"]
                         ]:
        """
        Evaluate models
        
        Args:
            model: RegressorMixin,
            X_test: pd.DataFrame,
            y_test: pd.Series
        
        Returns:
            .
            """
        try:
            prediction = model.predict(X_test)
            
            mse_class = MSE()
            mse = mse_class.calculate_scores(y_true=y_test, y_pred=prediction)
            mlflow.log_metric("mse", mse)### Experiment Tracking

            r2_class = R2()
            r2_score = r2_class.calculate_scores(y_true=y_test, y_pred=prediction)
            mlflow.log_metric("r2_score", r2_score)### Experiment Tracking
            
            rmse_class = RMSE()
            rmse = rmse_class.calculate_scores(y_true=y_test, y_pred=prediction)
            mlflow.log_metric("rmse", rmse)### Experiment Tracking

            return r2_score, rmse
        
        except Exception as e:
             logging.error("Error in evaluating model: {}".format(e))
             raise e
        