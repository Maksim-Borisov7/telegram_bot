from get_updates import get_updates
from get_api_translated import get_api_translated
from respond import respond
from config import EN_CHARS, API_TRANSLATED, BOT_URL
import requests


def get_translated(offset, chat_id):
    params = {"text": "Введите текст для перевода", "chat_id": chat_id}
    requests.post(BOT_URL + "sendMessage", params=params)
    while True:
        updates_message = get_updates(offset)
        if "result" not in updates_message:
            continue
        for message in updates_message["result"]:
            offset = message["update_id"] + 1
            try:
                if "text" not in message['message']:
                    continue
            except KeyError:
                continue
            if message['message']["text"] == '/exit':
                params = {"text": "Переводчик отключен", "chat_id": message["message"]["chat"]["id"]}
                requests.post(BOT_URL + "sendMessage", params=params)
                return offset
            if message['message']["text"][0] == '/':
                params = {"text": 'Введите текст для перевода:', "chat_id": message["message"]["chat"]["id"]}
                requests.post(BOT_URL + "sendMessage", params=params)
                continue
            en, ru = 'en', 'ru'
            chat_id = message["message"]["chat"]["id"]
            text = message['message']["text"]
            name = message["message"]["from"]["username"]
            if text[0].lower() in EN_CHARS:
                res = get_api_translated(API_TRANSLATED.format(text=text, en=en, ru=ru))
                respond(chat_id, res, name)
            else:
                en, ru = 'ru', 'en'
                res = get_api_translated(API_TRANSLATED.format(text=text, ru=ru, en=en))
                respond(chat_id, res, name)
