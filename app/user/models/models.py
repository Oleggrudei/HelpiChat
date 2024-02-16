from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Human(Base):
    __tablename__ = 'human'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    lastname: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    age: Mapped[int]
    is_married: Mapped[bool]
    role: Mapped[str]
    register_date: Mapped[datetime]
    tg_id: Mapped[str]


class EmailPasswordDetails(BaseModel):
    email: str
    password: str

class HumanDetails(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    password: str
    age: int
    is_married: bool
    role: str
    register_date: datetime
    tg_id: str
