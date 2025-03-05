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
en_chars = 'abcdefghijklmnopqrstuvwxyz'
API_TRANSLATED = "https://api.mymemory.translated.net/get?q={text}&langpair={en}|{ru}"
