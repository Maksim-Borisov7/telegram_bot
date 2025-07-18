import aiohttp

from database.sql.postgresql_handler import get_all_users
from config import settings


async def commands(chat_id, text):
    if text == "/start":
        await select_button(chat_id)
    elif text == "/all_users":
        await get_all_users(chat_id)


async def select_button(chat_id):
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "Переводчик RUS|EN:", "callback_data": "get_translated"},
            ]
        ]
    }
    params = {"chat_id": chat_id,
              "text": "Пожалуйста, выберите кнопку ниже:",
              "reply_markup": keyboard
              }
    async with aiohttp.ClientSession() as s:
        async with s.post(settings.BOT_URL + "sendMessage", json=params) as response:
            await response.json()
