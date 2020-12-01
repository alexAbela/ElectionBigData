import nltk
from nltk.corpus import stopwords
from numpy import *


textSamples = ["Hi my name is harald and i am sexy and like dick 345y713897t34", "Harald is very gay", "Harald is very sexy", "Harald je suis gay"]


def calculate_language(text):

    languages_ratios = {}
    tokens = nltk.wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements)  # language "score"

    return languages_ratios


def detect_language(text):
    ratios = calculate_language(text)

    most_rated_language = max(ratios, key=ratios.get)

    return most_rated_language


for text in textSamples:
        print(detect_language(text))

