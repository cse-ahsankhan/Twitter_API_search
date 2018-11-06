import tweepy
from textblob import TextBlob

consumer_key = 'L6a4sG272ElxeNMww5Y9cLC3p'
consumer_secret = 'MNsSOHsxXo3VqXUADaJT7fWjB25u28ixmngXyCKQQiHAgyXdXM'

access_token = '267044818-NAj54WUFkILbdnMgHAwRyzoI4CJz2D5HkoMgyOFF'
access_token_secret = 'LDirrveZgaqUCYTnZKTO8LHvd7RmXoV9IRpTQWcGnumPR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('RamMandir')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)