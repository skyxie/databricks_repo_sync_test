# databricks_repo_sync_test
This repo exists to test repo syncing with Databricks

## MLFlow Project

To test an MLFlow Project

1. Update `cluster.json` and change `$DATABRICKS_ROLE`
2. Create experiment
3. Run

    MLFLOW_TRACKING_URI=databricks  mlflow run $PWD --backend-config cluster.json --backend databricks --experiment-id $EXPERIMENT_ID
