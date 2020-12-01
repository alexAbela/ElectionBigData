import sys
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, DateType
spark = SparkSession.builder.appName("DT").getOrCreate()

schema = StructType([
    StructField("created_at", DateType(), True), # 2020-10-15 00:00:01
    StructField("tweet_id", StringType(), True), # 1.31652922155725E+018
    StructField("tweet", StringType(), True), #tweet body
    StructField("likes", FloatType(), True), # like count
    StructField("retweet_count", FloatType(), True), # retweet count
    StructField("source", StringType(), True), # twitter source
    StructField("user_id", StringType(), True),
    StructField("user_name", StringType(), True),
    StructField("user_screen_name", StringType(), True),
    StructField("user_description", StringType(), True),
    StructField("user_join_date", DateType(), True), \
    StructField("user_followers_count", IntegerType(), True),
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

dtTweets = spark.read.option("header", "true").schema(schema).option("multiline", True).option("quote", "\"").option("escape", "\"").csv("./data/hashtag_donaldtrump.csv")
#dtTweets = spark.read.schema(schema).option("multiline", True).option("quote", "\"").option("escape", "\"").csv("../Project/trump_snippet.csv")

dtTweets.printSchema()



dtTweets.select("tweet","likes", "retweet_count").show(10)

spark.stop()

#userIDs = dtTweets.select("created_at", "tweet_id", "tweet", "likes")
#userIDs.show()
#print(dtTweets.count())
#dtTweets.select("user_id","user_join_date", "user_name", "tweet", "created_at", "state_code", "collected_at").show(1000)
#dtTweets.show()
