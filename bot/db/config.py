import os

from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent

load_dotenv()


class BotSettings(BaseModel):
    token: str = os.getenv('BOT_TOKEN')
    admin_list: list[int] = [int(admin) for admin in os.getenv('ADMIN_LIST_ID').split(',')]
    language: str = os.getenv('LANGUAGE')
    throttling: int = int(os.getenv('THROTTLING'))


class BbSettings(BaseModel):
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/database.db"
    echo: bool = False


class Settings(BaseSettings):
    bot: BotSettings = BotSettings()
    bd: BbSettings = BbSettings()


settings = Settings()
