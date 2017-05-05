# -*- coding: utf-8 -*-

from traceback import format_tb
from contextlib import contextmanager

import requests
import json

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import DBAPIError

from WatchingUser import Base, Watching


class Regist:
    @contextmanager
    def sessionmanager(self, Session):
        session = Session()
        try:
            yield session
        except DBAPIError as e:
            print("ErrorMessage:{0}".format(e.args))
            print(format_tb(e.__traceback__))
        finally:
            session.close()


    def regist(self, userid):
        watching = Watching(userid, 'http://localhost:3000/tweets/{}', 'POST', 'http://localhost:3001/twitter/{}', 'POST')
        with self.sessionmanager(self.Session) as session:
            arts = session.add(watching)
        payload = {"baseurl" : watching.base_scraping_url }
        res = requests.post(watching.getScrapingUrl())
        
        res2 = requests.post(watching.getReadingUrl(), data=json.dumps(payload) )
        return ''
    
    def list(self):
        return num

    def run(self):
        pass
        # cat = Category('twitter', 'jenkinsci', '')

    def __init__(self, conf):
        self.engine = create_engine(conf.properties['db']['Urls'], echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

