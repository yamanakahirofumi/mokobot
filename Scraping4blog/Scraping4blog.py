from bs4 import BeautifulSoup
import urllib.request as req

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Text, MetaData
from sqlalchemy.orm import mapper,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Scraping4blog:
    def run(self):
        # blog URL
        url = 'http://techblog.netflix.com/feeds/posts/default'
        res = req.urlopen(url)

        soup = BeautifulSoup(res, "html.parser")
        titlelist = soup.select('feed entry')
        sendtitle =''

        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            for entry in titlelist:
                body = BeautifulSoup(entry.content.string, "html.parser")
                obj = Blog(entry.id.string, entry.title.string, body.get_text())
                session.add(obj)
            session.commit()
            for row in session.query(Blog).all():
                print(row)
                print(len(row.original_body))
        except:
            import sys
            print(sys.exc_info())
            print("ダメぽよ")
            session.rollback
        finally:
            session.close()
 
    def __init__(self):
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)


class Blog(Base):
    __tablename__ = "blog_detail"
    id = Column(Integer, primary_key=True)
    blog_id = Column(String)
    title = Column(String)
    original_body = Column(Text)

    def __init__(self, id, title, body):
        self.blog_id = id
        self.title = title
        self.original_body = body

    def __repr__(self):
        return "<Blog('%s', '%s', '%s')>" % (self.blog_id, self.title, self.original_body)
