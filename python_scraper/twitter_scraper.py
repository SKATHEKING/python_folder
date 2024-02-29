

# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
from tabulate import tabulate


# Creating list to append tweet data
tweets_list1 = []
usuario = str(input('Qual usuário você quer pegar?'))
tweets = int(input('Quantos tweets vc quer buscar?'))

def vamo_pegar_tudo(usuario,tweets):
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{usuario}').get_items()):  # declare a username
        if i > tweets:  # number of tweets you want to scrape
            break
        tweets_list1.append(
            [tweet.date, tweet.id, tweet.content, tweet.user.username])  # declare the attributes to be returned

        for i in tweets_list1:
            print(i)

vamo_pegar_tudo(usuario,tweets)
# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])


print(tabulate(tweets_df1, headers='keys', tablefmt='psql'))




