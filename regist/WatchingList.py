from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class WatchingList(Base):
    __tablename__ = "watchng_user"
    id = Column(Integer, primary_key=True)
    name = Column(String) # @xxxx
    base_scraping_url = Column(String)
    scraping_method = Column(String)
    base_reading_url = Column(String)
    reading_method = Column(String)

    def __init__(self, name, base_scraping_url, scraping_method, base_reading_url, reading_method):
        self.name = name
        self.base_scraping_url = base_scraping_url
        self.scraping_method = scraping_method
        self.base_reading_url = base_reading_url
        self.reading_method = reading_method

    def __repr__(self):
        return "<Category(read)('{}', '{}', '{}', '{}',  '{}')>".format(self.name, self.base_scraping_url, self.scraping_method,  self.base_reading_url, self.reading_method)

    def getScrapingUrl(self):
        url = self.base_scraping_url.format(self.name)
        return url

    def getReadingUrl(self):
        url = self.base_reading_url.format(self.name)
        return url

