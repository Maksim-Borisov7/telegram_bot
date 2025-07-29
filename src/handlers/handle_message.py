import logging
import aiohttp

from config import settings
from database.sql.postgresql_handler import add_message_to_database
from database.nosql.redis_handler import redis_handler
from src.handlers.send_message import Dispatch


async def get_updates(offset):
    params = {"offset": offset}
    async with aiohttp.ClientSession() as session:
        async with session.get(settings.BOT_URL + "getUpdates", params=params) as response:
            return await response.json()


async def respond(chat_id, text, name):
    if not await redis_handler(chat_id, text):
        logging.info("Отправленное сообщение не повторяется")

        params = {"chat_id": chat_id, "text": text}
        await Dispatch.send_message_get(**params)
        await add_message_to_database(name)




