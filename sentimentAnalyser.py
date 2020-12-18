import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def analyse(text):
    if text is None:
        return float(0.0)
    sid = SentimentIntensityAnalyzer()
    neg = []
    neu = []
    pos = []

    ss = sid.polarity_scores(text)
    print(ss)
    neg.append(ss[sorted(ss)[1]])
    neu.append(ss[sorted(ss)[2]])
    pos.append(ss[sorted(ss)[3]])

    compound = ss[sorted(ss)[0]]
    return float(compound)