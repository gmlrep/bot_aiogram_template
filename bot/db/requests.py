import asyncio

from sqlalchemy import Integer, Column, String, BigInteger, ForeignKey, select, insert, or_, update, bindparam, \
    delete, func, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.db.models import AbstractModel, User
from bot.db.config import settings

# async_engine = create_engine("sqlite+aiosqlite:///:memory:", echo=True)
async_engine = create_async_engine(settings.db_url, echo=settings.echo)

async_session = async_sessionmaker(async_engine, expire_on_commit=True)


async def insert_user(user_id, username, fullname):
    # async with async_engine.begin() as conn:
    #     await conn.run_sync(AbstractModel.metadata.create_all)
    async with async_session() as session:
        resp = await session.execute(select(User.user_id).where(User.user_id == user_id))
        resp = resp.scalar()
        if resp is None:
            user = User(user_id=user_id, username=username, fullname=fullname)
            session.add(user)
            await session.commit()
        else:
            await update_username(user_id=user_id, username=username)


async def count_users():
    async with async_session() as session:
        response = await session.execute(select(User.username))
        count = len(response.scalars().all())
        return count


async def update_username(user_id, username):
    async with async_session() as session:
        resp = await session.execute(select(User.username).where(User.user_id == user_id))
        resp = resp.scalar()
        if resp != username:
            await session.execute(update(User).where(User.user_id == user_id).values(username=username))
            await session.commit()
        else:
            return


# asyncio.run(insert_user(user_id=1234, username='2345tgvcd', fullname='23455ujbv'))