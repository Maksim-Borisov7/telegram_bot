from select_button import select_button
from postgresql import get_all_users
from config import BOT_URL
import requests


def commands(chat_id, text):
    if text == "/start":
        select_button(chat_id)
    elif text == "/all_users":
        get_all_users(chat_id)
    elif text == "/exit":
        params = {"text": "Переводчик отключен", "chat_id": chat_id}
        requests.post(BOT_URL + "sendMessage", params=params)