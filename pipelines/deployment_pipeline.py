import numpy as np
import pandas as pd
#import mlflow
#import os

from zenml import pipeline, step

#from materializer.custom_materializer import cs_materializer

from zenml.config import DockerSettings
from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
from zenml.integrations.constants import MLFLOW
#from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import MLFlowModelDeployer
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
    MLFlowModelDeployer,
)

from zenml.integrations.mlflow.services import MLFlowDeploymentService
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
from zenml.steps import BaseParameters, Output

from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model

#from .utils import get_data_for_test
from pipelines.utils import get_data_for_test
import json


docker_settings = DockerSettings(required_integrations=[MLFLOW])


class DeploymentTriggerConfig(BaseParameters):
    """
    Deployment Trigger Config
    """
    min_accuracy: float = 0

@step(enable_cache=False)
def dynamic_importer() -> str:
    """
    Dynamically import the MLflow prediction server
    Downloads the data from a mock API

    Args:
        .
    
    Returns:
        .
    """
    ## Create pipelines.utils.get_data_for_test() 
    data = get_data_for_test()
    return data


@step
def deployment_trigger(
    accuracy: float,
    config: DeploymentTriggerConfig,
#) -> bool:
):
    """
    Deployment Trigger
    Implements a simple model deployment trigger
    that looks at the input model accuracy 
    and decides if it is good enough to deploy.
    """
    return accuracy > config.min_accuracy


class MLFlowDeploymentLoaderStepParameters(BaseParameters):
    """
    MLFlow deployment getter parameters

    Attributes:
        pipeline_name: name of the pipeline that deployed the MLflow prediction server
        step_name: The name of the step that deployed the MLFlow prediction server
        running: When this flag is set, the step only returns a running service
        model_name: The name of the model that is deployes
    """

    pipeline_name: str
    step_name: str
    running: bool = True


@step(enable_cache=False)
def prediction_service_loader(
    pipeline_name: str,
    pipeline_step_name: str,
    running: bool = True,
    model_name: str = "model",
) -> MLFlowDeploymentService:
    """
    Get the prediction service started by the deployment pipeline.

    Args:
        pipeline_name: Name of the pipeline that deployed the MLflow prediction server.
        pipeline_step_name: The name of the step that deployed the MLflow prediction server
        running: bool = When this flag is set, the step only returns a running service
        model_name: The name of the model that is deployed

    Returns:
        MLFlowDeploymentService
    """
    ## Get the MLflow deployer stack component
    mlflow_model_deployer_component = MLFlowModelDeployer.get_active_model_deployer()
    
    ## Fetch existing services with same pipeline name, step name and model name
    existing_services = mlflow_model_deployer_component.find_model_server(
        pipeline_name=pipeline_name,
        pipeline_step_name=pipeline_step_name,
        model_name=model_name,
        running=running,
    )
    
    if not existing_services:
        raise RuntimeError(
            f"No MLFlow deployment service found for pipeline {pipeline_name}, "
            f"step {pipeline_step_name} and model {model_name}."
            f"pipeline for the '{model_name}' model is currently "
            f"running"
            )
    #print(f"existing_services: {existing_services}")
    #print(f"type(existing_services) {type(existing_services)}")
    return existing_services[0]

@step
def predictor(
    ## Note: data should be str and not np.ndarray
    service: MLFlowDeploymentService,
    data: str,
) -> np.ndarray:
    ## Need to create a step dynamic data importer
    ## Need Create on deployment_pipeline (here) deployment_trigger()
    #pass
    service.start(timeout=10) ## Should be a NOP if already started
    data = json.loads(data)
    data.pop("columns")
    data.pop("index")
    columns_for_df = [
        "payment_sequential",
        "payment_installments",
        "payment_value",
        "price",
        "freight_value",
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    ]
    df = pd.DataFrame(data["data"], columns=columns_for_df)
    json_list = json.loads(json.dumps(list(df.T.to_dict().values())))
    data = np.array(json_list)
    prediction = service.predict(data)
    return prediction


## Deployment pipeline
@pipeline(enable_cache=False, settings={"docker": docker_settings})
def continuous_deployment_pipeline(
    data_path: str,
    min_accuracy: float = 0,
    workers: int = 1,
    ## Stop pipeline if it is taking too much
    timeout: int = DEFAULT_SERVICE_START_STOP_TIMEOUT,
    ):
    df = ingest_df(data_path=data_path)
    X_train, X_test, y_train, y_test = clean_df(df)
    model = train_model(X_train, X_test, y_train, y_test)
    r2_score, rmse = evaluate_model(model, X_test, y_test)
    ## Create the deployment Criteria
    ## Create a deployment decision step -> Create deployment_pipeline.DeploymentTriggerConfig class -> deployment_trigger()
    ## Takes the r2_score and the min_accuracy from DeploymentTriggerConfig
    #deployment_decision = deployment_trigger(accuracy=r2_score)
    deployment_decision = deployment_trigger(r2_score)
    ## Takes (r2_score or rmse), and only deploys the model it it is greater than min accuracy
    ## from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
    ## mlflow_model_deployer_step is used to deploy the model
    mlflow_model_deployer_step(
        model=model,
        ## Error, it is not deployment_decision =, it is deploy_decision =
        ##deployment_decision=deployment_decision,###Error
        deploy_decision=deployment_decision,## Solution
        workers=workers,
        timeout=timeout,
    )


@pipeline(enable_cache=False, settings={"docker": docker_settings})
def inference_pipeline(pipeline_name: str, pipeline_step_name: str):
    """Link all the steps artifacts together"""
    data = dynamic_importer()
    service = prediction_service_loader(
        pipeline_name=pipeline_name,
        pipeline_step_name=pipeline_step_name,
        running=False,
    )
    prediction = predictor(service=service, data=data)
    return prediction

# @pipeline(enable_cache=False, settings={"docker": docker_settings})
# def inference_pipeline(pipeline_name: str, pipeline_step_name: str):
#     """ Link all the steps artifacts together"""
#     batch_data = dynamic_importer()
#     model_deployment_service = prediction_service_loader(
#         pipeline_name=pipeline_name,
#         pipeline_step_name=pipeline_step_name,
#         running=False,
#         )
#     predictor(service=model_deployment_service, data=batch_data)
