from get_start import get_start
from respond import respond
from get_updates import get_updates
from add_database import add_database


def main():
    offset = 0
    while True:
        updates_message = get_updates(offset)
        if "result" not in updates_message:
            continue

        for message in updates_message["result"]:
            offset = message["update_id"] + 1

            if "message" not in message and "text" not in message["message"]:
                continue
            chat_id = message["message"]["chat"]["id"]
            text = message["message"]["text"]
            name = message["message"]["from"]["username"]
            if message["message"]["text"] == "/start":
                get_start(chat_id)
                add_database(name)
                continue
            respond(chat_id, text, name)


if __name__ == "__main__":
    main()
