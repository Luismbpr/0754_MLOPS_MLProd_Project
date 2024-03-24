# # ### Test 002 - Start
#!//bin/bash
clear
echo Showing current stacks
echo ""
zenml stack list
echo ""
echo ""
echo ""
echo Script to create a new Stack, Experiment tracker and Model deployer
echo ""
echo ""
echo Enter Name for stack, experiment-tracker and model-deployer:
read var_creation_name
echo ""

echo Create Stack, Experiment-Tracker and Model Deployer with this name: $var_creation_name
[[ "$(echo -n 'Create it [y/N]> ' >&2; read; echo $REPLY)" == [Yy]* ]] \
    && [[ "$(echo -n 'Create stack with name:' $var_creation_name '[y/N]> ' >&2; read; echo $REPLY)" == [Yy]* ]] \
        && echo zenml down \
        && echo zenml up \
        && echo "" \
        && echo zenml experiment-tracker register mlflow_tracker_$var_creation_name --flavor=mlflow \
        && echo zenml down \
        && echo zenml up \
        && echo "" \
        && echo zenml model-deployer register mlflow_$var_creation_name --flavor=mlflow \
        && echo zenml down \
        && echo zenml up \
        && echo "" \
        && echo zenml stack register mlflow_stack_$var_creation_name -a default -o default -d mlflow_$var_creation_name -e mlflow_tracker_$var_creation_name --set \
        && echo "" \
    || echo "Stack not created";
# # ### Test 002 - End


# # # ### Test 001 - Start
# #!//bin/bash
# clear
# echo Showing current stacks
# echo ""
# zenml stack list
# echo ""
# echo ""
# echo ""
# echo Script to create a new Stack, Experiment tracker and Model deployer
# echo ""
# echo ""
# echo Enter Name for stack, experiment-tracker and model-deployer:
# read var_creation_name
# echo ""

# echo Create Stack, Experiment-Tracker and Model Deployer with this name: {$var_creation_name}
# [[ "$(echo -n 'Create it [y/N]> ' >&2; read; echo $REPLY)" == [Yy]* ]] \
#     && echo $var_creation_name will be used \
#     && echo zenml down \
#     && echo zenml up \
#     && echo "" \
#     && echo zenml experiment-tracker register mlflow_tracker_$var_creation_name --flavor=mlflow \
#     && echo zenml down \
#     && echo zenml up \
#     && echo "" \
#     && echo zenml model-deployer register mlflow_$var_creation_name --flavor=mlflow \
#     && echo zenml down \
#     && echo zenml up \
#     && echo "" \
#     && echo zenml stack register mlflow_stack_$var_creation_name -a default -o default -d mlflow_$var_creation_name -e mlflow_tracker_$var_creation_name --set \
#     && echo "" \
#     || echo Stack not created \
#     || echo "" \
#     || echo "";
# # # ### Test 001 - End



# zenml experiment-tracker register mlflow_tracker_$var_creation_name --flavor=mlflow
# zenml down
# zenml up
# clear
# zenml model-deployer register mlflow_$var_creation_name --flavor=mlflow
# zenml down
# zenml up
# clear
# zenml stack register mlflow_stack_$var_creation_name -a default -o default -d mlflow_$var_creation_name -e mlflow_tracker_$var_creation_name --set
# zenml down
# zenml up
# clear
# #zenml stack set mlflow_stack_$var_creation_name
# zenml stack list



### Sources
### 1) How to prompt for yes or no in bash? [duplicate]
###1) https://stackoverflow.com/questions/29436275/how-to-prompt-for-yes-or-no-in-bash
