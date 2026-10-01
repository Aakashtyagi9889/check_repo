import dlt
from pyspark.sql.functions import *


# STREAMING VIEW = > this view will be the source of my stremaing table
@dlt.view(
    name =  "sales_silver_view"
)

def sales_silver_view():
    df_sales = spark.readStream.table("sales_bronze")
    df_sales = df_sales.withColumn("pricePerSale",round(col("total_amount")/col("quantity"),2))
    df_sales = df_sales.withColumn("processDate" , current_timestamp())
    return df_sales

# SALES SILVER TABLE (WITH UPSERT )
# 1. Create empty table 

dlt.create_streaming_table(name = "sales_silver")

dlt.create_auto_cdc_flow(
    target = "sales_silver",
    source = "sales_silver_view",
    keys = ["sales_id"],
    sequence_by = col("processDate"),
    stored_as_scd_type = 1
)






