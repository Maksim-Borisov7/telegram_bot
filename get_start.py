import requests

from config import botURL


def get_start(chat_id):
    params = {"chat_id": chat_id, "text": "Приветствую тебя дорогой друг в моем телеграм боте"}
    requests.post(botURL + "sendMessage", params=params)
