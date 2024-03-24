import logging
from abc import ABC, abstractmethod
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
#from sklearn.ensemble import RandomForestRegressor
#from sklearn.base import RegressorMixin


class Model(ABC):
    """
    Abstract class for all models
    """

    @abstractmethod
    #def train(self, X_train, y_train) -> RegressorMixin:
    def train(self, X_train, y_train):
        """
        Trains the model

        Args:
            X_train
            y_train
        
        Returns:
            None
        """
        pass


#class LinearRegressionModel(Model):
class LinearRegressionModel(Model):
    """
    Class Linear Regression Model
    """

    #def train(self, X_train, X_test, y_train, y_test, **kwargs):
    def train(self, X_train, y_train, **kwargs):
        """
        LinearRegressionModel Method for LinearRegressionModel Class
        Trains the model

        Args:
            X_train
            y_train
        
        Returns:
            None
        """
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            logging.info("Model training completed")
            return reg
        except Exception as e:
            logging.error("Error in training model: {}".format(e))
            raise e
#
#
# class RandForestRegressionModel(Model):
#     """
#     Random Forest Regression Model
#     """

#     def train(self, X_train, y_train, **kwargs):
#         """
#         Trains the model

#         Args:
#             X_train
#             y_train
        
#         Returns:
#             None
#         """
#         try:
#             reg = RandomForestRegressor(**kwargs)
#             reg.fit(X_train, y_train)
#             logging.info("Model training completed")
#             return reg
#         except Exception as e:
#             logging.error("Error in training model: {}".format(e))
#             raise e
