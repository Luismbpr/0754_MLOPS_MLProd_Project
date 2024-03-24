import logging
import pandas as pd
from zenml import step
#from src.model_dev import RandForestRegressionModel

from sklearn.base import RegressorMixin
from src.model_dev import LinearRegressionModel

#from steps.config import ModelNameConfig
from .config import ModelNameConfig

#import mlflow
#from zenml.client import Client

#experiment_tracker = Client().active_stack.experiment_tracker
#print("experiment_tracker name: {}".format(experiment_tracker))
#@step(experiment_tracker=experiment_tracker.name)

# @step
# def train_model(df: pd.DataFrame) -> None:
#     pass


###def train_model(X_train, X_test, y_train, y_test) -> LinearRegressionModel:
### Experiment tracking
import mlflow
from zenml.client import Client
#experiment_tracker = Client().active_stack.experiment_tracker
#@step(experiment_tracker=experiment_tracker.name)
## On terminal zenml experiment-tracker list
#experiment_tracker_name = "mlflow_tracker_customer"
#@step(enable_cache=False, experiment_tracker=experiment_tracker_name)
#@step
# experiment_tracker = Client().active_stack.experiment_tracker
# @step(experiment_tracker=experiment_tracker.name)
import zenml.integrations.mlflow
experiment_tracker = Client().active_stack.experiment_tracker
@step(experiment_tracker=experiment_tracker.name)
def train_model(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    #y_train: pd.Series,
    #y_test: pd.Series,
    y_train: pd.DataFrame,
    y_test: pd.DataFrame,
    config: ModelNameConfig,
    ) -> RegressorMixin:
    """
    X_train: pd.DataFrame
    X_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series
    config: ModelNameConfig
    """
    ## Create config.py
    model = None
    try:
        ## Note: it is config.model_name and not ModelNameConfig
        if config.model_name == "LinearRegression":
            mlflow.sklearn.autolog()### Experiment Tracking
            #model = LinearRegressionModel().train(X_train, y_train)
            model = LinearRegressionModel()
            trained_model = model.train(X_train, y_train)
            logging.info("Model Trained Successfully")
            return trained_model
        # elif config.model_name == "RandomForestRegressor":
        #     mlflow.sklearn.autolog()### Experiment Tracking
        #     model = RandomForestRegressor().train(X_train, y_train)
        #     model = RandomForestRegressor()
        #     trained_model = model.train(X_train, y_train)
        #     logging.info("Model Trained Successfully")
        #     return trained_model
        else:
            raise ValueError("Model {} not suported".format(config.model_name))
    except Exception as e:
        logging.error("Error in training model: {}".format(e))
        raise e