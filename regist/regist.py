# -*- coding: utf-8 -*-

import requests

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')

from LogicBase import LogicBase

from WatchingList import Base, WatchingList, Category


class Regist(LogicBase):

    def regist(self, category, userid):
        with self.sessionmanager(self.Session) as session:
            cat = session.query(Category).filter(Category.category == category).first()
            if not cat:
                cat = Category(category)
                session.add(cat)
            watching = session.query(WatchingList).join(WatchingList.category)\
                                .filter(Category.category == category, WatchingList.name == userid).first()
            if not watching:
                watching = WatchingList(userid,
                                        'http://localhost:3000/tweets/{}',
                                        'POST',
                                        'http://localhost:3001/twitter/{}',
                                        'POST')
                watching.category = cat
                payload = {"baseurl" : watching.base_scraping_url }
                requests.post(watching.getScrapingUrl())
                requests.post(watching.getReadingUrl(),
                    json=payload)
        return ''

    def listup(self, category):
        with self.sessionmanager(self.Session) as session:
           watchlist = session.query(WatchingList).join(WatchingList.category)\
                                .filter(Category.category == category).all()
           watchlist = [ {"userid" : w.name} for w in watchlist]
        return watchlist

    def __init__(self, conf):
        super().__init__(conf)
        Base.metadata.create_all(self.engine)

