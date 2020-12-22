from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, DateType
import random

"""
Script that initiates a .csv file as a pyspark dataframe. 
We have added a method to save a new csv and a method to create a 10% subset of a larger csv file.  
"""

spark = SparkSession.builder.appName("splitter").master("local[*]").getOrCreate()

schema = StructType([
    StructField("created_at", DateType(), True),  # 2020-10-15 00:00:01
    StructField("tweet_id", StringType(), True),  # 1.31652922155725E+018
    StructField("tweet", StringType(), True),  # tweet body
    StructField("likes", FloatType(), True),  # like count
    StructField("retweet_count", FloatType(), True),  # retweet count
    StructField("source", StringType(), True),  # twitter source
    StructField("user_id", StringType(), True),
    StructField("user_name", StringType(), True),
    StructField("user_screen_name", StringType(), True),
    StructField("user_description", StringType(), True),
    StructField("user_join_date", DateType(), True), \
    StructField("user_followers_count", FloatType(), True),
    StructField("user_location", StringType(), True),
    StructField("lat", FloatType(), True),
    StructField("long", FloatType(), True),
    StructField("city", StringType(), True),
    StructField("country", StringType(), True),
    StructField("continent", StringType(), True),
    StructField("state", StringType(), True),
    StructField("state_code", StringType(), True),
    StructField("collected_at", DateType(), True)
])

def load(csvName):
    tweets = spark.read.schema(schema).option("multiline", True).option("quote", "\"").option("escape", "\"").csv('./data/' + csvName + '.csv')
    return tweets

def randomSplit(csvName):
    tweets = load(csvName)
    (bigSet, smallSet) = tweets.randomSplit([.90,.10], seed = random.seed())
    return smallSet

def createCSV(df, name):
    df.coalesce(1).write.csv('./data/' + name + '.csv')
    print('Wrote to .csv with name ' + name)