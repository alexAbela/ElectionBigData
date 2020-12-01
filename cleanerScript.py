import tweetCleaner as tc
from pyspark.sql.functions import monotonically_increasing_id, row_number
from pyspark.sql import Window

def clean(df, sqlContext):

    tweetList = list(df.select('tweet').toPandas()['tweet'])

    cleanTweets = [tc.tweet_cleaner_updated(text) for text in tweetList]

    cleanTweetDf = sqlContext.createDataFrame([(t,) for t in cleanTweets], ['tweet'])
    df = df.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    cleanTweetDf = cleanTweetDf.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    df = df.drop("tweet")
    df = df.join(cleanTweetDf, df.row_idx == cleanTweetDf.row_idx).drop("row_idx")

    return df


