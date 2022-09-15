# Databricks notebook source

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

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

# COMMAND ----------

b = spark.sparkContext.broadcast(plus_one)

@F.udf(returnType=T.IntegerType())
def plus_one_broadcast_udf(a):
    return b.value(a)

df.withColumn("j", plus_one_broadcast_udf("i")).show()

# COMMAND ----------

def plus_one_alt(a):
    return a + 1

plus_one_alt_udf = F.udf(plus_one_alt, T.IntegerType())
df.withColumn("j", plus_one_alt_udf("i")).show()

