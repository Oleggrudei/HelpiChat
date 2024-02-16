from datetime import datetime

from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Chats(Base):
    __tablename__ = 'chats'
    chat_id: Mapped[int] = mapped_column(primary_key=True)
    operator_id: Mapped[str]
    client_id: Mapped[str]
    state: Mapped[str]
    open_date: Mapped[datetime]
    close_date: Mapped[datetime]


class ChatsDetails(BaseModel):
    chat_id: int
    operator_id: str
    client_id: str
    state: str
    open_date: datetime
    close_date: datetime

# class Test(BaseModel):
#     id: int
#     operator_id: str
#     client_id: str
#     state: str
