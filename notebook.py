# Databricks notebook source
import sys
import os
import mlflow
from datetime import datetime

from pyspark.sql import functions as F
from pyspark.sql import types as T

import databricks_repo_sync_test
import my_model

# COMMAND ----------

databricks_repo_sync_test.plus_one(3)

# COMMAND ----------

df = spark.createDataFrame([(0,),(1,)], ("i",))
display(df)

# COMMAND ----------

plus_one_udf = F.udf(databricks_repo_sync_test.plus_one, T.IntegerType())
display(df.withColumn("j", plus_one_udf("i")))

# COMMAND ----------

code_path = [os.path.dirname(databricks_repo_sync_test.__file__), os.path.dirname(my_model.__file__)]

# COMMAND ----------

with mlflow.start_run(experiment_id="2515170193180273", run_name=datetime.now().strftime("%Y/%m/%d %H:%M:%S")) as active_run:
    print(active_run.run_info.id)
    mlflow.pyfunc.log_model(
        code_path=code_path,
        python_model=my_model.ModelA(),
        artifact_path="model_a"
    )
    mlflow.pyfunc.log_model(
        code_path=code_path,
        python_model=my_model.ModelB(),
        artifact_path="model_b"
    )

# COMMAND ----------


