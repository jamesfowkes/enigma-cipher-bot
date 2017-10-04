import tweepy
import os
import sys

CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_KEY = os.getenv("TWITTER_ACCESS_KEY")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
_auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
_api = tweepy.API(_auth)

def api():
	return _api

