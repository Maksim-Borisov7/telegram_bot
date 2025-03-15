import logging
import requests
import redis
from config import BOT_URL
from add_to_database import add_to_database


def respond(chat_id, text, name):
    r = redis.Redis(host='localhost', port=6379, db=0)
    try:
        r.ping()
        value = r.get('text')
        if value is not None and value.decode('utf-8') == text:
            r.flushall()
            params = {"chat_id": chat_id, "text": 'иди нахуй пидор блять заебал шлюха вонючка'}
            requests.post(BOT_URL + "sendMessage", params=params)
            logging.info("Реакция на повторное сообщение")
            return
        r.set('text', text)

    except redis.exceptions.RedisError as e:
        logging.critical(f"Ошибка: {e}")
        raise e

    params = {"chat_id": chat_id, "text": text}
    requests.post(BOT_URL + "sendMessage", params=params)
    add_to_database(name)
