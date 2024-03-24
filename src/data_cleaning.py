import logging
import numpy as np
import pandas as pd
from abc import ABC, abstractmethod
from typing import Union
from sklearn.model_selection import train_test_split


class DataStrategy(ABC):
    """
    Abstract Class defining strategy for handling data
    """

    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        pass


class DataPreProcessStrategy(DataStrategy):
    """
    Data preprocessing strategy to preprocess the data.
    
    Methods:
        handle_data
    """

    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess data
            - Removes columns that are not required (For this example)
            - Fills missing values with median average values.
            - Converts the data type to float.
        Note: These columns are important!
        """
        try:
            ## Dropping Columns
            data = data.drop(
                [
                    "order_approved_at",
                    "order_delivered_carrier_date",
                    "order_delivered_customer_date",
                    "order_estimated_delivery_date",
                    "order_purchase_timestamp"
                ], axis=1)
            
            ## Null Values - Fill Values
            data["product_weight_g"].fillna(data["product_weight_g"].median(), inplace=True)
            data["product_length_cm"].fillna(data["product_length_cm"].median(), inplace=True)
            data["product_height_cm"].fillna(data["product_height_cm"].median(), inplace=True)
            data["product_width_cm"].fillna(data["product_width_cm"].median(), inplace=True)
            data["review_comment_message"].fillna("No review", inplace=True)

            ## Selecting only numeric type columns
            ## Dropping non-numerical type columns
            data = data.select_dtypes(include=[np.number])
            cols_to_drop = ["customer_zip_code_prefix", "order_item_id"]
            data = data.drop(cols_to_drop, axis=1)
            return data
        
        except Exception as e:
            logging.error("Error in preprocessing data {}".format(e))
            raise e


class DataDivideStrategy(DataStrategy):
    """
    Data preprocessing strategy to split the data.
    
    Methods:
        handle_data
    """
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        """
        Divide data into train and test set.
        Args:
            data: pd.DataFrame
        
        Returns:
            X_train, X_test -> pd.DataFrame
            y_train, y_test -> pd.Series
        """
        try:
            X = data.drop(["review_score"], axis=1)
            y = data["review_score"]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            #logging.info("Successful Data Split")
            # pass
            ## X -> DataFrame and y -> Series
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logging.error("Error in dividing data {}".format(e))
            return e
        
class DataCleaning:
    """
    Data class that processes and splits the data into training and testing set
    """
    def __init__(self, data: pd.DataFrame, strategy: DataStrategy):
        #pass
        self.data = data
        self.strategy = strategy
    
    def handle_data(self) -> Union[pd.DataFrame, pd.Series]:
        """
        Handle data

        Args:
            data: pd.DataFrame
            Strategy: DataStrategy
            
        Available Data Strategies:
            - DataPreProcessStrategy
            - DataDivideStrategy
        
        Returns:
            - X_train, X_test: pd.DataFrame
            - y_train, y_test: pd.Series
        """
        try:
            ###print(f"self.strategy.handle_data(self.data): {self.strategy.handle_data(self.data)}")
            return self.strategy.handle_data(self.data)
        except Exception as e:
            logging.error("Error in handling data: {}".format(e))
            raise e


# ## Example
# if __name__ == "__main__":
#     data = pd.read_csv("/Users/luis/Documents/Programming/Courses_Programming/0754 FCC MLOPS Course ML Prod Grade Projects/venv_0754_FCC_MLOPS_MLProd_Projects_311_01/data/olist_customers_dataset_copy01.csv")
#     data_cleaning = DataCleaning(data=data, strategy=DataPreProcessStrategy())
#     data_cleaning.handle_data()
#     ##