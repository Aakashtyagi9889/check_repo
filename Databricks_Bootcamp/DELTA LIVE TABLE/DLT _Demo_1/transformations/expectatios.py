import dlt
from pyspark.sql.functions import *
expectations = {
    "rule1" : "product_id IS NOT NULL",
    "rule2" : "category IS NOT NULL"
}

@dlt.table(
    name = "expect_table"
)
# @dlt.expect_all(expectations)
# @dlt.expect_all_or_fail(expectations)
@dlt.expect_all_or_drop(expectations)
# @dlt.expect_all_or_warn(expectations)
def expect_table():
    df = spark.read.table("databricksansh.silver.products_enr")
    return df