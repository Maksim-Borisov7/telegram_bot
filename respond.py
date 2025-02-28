import requests

from config import botURL
def respond(chat_id, text):
    params = {"chat_id": chat_id, "text": text}
    requests.post(botURL + "sendMessage", params=params)
