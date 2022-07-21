from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

# объявление бд
Base = declarative_base()


# таблица постов
class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    post_number = Column(Integer)  # нумерация поста
    post = Column(Text)  # текст поста
