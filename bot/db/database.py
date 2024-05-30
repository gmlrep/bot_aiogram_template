from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from bot.db.config import settings

async_engine = create_async_engine(settings.bd.db_url, echo=settings.bd.echo)

async_session = async_sessionmaker(async_engine, expire_on_commit=True)


class Base(DeclarativeBase):
    pass
