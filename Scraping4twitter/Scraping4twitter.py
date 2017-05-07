from twitter import Twitter, Tweet, Base

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')

from LogicBase import LogicBase

import tweepy

class Scraping4twitter(LogicBase):

    def get_tweets(self, twitter_id):
        with self.sessionmanager(self.Session) as session:
            result = []
            resultset = session.query(Twitter).filter(Twitter.twitter_id == twitter_id).first()
            if resultset :
                result = [ {'tweet_id' : rs.tweet_id, 'body' : rs.tweet_body} for rs in resultset.tweets]
        return result

    def get_tweet_one(self, twitter_id, tweet_id):
        with self.sessionmanager(self.Session) as session:
             resultset = session.query(Tweet).join(Tweet.twitter).filter(Twitter.twitter_id == twitter_id, Tweet.tweet_id == tweet_id).first()
             if resultset :
                result = [ {'tweet_id' : resultset.tweet_id, 'body' : resultset.tweet_body} ]
        return result


    def run(self,twitter_id):
        with self.sessionmanager(self.Session) as session:
            count = session.query(Twitter).filter(Twitter.twitter_id == twitter_id).count()
            tw = {}
            statuses = {}
            if count == 0 :
                tw = Twitter(twitter_id,0)
                session.add(tw)
                statuses = self.api.user_timeline(id=tw.twitter_id,count=50)
            else:
                tw = session.query(Twitter).filter(Twitter.twitter_id == twitter_id).first()
                statuses = self.api.user_timeline(id=tw.twitter_id,count=50, since_id=tw.since_id)

            for status in statuses:
                tt = Tweet(status.id , status.text)
                tt.twitter = tw
                session.add(tt)
            tw.since_id = max(ts.tweet_id for ts in tw.tweets)

    def __init__(self, conf):
        super().__init__(conf)
        Base.metadata.create_all(self.engine)

        # 各種キーをセット
        CONSUMER_KEY = conf.properties['twitter']['CONSUMER_KEY']
        CONSUMER_SECRET = conf.properties['twitter']['CONSUMER_SECRET']
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        ACCESS_TOKEN = conf.properties['twitter']['ACCESS_TOKEN']
        ACCESS_SECRET = conf.properties['twitter']['ACCESS_SECRET']
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        #APIインスタンスを作成
        self.api = tweepy.API(auth)

