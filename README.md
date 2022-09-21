# databricks_repo_sync_test
This repo exists to test repo syncing with Databricks

## Setup

```bash
pip install -r requirements.txt
```

## dbx Test

Sync `databricks_repo_sync_test` to `dbfs`:

```bash
dbx sync dbfs -d /tmp/output/dir --source $PWD
```

Sync `notebook.py` to the Databricks workspace:

```bash
databricks workspace import --language python notebook.py $DEST_PATH
```

Add the synced `dbfs` path to `sys.path` in the notebook:

```python
import sys

if "/dbfs/tmp/output/dir" not in sys.path:
    sys.path.insert(0, "/dbfs/tmp/output/dir")
```

Run the notebook on an interative cluster!

## MLFlow Project

To test an MLFlow Project 

1. Update `cluster.json` and change `$DATABRICKS_ROLE`
2. Create experiment if one does not already exist
3. Copy `cluster.json` to another path (e.g. `cluster_with_secrets.json`) and set secrets
3. Run with code uploaded to dbfs

```bash
MLFLOW_TRACKING_URI=databricks  mlflow run $PWD --backend databricks \
    --backend-config cluster_with_secrets.json  \
    --experiment-id $EXPERIMENT_ID
```

4. Run with code from pypi

```bash
cd mlflow_project_with_package
MLFLOW_TRACKING_URI=databricks  mlflow run $PWD --backend databricks \
    --backend-config ../cluster_with_secrets.json  \
    --experiment-id $EXPERIMENT_ID
```
