import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
# import pymysql



ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

DB_URI = os.path.join(ROOT_PATH, 'db.db')


engine = create_engine(f"sqlite:///{DB_URI}", echo=True)
# engine = create_engine("mysql+pymysql://scott:tiger@hostname/dbname?charset=utf8mb4")

Base = declarative_base()