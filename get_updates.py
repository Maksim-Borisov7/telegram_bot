import requests

from config import BOT_URL


def get_updates(offset):
    params = {"offset": offset}
    response = requests.get(BOT_URL + "getUpdates", params=params)
    return response.json()
