import aiohttp

from config import settings
from src.handlers.handle_message import get_updates, respond


async def get_api_translated(url):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as response:
            data = await response.json()
    for r in data["matches"]:
        return r['translation']


async def get_translated(offset, chat_id):
    params = {"text": "Введите текст для перевода", "chat_id": chat_id}
    async with aiohttp.ClientSession() as s:
        async with s.get(settings.BOT_URL + "sendMessage", params=params) as response:
            await response.json()
    while True:
        updates_message = await get_updates(offset)
        if "result" not in updates_message:
            continue

        for message in updates_message["result"]:
            offset = message["update_id"] + 1
            try:
                if "text" not in message['message']:
                    continue
            except KeyError:
                continue

            chat_id = message["message"]["chat"]["id"]
            text = message["message"]["text"]
            name = message["message"]["from"]["username"]

            if text == '/exit':
                params = {"text": "Переводчик отключен", "chat_id": chat_id}
                async with aiohttp.ClientSession() as s:
                    async with s.get(settings.BOT_URL + "sendMessage", params=params) as response:
                        await response.json()
                return offset

            if message['message']['text'][0] == '/':
                params = {"text": "Введите текст для перевода", "chat_id": chat_id}
                async with aiohttp.ClientSession() as s:
                    async with s.get(settings.BOT_URL + "sendMessage", params=params) as response:
                        await response.json()
                continue

            if text[0].lower() in settings.EN_CHARS:
                res = await get_api_translated(settings.API_TRANSLATED.format(text=text, en="en", ru="ru"))
                await respond(chat_id, res, name)
            else:
                res = await get_api_translated(settings.API_TRANSLATED.format(text=text, en="ru", ru="en"))
                await respond(chat_id, res, name)


