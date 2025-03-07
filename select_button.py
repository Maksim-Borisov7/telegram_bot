import requests

from config import BOT_URL


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



