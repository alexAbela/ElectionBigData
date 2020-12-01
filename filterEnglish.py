import languageDetect as sc
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

    languages = [sc.detect_language(text) for text in tweetList]

    print("Success: languages detected")

    languageDf = sqlContext.createDataFrame([(l,) for l in languages], ['languages'])
    df = df.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    languageDf = languageDf.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    df = df.join(languageDf, df.row_idx == languageDf.row_idx).drop("row_idx")
    df = df.filter(df.languages == 'english').drop("languages")
    print("Success: filtered languages")

    return df
