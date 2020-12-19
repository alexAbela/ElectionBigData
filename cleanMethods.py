import languageDetect as ld
import tweetCleaner as tc
import numpy as np
from pyspark.sql.functions import monotonically_increasing_id, row_number
from pyspark.sql import Window


def filterEnglish(df, sqlContext):

    before = df.count()
    df = df.dropna(subset=['tweet'])
    after = df.count()
    df = df.filter(df.country == 'United States of America')
    print("Success: removed " + str(before-after) + " null tweets and filtered USA")

    tweetList = list(df.select('tweet').toPandas()['tweet'])

    print("Success: made tweet list")

    languages = [ld.detect_language(text) for text in tweetList]

    print("Success: languages detected")

    languageDf = sqlContext.createDataFrame([(l,) for l in languages], ['languages'])
    df = df.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    languageDf = languageDf.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    df = df.join(languageDf, df.row_idx == languageDf.row_idx).drop("row_idx")
    df = df.filter(df.languages == 'english').drop("languages")
    print("Success: filtered languages")

    return df


def clean(df, sqlContext):
    tweetList = list(df.select('tweet').toPandas()['tweet'])
    print("Success: made tweet list")

    cleanTweets = [tc.tweet_cleaner(text) for text in tweetList]
    print("Success: tweets cleaned")

    cleanTweetDf = sqlContext.createDataFrame([(t,) for t in cleanTweets], ['tweet'])
    df = df.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    cleanTweetDf = cleanTweetDf.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    df = df.drop("tweet")
    df = df.join(cleanTweetDf, df.row_idx == cleanTweetDf.row_idx).drop("row_idx")
    print("Success: cleaned and joined")

    return df




