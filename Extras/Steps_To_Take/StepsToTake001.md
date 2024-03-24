Steps to take

Create a virtual environment Python version needed
- Python version: python==3.9.18
- Activate Virtual environment
- Install requirements.txt library version

```shell
cd ~
source start_miniforge.sh
cd '/Users/luis/Documents/Proyects_To_Export/0754_FCCMLOPS_MLProd_Project/venv_0754_FCC_MLOPS_MLProd_Projects_309_01_01/'
conda create --name venv_0754_FCC_MLOPS_MLProd_Projects_309_01_01 python=3.9.18
conda activate venv_0754_FCC_MLOPS_MLProd_Projects_309_01_01

pip install -r requirements.txt
conda install nb_conda_kernels
conda install ipykernel
python -m ipykernel install --user --name ex --display-name "venv_0754_FCC_MLOPS_MLProd_Projects_311_02"
```

Initialize Zenml (only one time)

```shell
zenml init
```

Activate zenml environment

```shell
zenml down
zenml disconnect
zenml up
```

Create a zenml stack, experiment-tracker and model-deployer component
Note: Had to use zenml down and up every time because the server was getting disconnected.
Although it was getting disconnected all of them were created
```shell
zenml down
zenml up
clear
zenml experiment-tracker register mlflow_tracker_customer_05 --flavor=mlflow
zenml down
zenml up
clear
zenml model-deployer register mlflow_customer_05 --flavor=mlflow
zenml down
zenml up
clear
zenml stack register mlflow_stack_customer_05 -a default -o default -d mlflow_customer_05 -e mlflow_tracker_customer_05 --set
zenml down
zenml up
clear
zenml stack set mlflow_stack_customer_05
zenml stack list
```

```shell
cd '/Users/luis/Documents/Proyects_To_Export/0754_FCCMLOPS_MLProd_Project/venv_0754_FCC_MLOPS_MLProd_Projects_309_01_01/Extras/Scripts/'
touch Zenml_Create_New_Stack_001.sh
vim Zenml_Create_New_Stack_001.sh
esc + :wq
chmod 755 Zenml_Create_New_Stack_001.sh
Or
chmod u+x Zenml_Create_New_Stack_001.sh
```



To run the script
```shell
## Way 01
./hello_world.sh

## Way 02
bash hello_world.sh.
```