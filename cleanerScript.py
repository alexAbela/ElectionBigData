import tweetCleaner as tc

def clean(df)

    tweetList = list(df.select('tweet').toPandas()['tweet'])

    cleanTweets = [tc.tweet_cleaner_updated(text) for text in tweetList]

