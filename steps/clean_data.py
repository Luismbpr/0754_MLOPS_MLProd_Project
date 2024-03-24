# import logging
# import pandas as pd
# from zenml import step

#@step
#def clean_df(df: pd.DataFrame) -> None:
#    pass

import logging
import pandas as pd
from zenml import step
from src.data_cleaning import DataCleaning, DataPreProcessStrategy, DataDivideStrategy
## Annotated Python built-in type setting built in parameters
from typing_extensions import Annotated
from typing import Tuple

@step
def clean_df(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, "X_train"],
    Annotated[pd.DataFrame, "X_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"],
]:
    """
    Clean the data and divides it into Train and Test Set

    Args:
        df: pd.DataFrame -> Raw Data

    Returns:
        Annotated[pd.DataFrame, "X_train"] -> train data
        Annotated[pd.DataFrame, "X_test"] -> test data
        Annotated[pd.Series, "y_train"] -> train labels
        Annotated[pd.Series, "y_test"] -> test labels
    """
    try:
        process_strategy = DataPreProcessStrategy()
        data_cleaning = DataCleaning(df, process_strategy)
        processed_data = data_cleaning.handle_data()

        divide_strategy = DataDivideStrategy()
        data_cleaning = DataCleaning(processed_data, divide_strategy)
        X_train, X_test, y_train, y_test = data_cleaning.handle_data()
        logging.info("Data cleaning completed")
        ## Error
        ##TypeError: cannot unpack non-iterable StepArtifact object
        ## It was not returning anything
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logging.error("Error {}".format(e))
        raise e