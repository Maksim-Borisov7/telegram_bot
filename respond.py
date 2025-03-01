import requests

from config import botURL
from add_database import add_database

def respond(chat_id, text, name):
    params = {"chat_id": chat_id, "text": text}
    requests.post(botURL + "sendMessage", params=params)
    add_database(name)
