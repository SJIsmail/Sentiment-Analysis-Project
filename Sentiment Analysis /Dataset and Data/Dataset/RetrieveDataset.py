# General:
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

# Consume:
CONSUMER_KEY    = 'hVQOCr5yLe9blV4cUWOGBd43F'
CONSUMER_SECRET = 'US9tNtdrlfVwtmzwCC9vKHvKeA3Y182HfYtPXCZZ5J90DRJnxD'

# Access:
ACCESS_TOKEN  = '842319468176982016-8NVdVJ0CsNabb1n44VdNdNd7q10WCLb'
ACCESS_SECRET = 'lPfqDPL0yV1WNhUZHhOwtFcrBRQz34gI2TvQGXKEWvxPa'


# We import our access keys:

def twitter_setup():
    """
        Utility function to setup the Twitter's API
        with our access keys provided.
        """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    
    # Return API with authentication:
    api = tweepy.API(auth)
    return api

# We create an extractor object:
extractor = twitter_setup()
txtfile = open('txtfile2.txt','w+')
for tweet in tweepy.Cursor(extractor.search,q='"#yegtraffic" OR "traffic"  -filter:retweets',rpp=100,include_entities=True,lang="en",geocode="53.631611,-113.323975,30km",tweet_mode='extended' ).items(400):
    txtfile.write(tweet.full_text+"\n")
txtfile.close()
























"""
with open('txtfile.txt','r') as data:
    count = 0
    datalines = (line.rstrip('\r\n') for line in data)
    for line in datalines:
        print("{}".format(count)+"\n")
        print (line)
"""


# We create a tweet list as follows:
"""tweets = extractor.user_timeline(screen_name="realDonaldTrump", count=200, tweet_mode="extended")
print("Number of tweets extracted: {}.\n".format(len(tweets)))

# We print the most recent 5 tweets:
print("5 recent tweets:\n")
for tweet in tweets[:5]:
    print(tweet.full_text)
    print()

# We print info from the first tweet:
print(tweets[0].id)
print(tweets[0].created_at)
print(tweets[0].source)
print(tweets[0].favorite_count)
print(tweets[0].retweet_count)
print(tweets[0].geo)
print(tweets[0].coordinates)
print(tweets[0].entities)
"""
