import tweepy
from textblob import TextBlob

consumer_key = 'Unique_COnsumer_Key'
consumer_secret = 'Unique_Secret_Key'

access_token = 'Unique_access_token'
access_token_secret = 'Unique_Secret_Token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('RamMandir')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
