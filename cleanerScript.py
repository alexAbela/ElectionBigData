import tweetCleaner as tc

def clean(df)

    tweetList = list(df.select('tweet').toPandas()['tweet'])

    cleanTweets = [tc.tweet_cleaner_updated(text) for text in tweetList]

    languageDf = sqlContext.createDataFrame([(l,) for l in languages], ['languages'])
    df = df.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    languageDf = languageDf.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    df = df.join(languageDf, df.row_idx == languageDf.row_idx).drop("row_idx")
    df = df.filter(df.languages == 'english').drop("languages")

