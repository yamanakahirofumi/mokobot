# -*- coding: utf-8 -*-

import requests
import json

from Read import Base, Category, Article

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')
from LogicBase import LogicBase

class Alread2y(LogicBase):
    def get(self,cat,name):
        with self.sessionmanager(self.Session) as session:
            arts = session.query(Article).join(Article.category).filter(Article.read_count == 0, Category.category == cat, Category.name == name).all()
            resultset = [ art.ref_id for art in arts ]
        return resultset

    def update(self, cat, name):
        with self.sessionmanager(self.Session) as session:
            cat = session.query(Category).filter(Category.category == cat, Category.name == name).first()
            if cat:
                res = requests.get(cat.getUrl())
                arts = [ d['tweet_id']  for d in json.loads(res.text)]
                sources = [ s.ref_id for s in cat.articles]
                for art in arts :
                    if art not in sources :
                        cat.articles.append(Article(art))

    def regist(self, cat, name, baseurl):
        with self.sessionmanager(self.Session) as session:
            result = session.query(Category).filter(Category.category == cat, Category.name == name).first()
            if not result :
                cat = Category(cat, name, baseurl)
                session.add(cat)
        self.update(cat, name)
        return

    def read(self, cat, name, ref_id):
        with self.sessionmanager(self.Session) as session:
            art = session.query(Article).join(Article.category).filter(Article.ref_id == ref_id, Category.category == cat, Category.name == name).first()
            art.read_count += 1

    def run(self):
        pass
        # cat = Category('twitter', 'jenkinsci', '')

    def __init__(self, conf):
        super().__init__(conf)
        Base.metadata.create_all(self.engine)

