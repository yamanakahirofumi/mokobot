# -*- coding: utf-8 -*-

from traceback import format_tb
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.exc import DBAPIError

class LogicBase:
    @staticmethod
    @contextmanager
    def sessionmanager(Session):
        session = Session()
        try:
            yield session
            session.commit()
        except DBAPIError as e:
            print("ErrorMessage:{0}".format(e.args))
            print(format_tb(e.__traceback__))
        finally:
            session.close()

    def __init__(self, conf):
        self.engine = create_engine(conf.properties['db']['Urls'], echo=True)
        self.Session = sessionmaker(bind=self.engine)

