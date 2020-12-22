import re
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer

"""
Script that cleans text, so that i can be analysed more accurately. 
"""


tok = WordPunctTokenizer()

#Defnining variables and patterns that will be used for filtering
pattern1 = r'@[A-Za-z0-9_]+'
pattern2 = r'https?://[^ ]+'
combined_patterns = r'|'.join((pattern1, pattern2))
www_pat = r'www.[^ ]+'
#expanding negations
negations_dic = {"isn't": "is not", "aren't": "are not", "wasn't": "was not", "weren't": "were not",
                 "haven't": "have not", "hasn't": "has not", "hadn't": "had not", "won't": "will not",
                 "wouldn't": "would not", "don't": "do not", "doesn't": "does not", "didn't": "did not",
                 "can't": "can not", "couldn't": "could not", "shouldn't": "should not", "mightn't": "might not",
                 "mustn't": "must not"}
neg_pattern = re.compile(r'\b(' + '|'.join(negations_dic.keys()) + r')\b')


def tweet_cleaner(text):

    #handeing null text
    if text is None:
        return "ntnd"

    soup = BeautifulSoup(text, 'lxml')
    souped = soup.get_text()
    try:
        bom_removed = souped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        bom_removed = souped
    stripped = re.sub(combined_patterns, '', bom_removed)
    stripped = re.sub(www_pat, '', stripped)
    lower_case = stripped.lower()
    neg_handled = neg_pattern.sub(lambda x: negations_dic[x.group()], lower_case)
    letters_only = re.sub("[^a-zA-Z]", " ", neg_handled)

    #removing whitespace
    words = [x for x in tok.tokenize(letters_only) if len(x) > 1]
    return (" ".join(words)).strip()


