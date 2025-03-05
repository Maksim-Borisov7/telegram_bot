from get_updates import get_updates
from get_api_translated import get_api_translated
from respond import respond
from get_start import get_start
from config import en_chars, API_TRANSLATED


def get_translated(offset):
    while True:
        updates_message = get_updates(offset)
        if "result" not in updates_message:
            continue
        for message in updates_message["result"]:
            en, ru = 'en', 'ru'
            offset = message["update_id"] + 1
            if 'callback_query' in message:
                return
            if "text" not in message['message']:
                continue
            chat_id = message["message"]["chat"]["id"]
            text = message['message']["text"]
            name = message["message"]["from"]["username"]
            if text == "/start":
                get_start(chat_id)
                break
            if text[0].lower() in en_chars:
                res = get_api_translated(API_TRANSLATED.format(text=text, en=en, ru=ru))
                respond(chat_id, res, name)
            else:
                en, ru = 'ru', 'en'
                res = get_api_translated(API_TRANSLATED.format(text=text, ru=ru, en=en))
                respond(chat_id, res, name)