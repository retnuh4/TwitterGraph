import json
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def main():
    twit_path = Path("C:/Users/userName/Folder/With/folder.txt")
    topen = twit_path

    twit_data = []
    twit_f = open(topen, 'r')

    for line in twit_f:
        try:
            tweet = json.loads(line)
            twit_data.append(tweet)

        except:
            continue

    print(len(twit_data))

    tweets = pd.DataFrame()
    tweets['text'] = (map(lambda tweet: tweet['text'], twit_data))

    tweets_count = tweets['text'].value_counts()

    fig, ax = plt.subplots()

    ax.tick_params(axis='x', labelsize=0)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('HUDL', fontsize=10)
    ax.set_ylabel('Number Of Tweets', fontsize=10)
    ax.set_title('Tweets With Hudl Highlights', fontsize=15, fontweight='bold')
    tweets_count[:1].plot(ax=ax, kind='bar', color='orange')
    plt.show('tweets_count')


if __name__ == '__main__':
    main()
