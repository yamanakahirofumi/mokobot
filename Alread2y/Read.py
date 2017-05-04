from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = "category_read"
    id = Column(Integer, primary_key=True)
    category = Column(String) # twitter or blog
    name = Column(String) # @xxxx
    base_url = Column(String)

    def __init__(self, category, name, base_url):
        self.category = category
        self.name = name
        self.base_url = base_url #http://loacalhost:3001/tweets/{}

    def __repr__(self):
        return "<Category(read)('{}', '{}', '{}')>".format(self.category, self.name, self.base_url)

    def getUrl(self):
        url = self.base_url.format(self.name)
        return url

class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True)
    ref_id =  Column(String)
    read_count = Column(Integer)

    category_id = Column(Integer, ForeignKey('category_read.id'))
    category = relationship('Category', backref='articles')

    def __init__(self, ref_id):
        self.ref_id = ref_id
        self.read_count = 0

    def __repr__(self):
        return "<article('{}', '{}')>".format(self.ref_id, self.read_count)





