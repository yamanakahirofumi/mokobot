# -*- coding: utf-8 -*-

from traceback import format_tb

import requests
import json

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import DBAPIError

from Read import Base, Category, Article


class Alread2y:
    def get(self,cat,name):
        session = self.Session()
        try:
            cat = session.query(Category).filter(Category.category == cat, Category.name == name).first()
        except DBAPIError as e:
            print("ErrorMessage:{0}".format(e.args))
            print(format_tb(e.__traceback__))
        finally:
            session.close()
    
    
    def update(self, cat, name):
        session = self.Session()
        try:
            cat = session.query(Category).filter(Category.category == cat, Category.name == name).first()
            if cat:
                res = requests.get(cat.getUrl())
                arts = [ d['tweet_id']  for d in json.loads(res.text)]
                sources = [ s.ref_id for s in cat.articles]
                for art in arts :
                    if art not in sources :
                        cat.append(Article(art))
                session.commit()
        except DBAPIError as e:
            print("ErrorMessage:{0}".format(e.args))
            print(format_tb(e.__traceback__))
        finally:
            session.close()

    def regist(self, cat, name, baseurl):
        session = self.Session()
        try:
            result = session.query(Category).filter(Category.category == cat, Category.name == name).first()
            if not result :
                cat = Category(cat, name, baseurl)
                session.add(cat)
                session.commit()
        except DBAPIError as e:
            print("ErrorMessage:{0}".format(e.args))
            print(format_tb(e.__traceback__))
        finally:
            session.close()
        self.update(cat, name)
        return

    def read(self, cat, name):
        session = self.Session()
        try:
            num = session.query(func.count(Article.id)).join(Article.category).filter(Article.read_count == 0, Category.category == cat, Category.name == name).scalar()
        except DBAPIError as e:
            print("ErrorMessage:{0}".format(e.args))
            print(format_tb(e.__traceback__))
        finally:
            session.close()
        print(num)
        return num

    def run(self):
        pass
        # cat = Category('twitter', 'jenkinsci', 'http://localhost:3000/tweets')

    def __init__(self, conf):
        self.engine = create_engine(conf.properties['db']['Urls'], echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
