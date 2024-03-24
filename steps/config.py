# import logging
# from zenml.steps import BaseParameters


# class ModelNameConfig(BaseParameters):
#     """
#     Model Configs
#     """
#     model_name: str = "LinearRegression"
#     #model_name: str = "RandomForestReg"

#import logging
from zenml.steps import BaseParameters


class ModelNameConfig(BaseParameters):
    """
    Contains the model configuration
    """
    model_name: str = "LinearRegression"
    #model_name: str = "LinearRegressionModel"
    #model_name: str = "RandomForestRegressor"
