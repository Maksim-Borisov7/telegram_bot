from select_button import select_button
from respond import respond
from get_updates import get_updates
from add_database import add_database
from get_translated import get_translated


def main():
    offset = 0
    while True:
        updates_message = get_updates(offset)
        if "result" not in updates_message:
            continue
        for message in updates_message["result"]:
            offset = message["update_id"] + 1
            if 'callback_query' in message:
                chat_id = message['callback_query']["message"]["chat"]["id"]
                offset = get_translated(offset, chat_id)
                continue
            if "message" not in message or "text" not in message["message"]:
                continue
            chat_id = message["message"]["chat"]["id"]
            text = message["message"]["text"]
            name = message["message"]["from"]["username"]
            if message["message"]["text"] == "/start":
                select_button(chat_id)
                add_database(name)
                continue

            respond(chat_id, text, name)


if __name__ == "__main__":
    main()

