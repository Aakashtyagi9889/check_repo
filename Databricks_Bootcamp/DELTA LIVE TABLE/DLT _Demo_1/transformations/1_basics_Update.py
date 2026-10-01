# Create a streaming table 
from pyspark import pipelines as dp
from pyspark.sql.functions import *
#  currently my source is delta table ==> sales.enr

@dp.table(
    name =  'sales_stg'
) 

def sales_stg():
    df = spark.readStream.option("skipChangeCommit", True )\
        .table("databricksansh.silver.sales_enr")
    return df   

#  Create Materalized View 
@dp.materialized_view(
    name =  "sales_enr"
)

def sales_trn():
    df = spark.read.table("sales_stg") # yaha par isne ek schema bnaya usme imagine karlia ki table usi mai hai islie pura path nahi dia databricks.ansh.sales_enr
    df = df.withColumn("priceAfterDiscount", col("total_amount")-col("discount"))
    return df
# DBTITLE 1,Create a streaming table")

# CREATE MAT VIEW
@dp.materialized_view(
    name = "sales_cur"
)
def sales_cur():
    df = spark.read.table("sales_enr")
    return df

# Creating temporay view on the top of sales_cur
# CREATE TEMP VIEW
@dp.temporary_view(
    name = "sales_cur_view"
)
def sales_cur():
    df = spark.read.table("sales_cur")
    return df
