import logging
import redis
import requests
from config import BOT_URL, REDIS_DB, REDIS_HOST, REDIS_PORT

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def redis_handler(chat_id, text):
    try:
        value = r.get('text')
        if value is not None and value.decode('utf-8') == text:
            params = {"chat_id": chat_id, "text": 'Вы повторили сообщение'}
            requests.post(BOT_URL + "sendMessage", params=params)
            logging.info("Реакция на повторное сообщение")

            r.flushall()
            return True
        r.set('text', text)
        return False
    except redis.exceptions.RedisError as e:
        logging.critical(f"Ошибка: {e}")
        raise e
    finally:
        r.close()
