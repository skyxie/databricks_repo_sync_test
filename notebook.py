# Databricks notebook source
import sys
from pyspark.sql import functions as F
from pyspark.sql import types as T

from databricks_repo_sync_test import plus_one

# COMMAND ----------

plus_one(3)

# COMMAND ----------

df = spark.createDataFrame([(0,),(1,)], ("i",))
df.show()

# COMMAND ----------

plus_one_udf = F.udf(plus_one, T.IntegerType())
df.withColumn("j", plus_one_udf("i")).show()
