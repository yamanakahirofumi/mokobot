from bs4 import BeautifulSoup
import requests

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')
from LogicBase import LogicBase

Base = declarative_base()

class Scraping4blog(LogicBase):
    def run(self):
        # blog URL
        url = 'http://techblog.netflix.com/feeds/posts/default'
        res = requests.get(url)

        soup = BeautifulSoup(res.text, "html.parser")
        titlelist = soup.select('feed entry')

        with self.sessionmanager(self.Session) as session:
            for entry in titlelist:
                body = BeautifulSoup(entry.content.string, "html.parser")
                obj = Blog(entry.id.string, entry.title.string, body.get_text())
                session.add(obj)
            session.commit()
            for row in session.query(Blog).all():
                print(row)
                print(len(row.original_body))

    def __init__(self, conf):
        super().__init__(conf)
        Base.metadata.create_all(self.engine)


class Blog(Base):
    __tablename__ = "blog_detail"
    id = Column(Integer, primary_key=True)
    blog_id = Column(String)
    title = Column(String)
    original_body = Column(Text)

    def __init__(self, blog_id, title, body):
        self.blog_id = blog_id
        self.title = title
        self.original_body = body

    def __repr__(self):
        return "<Blog('%s', '%s', '%s')>" % (self.blog_id, self.title, self.original_body)
