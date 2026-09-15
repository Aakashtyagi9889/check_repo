import dlt 

#  CREATE AN EMPTY STREAM TABLE 

dlt.create_streaming_table(
    name = "append_table"
)

# CREATE STREAMING TABLE (FLOW -1)
@dlt.append_flow(
    target = "append_table"
)
def flow():
    df= spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format" , "csv")\
        .load("/Volumes/databricksansh/bronze/autovol/flow1/")
    return df
    

# CREATE FOR FLOW 2

@dlt.append_flow(
    target = "append_table"
)
 
def flow2():
    df = spark.readStream.format("cloudFiles")\
         .option("cloudFiles.format","csv")\
         .load("/Volumes/databricksansh/bronze/autovol/flow2/")
    return df










