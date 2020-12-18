import sentimentAnalyser as sa
import numpy as np
from pyspark.sql.functions import monotonically_increasing_id, row_number
from pyspark.sql import Window


def analyse(df, sqlContext):
    tweetList = list(df.select('tweet').toPandas()['tweet'])
    print("Success: made tweet list")

    sentiments = [sa.analyse(text) for text in tweetList]
    print("Success: tweets analysed")

    sentimentDf = sqlContext.createDataFrame([(s,) for s in sentiments], ['sentiment'])
    df = df.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    sentimentDf = sentimentDf.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    df = df.join(sentimentDf, df.row_idx == sentimentDf.row_idx).drop("row_idx")
    print("Success: analysed and joined")

    return df
