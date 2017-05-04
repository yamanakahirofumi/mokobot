from twitter import Twitter, Tweet, Base
from settings import SettingManager

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

import tweepy

class Scraping4twitter:
    
    def get_tweets(self, twitter_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        result = {}
        try:
            resultset = session.query(Twitter).filter(Twitter.twitter_id == twitter_id).first()
            if resultset : 
                result = [ {'tweet_id' : rs.tweet_id, 'body' : rs.tweet_body} for rs in resultset.tweets]
            else:
                result =[]
        except:
            import sys
            print(sys.exc_info())
        finally:
            session.close()
        return result

    def get_tweet_one(self, twitter_id, tweet_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        result = {}
        try:
            resultset = session.query(Tweet).join(Tweet.twitter).filter(Twitter.twitter_id == twitter_id, Tweet.tweet_id == tweet_id).first()
        except:
            import sys
            print(sys.exc_info())
        finally:
            session.close()
        return resultset


    def run(self,twitter_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            count = session.query(Twitter).filter(Twitter.twitter_id == twitter_id).count()
            tw = {}
            statuses = {}
            if count == 0 :
                tw = Twitter(twitter_id,0)
                session.add(tw)
                statuses = self.api.user_timeline(id=tw.twitter_id,count=20)
            else:
                tw = session.query(Twitter).filter(Twitter.twitter_id == twitter_id).first()
                statuses = self.api.user_timeline(id=tw.twitter_id,count=20, since_id=tw.since_id)

            for status in statuses:
                tt = Tweet(status.id , status.text)
                tt.twitter = tw
                session.add(tt)
            session.commit()
            tw.since_id = max(ts.tweet_id for ts in tw.tweets) 

        except:
            import sys
            print(sys.exc_info())
            session.rollback
        finally:
            session.close()
 
    def __init__(self):
        self.engine = create_engine("sqlite:///db.sqlite3")
        Base.metadata.create_all(self.engine)

        # 各種キーをセット
        settings = SettingManager()

        CONSUMER_KEY = settings.properties['twitter']['CONSUMER_KEY']
        CONSUMER_SECRET = settings.properties['twitter']['CONSUMER_SECRET']
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        ACCESS_TOKEN = settings.properties['twitter']['ACCESS_TOKEN']
        ACCESS_SECRET = settings.properties['twitter']['ACCESS_SECRET']
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        #APIインスタンスを作成
        self.api = tweepy.API(auth)


    def run_serve(self):
        api.run(host='0.0.0.0', port=3000)




