import requests

from config import botURL


def get_updates(offset):
    params = {"offset": offset}
    response = requests.get(botURL + "getUpdates", params=params)
    return response.json()
