from get_start import get_start
from respond import respond
from get_updates import get_updates


def main():
    offset = 0
    while True:
        updates = get_updates(offset)
        if "result" in updates:
            for update in updates["result"]:
                offset = update["update_id"] + 1
                if "message" in update and "chat" in update["message"] and "text" in update["message"]:
                    chat_id = update["message"]["chat"]["id"]
                    text = update["message"]["text"]
                    if text == "/start":
                        get_start(chat_id)
                        continue
                    respond(chat_id, text)


if __name__ == "__main__":
    main()
