# -*- coding: utf-8 -*-

from traceback import format_tb
from contextlib import contextmanager

import requests
import json

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import DBAPIError

from WatchingList import Base, WatchingList


class Regist:
    @contextmanager
    def sessionmanager(self, Session):
        session = Session()
        try:
            yield session
            session.commit()
        except DBAPIError as e:
            print("ErrorMessage:{0}".format(e.args))
            print(format_tb(e.__traceback__))
        finally:
            session.close()


    def regist(self, userid):
        watching = WatchingList(userid, 'http://localhost:3000/tweets/{}', 'POST', 'http://localhost:3001/twitter/{}', 'POST')
        with self.sessionmanager(self.Session) as session:
            session.add(watching)
            payload = {"baseurl" : watching.base_scraping_url }
            res = requests.post(watching.getScrapingUrl())
        
            res2 = requests.post(watching.getReadingUrl(), data=json.dumps(payload) )
        return ''
    
    def list(self):
        with self.sessionmanager(self.Session) as session:
           watchlist = session.query(WatchingList).all()
        return watchlist

    def __init__(self, conf):
        self.engine = create_engine(conf.properties['db']['Urls'], echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

