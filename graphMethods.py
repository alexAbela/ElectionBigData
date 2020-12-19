from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, DateType
from pyspark.sql import functions as f
import datetime


def amountOfTweetsTime(df, candidate, spark, sqlContext):
    startDate = datetime.datetime(2020, 10, 15)
    schema = StructType([
        StructField("Date", DateType(), True),  # 2020-10-15 00:00:01
        StructField(candidate, FloatType(), True),  # 1.31652922155725E+018
    ])
    newdf = sqlContext.createDataFrame([], schema)
    for i in range(25):
        print(startDate)
        dfDay = df.filter(df.created_at == startDate).cache()
        amount = float(dfDay.count())
        newRow = spark.createDataFrame([(startDate, amount)], schema)
        newdf = newdf.union(newRow)
        startDate += datetime.timedelta(days=1)
    return newdf


def sentimentPerDay(df, candidate, spark, sqlContext):
    startDate = datetime.datetime(2020, 10, 15)
    schema = StructType([
        StructField("Date", DateType(), True),  # 2020-10-15 00:00:01
        StructField(candidate, FloatType(), True),  # 1.31652922155725E+018
    ])
    newdf = sqlContext.createDataFrame([], schema)
    for i in range(25):
        print(startDate)
        dfDay = df.filter(df.created_at == startDate).cache()
        daySenti = dfDay.agg({'sentiment': 'sum'}).collect()[0]
        daySentiAmount = daySenti["sum(sentiment)"]
        tweetamount = dfDay.count()
        averageSenti = daySentiAmount / tweetamount

        newRow = spark.createDataFrame([(startDate, averageSenti)], schema)
        newdf = newdf.union(newRow)
        startDate += datetime.timedelta(days=1)

        print(averageSenti)

    return newdf


