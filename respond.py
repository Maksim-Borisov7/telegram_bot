import requests

from config import BOT_URL
from add_database import add_database


def respond(chat_id, text, name):
    params = {"chat_id": chat_id, "text": text}
    requests.post(BOT_URL + "sendMessage", params=params)
    add_database(name)
