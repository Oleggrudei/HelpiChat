from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from fastapi import Depends
from typing import Annotated
from config import HOST, USER, PASSWORD, DB_NAME

DB_URL = f"postgresql+psycopg://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"

engine = create_engine(
    url=DB_URL,
    echo=True
)

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


# def get_db():
#     db = session_factory()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# db_dependency = Annotated[Session, Depends(get_db())]


