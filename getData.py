#!/usr/bin/env python
import tweepy
import yaml


class GetTweets(object):
    """
    """
    def __init__(self):
        """
        Instantiating a FindTweets object ingests access tokens from
        Twitter via a 'config.yml' file.

        These are passed to a tweepy.OAuthHandler object which is then
        used to create an api endpoint.
        """
        cfg = yaml.safe_load(open('config.yaml', 'r'))
        consumer_key = cfg['twitter']['ckey']
        consumer_secret = cfg['twitter']['csecret']
        access_token = cfg['twitter']['token']
        access_token_secret = cfg['twitter']['tokensecret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def findTweets(self, handle, tcount=200):
        """
        This method returns the specified number of tweets from the
        specified user's handle as a string. Default settings will return
        3240 tweets, which is the maximum Twitter allows.
        """
        all_tweets = []
        new_tweets = self.api.user_timeline(
            screen_name=handle, count=tcount, tweet_mode='extended')
        all_tweets.extend(new_tweets)
        oldest_id = all_tweets[-1].id - 1

        while len(new_tweets) > 0:
            new_tweets = self.api.user_timeline(
                screen_name=handle,
                count=tcount,
                tweet_mode='extended',
                max_id=oldest_id
            )
            all_tweets.extend(new_tweets)
            oldest_id = all_tweets[-1].id - 1

        tweet_text = " ".join(tweet.full_text for tweet in all_tweets)
        return tweet_text
