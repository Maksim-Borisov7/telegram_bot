from database.sql.postgresql_handler import get_all_users
from config import BOT_URL
import requests


def commands(chat_id, text):
    if text == "/start":
        select_button(chat_id)
    elif text == "/all_users":
        get_all_users(chat_id)


def select_button(chat_id):
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
    requests.post(BOT_URL + "sendMessage", json=params)
