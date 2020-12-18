import csv
import initSentiment as i
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, DateType

data = i.load('dt10rated')
results = []
with open("./data/stateNames.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

def analyse(df, candidate, spark, sqlContext):
    # newdf = spark.createDataFrame([],['state', candidate])
    schema = StructType([
    StructField("state", StringType(), True),  # 2020-10-15 00:00:01
    StructField(candidate, FloatType(), True),  # 1.31652922155725E+018
    ])
    newdf = sqlContext.createDataFrame([], schema)
    df = df.select('state', 'sentiment')
    for state in results:
        print(state[0])
        dfState = df.filter(df.state == state[0])
        stateSenti = dfState.agg({'sentiment':'sum'}).collect()[0]
        newRow = spark.createDataFrame([(state[0],stateSenti["sum(sentiment)"])], schema)
        newdf = newdf.union(newRow)
        print(stateSenti)
    return newdf

    