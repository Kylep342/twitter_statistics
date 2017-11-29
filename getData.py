import tweepy
import yaml


class FindTweets(object):
    """
    """
    def __init__(self):
        """
        Instantiating a FindTweets object ingests access tokens from
        Twitter via a 'config.yml' file.

        These are passed to a tweepy.OAuthHandler object which is then
        used to create an api endpoint.
        """
        cfg = yaml.load(open('config.yaml', 'r'))
        consumer_key = cfg['twitter']['ckey']
        consumer_secret = cfg['twitter']['csecret']
        access_token = cfg['twitter']['token']
        access_token_secret = cfg['twitter']['tokensecret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def getTweets(self, handle, tcount=100):
        """
        This method returns the specified number of tweets from the
        specified user's handle as a string.
        """
        tweets = self.api.user_timeline(
            screen_name=handle, count=tcount, tweet_mode='extended')
        tweet_text = " ".join(tweet.full_text for tweet in tweets)
        return tweet_text
