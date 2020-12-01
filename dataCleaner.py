import pandas as pd


donald_trump = pd.read_csv('./data/hashtag_donaldtrump.csv', lineterminator='\n')
donald_trump.loc[:,'who'] = 'donald Trump'
joe_biden = pd.read_csv('./data/hashtag_joebiden.csv', lineterminator='\n')
joe_biden.loc[:,'who'] = 'joe Biden'
data = pd.concat([joe_biden, donald_trump])

# languages = [detect_language(val) for val in tweets.tweet]
# text = tweets.loc[np.array(languages) == 'english']

