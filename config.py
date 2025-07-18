import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    BOT_TOKEN: str = os.getenv('BOT_TOKEN')
    BOT_URL: str = os.getenv('BOT_URL')

    HOST: str = os.getenv("HOST")
    USER: str = os.getenv("USER")
    PASSWORD: int = os.getenv("PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")
    PORT: int = os.getenv("PORT")
    PG_URL: str = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

    ECHO: bool = False

    EN_CHARS: str = 'abcdefghijklmnopqrstuvwxyz'
    API_TRANSLATED: str = "https://api.mymemory.translated.net/get?q={text}&langpair={en}|{ru}"

    REDIS_HOST: str = os.getenv("REDIS_HOST")
    REDIS_PORT: int = os.getenv("REDIS_PORT")
    REDIS_DB: int = os.getenv("REDIS_DB")


settings = Settings()
