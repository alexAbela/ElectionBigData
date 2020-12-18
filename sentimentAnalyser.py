import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def analyse(text):
    if text is None:
        return 0
    sid = SentimentIntensityAnalyzer()
    neg = []
    neu = []
    pos = []

    ss = sid.polarity_scores(text)
    print(ss)
    neg.append(ss[sorted(ss)[1]])
    neu.append(ss[sorted(ss)[2]])
    pos.append(ss[sorted(ss)[3]])

    ##returns 1 for positive, 2 for negative, 3 for neutral

    if pos > neg:
        return 2
    if pos == neg:
        return -2
    else:
        return 0

# result = pd.DataFrame({'pos':pos,'neg':neg,'neu':neu})

    # a = (result.pos>result.neg).sum()
    # b = (result.pos<result.neg).sum()
    # c = (result.pos==result.neg).sum()



print(analyse("I like to hate Michael Bay films, but I couldn't fault this one"))

