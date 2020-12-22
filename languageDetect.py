import nltk
from nltk.corpus import stopwords
from numpy import *

"""
The script for detecting language in a text, 
inspired from: https://www.kaggle.com/gatandubuc/donald-trump-vs-joe-biden/data 
"""

# A test set
# textSamples = ["THIS IS A TEST SAMPLE", "Dette er en test tekst", "Ich heiße Harald"]


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
    if text is None:
        return "language undetectable"

    ratios = calculate_language(text)

    most_rated_language = max(ratios, key=ratios.get)

    return most_rated_language


# for text in textSamples:
#         print(detect_language(text))
#
