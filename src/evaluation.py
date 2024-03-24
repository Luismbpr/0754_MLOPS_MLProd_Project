import logging
from abc import ABC, abstractmethod

#import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import root_mean_squared_error

class Evaluation(ABC):
    """
    Abstract class definng strategy for evaluating the models
    """
    @abstractmethod
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        """
        Calculate the scores for the model

        Args:
            y_true: True labels
            y_pred: Predicted labels
        
        Returns:
            None
        """
        pass


class MSE(Evaluation):
    """
    Class for Evaluating MSE Score
    """
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        """
        Evaluation Strategy that uses MSE Mean Squared Error
        
        Args:
            y_true: True labels
            y_pred: Predicted labels

        Returns:
            None
        """
        try:
            logging.info("Calculating MSE")
            mse = mean_squared_error(y_true, y_pred)
            logging.info("MSE: {}".format(mse))
            return mse
        except Exception as e:
            logging.error("Error in calculating MSE: {}".format(e))
            raise e


class R2(Evaluation):
    """
    Class for Evaluating R2 Score
    """
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        """
        Evaluation Strategy that uses R2 Score
        
        Args:
            y_true: True labels
            y_pred: Predicted labels

        Returns:
            None
        """
        try:
            logging.info("Calculating R2 Score")
            r2 = r2_score(y_true, y_pred)
            logging.info("R2 Score: {}".format(r2))
            return r2
        except Exception as e:
            logging.error("Error in calculating R2 Score: {}".format(e))
            raise e


class RMSE(Evaluation):
    """
    Class for Evaluating MSE Score
    """
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        """
        Evaluation Strategy that uses RMSE Root Mean Squared Error
        
        Args:
            y_true: True labels
            y_pred: Predicted labels

        Returns:
            None
        """
        try:
            logging.info("Calculating RMSE")
            ###01
            #### Can use it with y_train, y_test: pd.Series on steps.model_train train_model
            #rmse = mean_squared_error(y_true, y_pred)
            #rmse = np.sqrt(rmse)
            ###02
            #rmse = root_mean_squared_error(y_true, y_pred, squared=False)
            ###03
            #### Can use it with y_train, y_test: pd.DataFrame on steps.model_train train_model
            rmse = mean_squared_error(y_true, y_pred, squared=False)
            logging.info("RMSE: {}".format(rmse))
            return rmse
        except Exception as e:
            logging.error("Error in calculating RMSE: {}".format(e))
            raise e