import logging
import requests

from config import BOT_URL
from database.sql.postgresql_handler import add_message_to_database
from database.nosql.redis_handler import redis_handler


def get_updates(offset):
    params = {"offset": offset}
    response = requests.get(BOT_URL + "getUpdates", params=params)
    return response.json()


def respond(chat_id, text, name):
    if not redis_handler(chat_id, text):
        logging.info("Отправленное сообщение не повторяется")

        params = {"chat_id": chat_id, "text": text}
        requests.post(BOT_URL + "sendMessage", params=params)

        add_message_to_database(name)




