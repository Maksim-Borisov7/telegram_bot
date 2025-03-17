import logging

from src.handlers.commands import commands
from src.handlers.get_translated import get_translated
from src.handlers.handle_message import respond, get_updates


def handler(message):
    if "update_id" not in message:
        return None

    offset = message["update_id"] + 1

    if 'callback_query' in message:
        chat_id = message['callback_query']["message"]["chat"]["id"]
        return get_translated(offset, chat_id)

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
                new_offset = handler(message)
                if new_offset:
                    offset = new_offset

        except Exception as e:
            logging.error(f"Ошибка в основном цикле: {e}")
            continue


if __name__ == "__main__":
    main()

