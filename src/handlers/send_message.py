import logging
import aiohttp
from config import settings


class Dispatch:
    @staticmethod
    async def send_message_get(**params):
        logging.info('Выполнен GET запрос')
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(settings.BOT_URL + "sendMessage", params=params) as response:
                    await response.json()
        except Exception as e:
            logging.info(f"Ошибка в Dispatch: {e}")

    @staticmethod
    async def send_message_post(**params):
        logging.info('Выполнен POST запрос')
        try:
            async with aiohttp.ClientSession() as s:
                async with s.post(settings.BOT_URL + "sendMessage", params=params) as response:
                    await response.json()
        except Exception as e:
            logging.info(f"Ошибка в Dispatch: {e}")

