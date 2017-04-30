from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()


class Twitter(Base):
    __tablename__ = "twitter"
    id = Column(Integer, primary_key=True)
    twitter_id = Column(String)
    since_id = Column(Integer)

    def __init__(self, twitter_id, since_id):
        self.twitter_id = twitter_id
        self.since_id = since_id

    def __repr__(self):
        return "<Twitter('{}', '{}')>".format(self.twitter_id, self.since_id)


class Tweet(Base):
    __tablename__ = "tweet"
    id = Column(Integer, primary_key=True)
    tweet_id = Column(String)
    tweet_body = Column(Text)
    twitter_class_id = Column(Integer, ForeignKey('twitter.id'))
    twitter = relationship('Twitter', backref='tweets')

    def __init__(self, tweet_id, tweet_body):
        self.tweet_id = tweet_id
        self.tweet_body = tweet_body

    def __repr__(self):
        return "<Tweet('{}', '{}')>".format(self.tweet_id, self.tweet_body)



