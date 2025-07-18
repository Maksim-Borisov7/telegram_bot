import logging

import aiohttp
import requests

from config import settings
from database.sql.postgresql_handler import add_message_to_database
from database.nosql.redis_handler import redis_handler


async def get_updates(offset):
    params = {"offset": offset}
    async with aiohttp.ClientSession() as session:
        async with session.get(settings.BOT_URL + "getUpdates", params=params) as response:
            return await response.json()


async def respond(chat_id, text, name):
    if not await redis_handler(chat_id, text):
        logging.info("Отправленное сообщение не повторяется")

        params = {"chat_id": chat_id, "text": text}
        async with aiohttp.ClientSession() as session:
            async with session.post(settings.BOT_URL + "sendMessage", params=params) as response:
                await response.json()

        await add_message_to_database(name)




