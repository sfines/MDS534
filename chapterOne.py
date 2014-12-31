__author__ = 'Steve Fines'

# Chapter One in Mining the Social Web is all about Twitter
import twitter
import json

# Twitter's OAuth stuff
CONSUMER_KEY = '4JpzPefAPpLFXbzDamI0et281'
CONSUMER_SECRET = 'GKqPWT8e962QHG5AZ3oETTDJdJD4RG2mQHZ8Wq78VuEH2uidX5'
OAUTH_TOKEN = '6895552-zHZvhNWEriddyvVMxWqJTbayNQi0dk6qbrz2862wjY'
OAUTH_TOKEN_SECRET = 'AF8qAoktNPqCi0JtkS5zWVmHZZCTNLsCikIC1Fy4LnKQv'


def get_authenticated_twitter():
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    return twitter.Twitter(auth=auth)


def get_trends_for_region(twitter_api, region_id=1):
    raw_responses = twitter_api.trends.place(_id=region_id)
    responses = raw_responses[0]['trends']
    results = []
    for response in responses:
        try:
            results.append(
                (response.get('url'),
            response.get('query'),
            response.get('name'),
            response.get('promoted_content'))
            )
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


twitter = get_authenticated_twitter()
trends = get_trends_for_region(twitter)
get_trend_names(trends)


