__author__ = 'Steve Fines'

# Chapter One in Mining the Social Web is all about Twitter
import twitter
import json
import configparser


# Twitter's OAuth stuff
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''


def get_authenticated_twitter():
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    return twitter.Twitter(auth=auth)


def get_trends_for_region(twitter_api, region_id=1):
    raw_responses = twitter_api.trends.place(_id=region_id)
    responses = raw_responses[0]['trends']
    results = []
    for response in responses:
        try:
            results.append((response.get('url'), response.get('query'), response.get('name'), response.get('promoted_content')))
        except KeyError as ke:
            print("Couldn't read: "+ke.args[0])
            pass
    return results


def get_trend_names(trends):
    trendset = []
    for trend in trends:
        trendset.append(trend[2])
        print(trend[2])
    return trendset


def parse_config(config_file):
    parser = configparser.ConfigParser()
    parser.read(config_file)
    return (parser['twitter']['consumer_key'],
     parser['twitter']['consumer_secret'],
     parser['twitter']['oauth_token'],
     parser['twitter']['oauth_token_secret'])

config = parse_config('mds.ini')

CONSUMER_KEY = config[0]
CONSUMER_SECRET = config[1]
OAUTH_TOKEN = config[2]
OAUTH_TOKEN_SECRET = config[3]

twitter = get_authenticated_twitter()
trends = get_trends_for_region(twitter)
get_trend_names(trends)


