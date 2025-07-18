import logging
import aiohttp
import aioredis
from config import settings
from database.sql.postgresql_handler import logger


r = aioredis.from_url(
    f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}",
    decode_responses=True
)


async def redis_handler(chat_id, text):
    try:
        value = await r.get('text')
        if value is not None and value == text:
            params = {"chat_id": chat_id, "text": 'Вы повторили сообщение'}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(settings.BOT_URL + "sendMessage", params=params):
                        logging.info("Реакция на повторное сообщение")
                        await r.flushall()
                        return True

            except Exception as e:
                logger.error(f"Ошибка в redis_handler {e}")

        await r.set('text', text)
        return False

    except aioredis.RedisError as e:
        logging.error(f"Ошибка Redis: {e}")
        return False

    finally:
        await r.close()
