from respond import respond
from get_updates import get_updates
from get_translated import get_translated
from commands import commands
import logging


def handle_message(message):
    if "update_id" not in message:
        return None

    offset = message["update_id"] + 1

    if 'callback_query' in message:
        chat_id = message['callback_query']["message"]["chat"]["id"]
        get_translated(offset, chat_id)
        return offset

    if "message" not in message or "text" not in message["message"]:
        return offset

    chat_id = message["message"]["chat"]["id"]
    text = message["message"]["text"]
    name = message["message"]["from"]["username"]

    if text[0] == "/":
        commands(chat_id, text)
    else:
        respond(chat_id, text, name)

    return offset


def main():
    offset = 0
    while True:
        try:
            updates_message = get_updates(offset)
            if "result" not in updates_message:
                continue

            for message in updates_message["result"]:
                new_offset = handle_message(message)
                if new_offset:
                    offset = new_offset

        except Exception as e:
            logging.error(f"Ошибка в основном цикле: {e}")
            continue


if __name__ == "__main__":
    main()

