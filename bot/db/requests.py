import asyncio

from sqlalchemy import select, insert, update, delete

from bot.db.database import async_session
from bot.db.models import User


async def insert_user(user_id: int, username: str, fullname: str) -> None:
    async with async_session() as session:
        resp = await session.execute(select(User.user_id).filter_by(user_id=user_id))
        resp = resp.scalar()
        if resp is None:
            user = User(user_id=user_id, username=username, user_fullname=fullname)
            session.add(user)
            await session.commit()
        else:
            await update_username(user_id=user_id, username=username)


async def count_users() -> int:
    async with async_session() as session:
        response = await session.execute(select(User.username))
        count = len(response.scalars().all())
        return count


async def update_username(user_id: int, username: str) -> None:
    async with async_session() as session:
        resp = await session.execute(select(User.username).filter_by(user_id=user_id))
        resp = resp.scalar()
        if resp != username:
            await session.execute(update(User).filter_by(user_id=user_id).values(username=username))
            await session.commit()
        else:
            return

# asyncio.run(insert_user(user_id=1234, username='2345tgvcd', fullname='23455ujbv'))
