from nltk.sentiment.vader import SentimentIntensityAnalyzer

"""
Script that returns the sentiment of a text. This method only returns the compound score, as that is 
what is relevant for us. We would be able to retrieve the individual negative, neutral and positive scores if wished. 
"""

def analyse(text):
    if text is None:
        return float(0.0)
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(text)
    #print(ss)
    compound = ss[sorted(ss)[0]]
    return float(compound)
