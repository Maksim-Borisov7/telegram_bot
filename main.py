from get_start import get_start
from respond import respond
from get_updates import get_updates


def main():
    offset = 0
    while True:
        updates_message = get_updates(offset)
        if "result" not in updates_message:
            return
        for message in updates_message["result"]:
            offset = message["update_id"] + 1
            if "message" in message and "text" in message["message"]:
                chat_id = message["message"]["chat"]["id"]
                text = message["message"]["text"]
                if text == "/start":
                    get_start(chat_id)
                    continue
                respond(chat_id, text)


if __name__ == "__main__":
    main()
