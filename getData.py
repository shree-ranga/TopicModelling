# Event Detection from Tweets
# -*- coding: utf-8 -*-

# Data collection

__author__ = 'Shree Ranga Raju'

import tweepy
import json
import pprint

def init_twitter_API():
	# Twitter API Keys and Secrets
	consumer_key = ''
	consumer_secret = ''
	access_token = ''
	access_secret = ''

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
	return api


def parse_json_data(data):
	tweet = json.loads(data)
	# pprint.pprint(tweet)
	# date = tweet['created_at']
	# tweet_id = tweet['id']
	# screen_name = tweet['user']['name']
	# Consider retweet as a tweet from the user
	if 'retweeted_status' in tweet:
		text = tweet['retweeted_status']['full_text']
	else:
		text = tweet['full_text']
	# return [date, tweet_id, screen_name, text]
	return text

# def push_tweet_to_file(text):
# 	# db_json = {}
# 	# db_json['tweet_id'] = tweet_id
# 	# db_json['screen_name'] = screen_name
# 	# db_json['tweet_text'] = text
# 	# db_json['date'] = date
# 	# DB name is MyTweetsDB and collection name is tweets

# 	print "wrote to file"

def get_data(user_name, fdata):
	# i = 0
	# Gets last 100 tweets from each user from the moment this script is run.
	for tweets in tweepy.Cursor(api.user_timeline, id = user_name, tweet_mode = 'extended').items(100):
		data = json.dumps(tweets._json)
		tweet_text = parse_json_data(data)
		# print tweet_text
		fdata.write(str(tweet_text.encode('utf8')) + "\n")


if __name__ == '__main__':

	api = init_twitter_API()
	print 'Initialized Twitter API.'

	fdata = fdata = open("data.txt", "w")

	user_names = ['nytimes', 'cnn', 'abc', 'ajenglish', 'bbcnews', 'washingtonpost', 'usatoday', 'thetimes', 'cnet', 'telegraph']
	# user_names = ['nytimes', 'cnn']

	for user_name in user_names:
		get_data(user_name, fdata)

	fdata.close()

	print "Data Collection done!"











