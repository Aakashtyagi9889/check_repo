# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %md
# MAGIC # check for scd Type 2 (track chnages)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from databricksansh.gold.dim_products

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from databricksansh.gold.products_silver
# MAGIC where product_id = 29;

# COMMAND ----------

 