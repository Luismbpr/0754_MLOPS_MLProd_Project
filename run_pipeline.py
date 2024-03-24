from pipelines.training_pipeline import train_pipeline

####from steps.config import ModelNameConfig
import mlflow
from zenml.client import Client
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri
#import zenml.integrations.mlflow


from zenml.steps import step




if __name__ == "__main__":
    ## Run the pipeline
    ####model_name = "LinearRegression"
    #print(f"experiment_tracker.get_tracking_uri() {Client().active_stack.experiment_tracker.get_tracking_uri()}")
    #experiment_tracker = Client().active_stack.experiment_tracker
    #print(f"Client().active_stack.experiment_tracker {Client().active_stack.experiment_tracker}")
    #print(f"experiment_tracker.name {experiment_tracker.name}")
    #print("Client().active_stack.experiment_tracker.get_tracking_uri()")
    #print(f"{Client().active_stack.experiment_tracker.get_tracking_uri()}")
    #print("Tracking URI {}".format(get_tracking_uri()))
    #train_pipeline(data_path="/Users/luis/Documents/Programming/Courses_Programming/0754 FCC MLOPS Course ML Prod Grade Projects/venv_0754_FCC_MLOPS_MLProd_Projects_311_01/data/olist_customers_dataset_copy01.csv")
    train_pipeline(data_path="./data/olist_customers_dataset_copy01.csv")


#zenml integration install mlflow -y
#zenml experiment-tracker register mlflow_tracker --flavor=mlflow
#zenml model-deployer register mlflow --flavor=mlflow
#zenml stack register mlflow_stack -a default -o default -d mlflow -e mlflow_tracker --set
    
# zenml experiment-tracker list
# zenml model-deployer list
# zenml stack list
# zenml orchestrator list


#zenml stack delete stack_name_to_delete
#zenml model-deployer delete model_deployer_name_to_delete
    


# zenml experiment-tracker register mlflow_tracker_customer --flavor=mlflow
# zenml model-deployer register mlflow_customer --flavor=mlflow
# zenml stack register mlflow_stack_customer -a default -o default -d mlflow_customer -e mlflow_tracker_customer --set


# zenml experiment-tracker list
# zenml model-deployer list
# zenml stack list
# zenml orchestrator list
#zenml pipeline list
    
#How do I change the active stack in ZenML?
#You can change the active stack in ZenML by running the following command in your terminal:
#zenml stack set my_stack
    
#If you want the name of the current experiment tracker, use the get command:
#zenml experiment-tracker get
#No experiment tracker set for active stack ('default').

### Using an experiment tracker   
#% zenml stack set mlflow_stack_customer
#% zenml experiment-tracker list
### After setting the stack mlflow_stack_customer I checked and the experiment-tracker is now active
    


# zenml experiment-tracker list
# zenml artifact-store describe
# zenml artifact-store list
# zenml stack list
# zenml stack set default
# zenml stack list
# zenml artifact-store list
# zenml stack set mlflow_stack_customer
    

##Client().active_stack.experiment_tracker.get_tracking_uri()
### uri
##file:/Users/luis/Library/Application Support/zenml/local_stores/e63160d8-544f-417d-8350-b5becab076c0/mlruns
#mlflow ui --backend-store-uri "file:/Users/luis/Library/Application Support/zenml/local_stores/e63160d8-544f-417d-8350-b5becab076c0/mlruns"



#zenml integration install mlflow -y
#zenml experiment-tracker register mlflow_tracker_customer_02 --flavor=mlflow
#zenml model-deployer register mlflow_customer_02 --flavor=mlflow
#zenml stack register mlflow_stack_customer_02 -a default -o default -d mlflow_customer_02 -e mlflow_tracker_customer_02 --set
    

# zenml down
# zenml up
# clear
# zenml experiment-tracker register mlflow_tracker_customer_05 --flavor=mlflow
# zenml down
# zenml up
# clear
# zenml model-deployer register mlflow_customer_05 --flavor=mlflow
# zenml down
# zenml up
# clear
# zenml stack register mlflow_stack_customer_05 -a default -o default -d mlflow_customer_05 -e mlflow_tracker_customer_05 --set
# zenml down
# zenml up
# clear
# zenml stack set mlflow_stack_customer_05
# zenml stack list
    

# # pip uninstall 'catboost==1.0.4'
# # pip uninstall 'joblib>=1.1.0'
# # pip install 'lightgbm==4.1.0' ## pip install cmake
# # pip install 'optuna==2.10.0'
# # pip install 'streamlit==1.29.0'
# # pip install 'xgboost==2.0.3'
# # pip install 'markupsafe==1.1.1'
# # pip install 'scikit-learn>=1.3.2'
# # pip install altair
# # pip install 'zenml>=0.52.0'
    


