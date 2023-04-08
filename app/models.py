from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

''' Объявление базы данных. '''
Base = declarative_base()


''' Модель таблицы постов. '''
class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    post_number = Column(Integer)  # Порядковый номер поста.
    post = Column(Text)  # Сожержание поста.
