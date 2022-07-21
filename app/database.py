from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import models

# адрес бд
SQLALCHEMY_DATABASE_URL = "sqlite:///app/fws.db"

# движок, который сессия будет использовать для подключения к бд
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# объявление сессии бд
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# создание сессии бд
session = Session()

# создание базы данных с текущей сессией
models.Base.metadata.create_all(engine)
