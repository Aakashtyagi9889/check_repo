# Create a streaming table 
import dlt
from pyspark.sql.functions import *
#  currently my source is delta table ==> sales.enr

@dlt.table(
    name =  'sales_stg'
) 

def sales_stg():
    df = spark.readStream.option("skipChangeCommit", True )\
        .table("databricksansh.silver.sales_enr")
    return df   

#  Create Materalized View 

@dlt.table(
    name =  "sales_enr"
)

def sales_trn():
    df = spark.read.table("sales_stg") # yaha par isne ek schema bnaya usme imagine karlia ki table usi mai hai islie pura path nahi dia databricks.ansh.sales_enr
    df = df.withColumn("priceAfterDiscount", col("total_amount")-col("discount"))
    return df
# DBTITLE 1,Create a streaming table")

# CREATE MAT VIEW
@dlt.table(
    name = "sales_cur"
)

def sales_cur():
    df = spark.read.table("sales_enr")
    return df

