import mlflow
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType, StructType, StructField
from databricks_repo_sync_test import plus_one


class ModelA(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        pass
    
    def predict(self, context, model_input):
        plus_one_udf = udf(plus_one, IntegerType())
        return model_input.withColumn("j", plus_one_udf("i"))


class ModelB(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        pass
    
    def predict(self, context, model_input):
        def plus_two(a):
            return a + 2
        plus_two_udf = udf(plus_two, IntegerType())
        return model_input.withColumn("j", plus_two_udf("i"))
    
class ModelC(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        pass
    
    def predict(self, context, model_input):
        pdf = model_input.toPandas()
        pdf.loc[:, "j"] = pdf["i"].apply(plus_one)
        spark = SparkSession.builder.getOrCreate()
        return spark.createDataFrame(
            pdf,
            schema=StructType(
                [
                    StructField("i", IntegerType(), False),
                    StructField("j", IntegerType(), False)
                ]
            )
        )