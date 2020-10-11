from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

db = create_engine(Config.DB_URL, echo=True)
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()