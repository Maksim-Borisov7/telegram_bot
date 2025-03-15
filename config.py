import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_URL = os.getenv('BOT_URL')

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DB_NAME = os.getenv("DB_NAME")
PORT = os.getenv("PORT")
PG_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

EN_CHARS = 'abcdefghijklmnopqrstuvwxyz'
API_TRANSLATED = "https://api.mymemory.translated.net/get?q={text}&langpair={en}|{ru}"

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DB = os.getenv("REDIS_DB")

