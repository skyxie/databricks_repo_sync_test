import mlflow
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
from databricks_repo_sync_test import plus_one


class ModelA(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        pass
    
    def predict(self, context, model_input):
        plus_one_udf = udf(plus_one, IntegerType())
        return model_input.withColumn("j", plus_one_udf("i")).show()


class ModelB(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        pass
    
    def predict(self, context, model_input):
        def plus_two(a):
            return a + 2
        plus_two_udf = udf(plus_two, IntegerType())
        return model_input.withColumn("j", plus_two_udf("i")).show()