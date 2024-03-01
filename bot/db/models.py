import datetime

from sqlalchemy import create_engine, Integer, String, BigInteger, ForeignKey, func
from sqlalchemy.orm import Session, as_declarative, declared_attr, Mapped, mapped_column, sessionmaker


@as_declarative()
class AbstractModel:
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)

    # Называет таблицы как классы
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class User(AbstractModel):
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    fullname: Mapped[str] = mapped_column()
    start_date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


# class Address(AbstractModel):
#     email = mapped_column(String)
#     id_user = mapped_column(ForeignKey("user.id"))
