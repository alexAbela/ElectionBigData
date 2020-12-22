import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""
Script that creates the graphs. 
"""

dfSenti = pd.read_csv('data/sentiPrDay.csv')

fig, ax=plt.subplots(1, 1, figsize=(12,10), gridspec_kw={'hspace':0.05})
lineax=ax

sns.lineplot(data=dfSenti, x="date", y="biden")
sns.lineplot(x='date', y='biden', color='blue', data=dfSenti, ax=lineax, label='Biden')
sns.scatterplot(x='date', y='biden', color='blue', data=dfSenti)
sns.lineplot(x='date', y='trump', color='red', data=dfSenti, label='Trump')
sns.scatterplot(x='date', y='trump', color='red', data=dfSenti)
lineax.set_ylim([-0.3, 0.3])
lineax.set_ylabel('Sentiment per day')
lineax.set_xlabel('Date')
plt.xticks(rotation=90)
lineax.axhline(y=0, color='k', linestyle='-')
lineax.axhline(y=0.05, color='lightgrey', linestyle='-')
lineax.axhline(y=-0.05, color='lightgrey', linestyle='-')
lineax.axvline(x="2020-11-03", color='lightgrey', linestyle='-', label='Votes start being counted')
lineax.spines['right'].set_visible(False)
lineax.spines['top'].set_visible(False)

plt.savefig('sentiPrDay.png')

dfAmount = pd.read_csv('data/tweetsPrDay.csv')


fig, ax=plt.subplots(1, 1, figsize=(12,10), gridspec_kw={'hspace':0.05})
lineax=ax

sns.lineplot(data=dfSenti, x="date", y="biden")
sns.lineplot(x='date', y='biden', color='blue', data=dfAmount, ax=lineax, label='Biden')
sns.scatterplot(x='date', y='biden', color='blue', data=dfAmount)
sns.lineplot(x='date', y='trump', color='red', data=dfAmount, label='Trump')
sns.scatterplot(x='date', y='trump', color='red', data=dfAmount)
lineax.set_ylim([0, 2000])
lineax.set_ylabel('Amount of tweets per day')
lineax.set_xlabel('Date')
plt.xticks(rotation=90)
lineax.axvline(x="2020-11-03", color='lightgrey', linestyle='-', label='Votes start being counted')
lineax.axhline(y=0, color='k', linestyle='-')
lineax.axhline(y=0.05, color='lightgrey', linestyle='-')
# lineax.axes.get_xaxis().set_ticks([])
lineax.spines['right'].set_visible(False)
lineax.spines['top'].set_visible(False)
# lineax.spines['bottom'].set_visible(False)

plt.savefig('tweetsPrDay.png')
