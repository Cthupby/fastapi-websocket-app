from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import models


''' Aдрес базы данных SQLite. '''
SQLALCHEMY_DATABASE_URL = "sqlite:///app/fws.db"

'''
Движок, который сессия будет использовать для подключения к базе данных.
'''
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

''' Объявление сессии базы данных.'''
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

''' Создание сессии базы данных. '''
session = Session()

''' Создание базы данных с текущей сессией. '''
models.Base.metadata.create_all(engine)
