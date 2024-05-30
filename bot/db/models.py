import datetime

from sqlalchemy import Integer, String, BigInteger, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from bot.db.database import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    user_fullname: Mapped[str] = mapped_column()
    create_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
