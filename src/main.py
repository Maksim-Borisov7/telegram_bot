import asyncio
import logging

from src.handlers.commands import commands
from src.handlers.get_translated import get_translated
from src.handlers.handle_message import respond, get_updates


async def handler(message):
    if "update_id" not in message:
        return None

    offset = message["update_id"] + 1

    if 'callback_query' in message:
        chat_id = message['callback_query']["message"]["chat"]["id"]
        return await get_translated(offset, chat_id)

    if "message" not in message or "text" not in message["message"]:
        return offset

    chat_id = message["message"]["chat"]["id"]
    text = message["message"]["text"]
    name = message["message"]["from"]["username"]

    if text[0] == "/":
        await commands(chat_id, text)
    else:
        await respond(chat_id, text, name)

    return offset


async def main():
    offset = 0
    while True:
        try:
            updates_message = await get_updates(offset)
            if updates_message is None or "result" not in updates_message:
                logging.info("Получен пустой ответ от get_updates")
                await asyncio.sleep(5)
                continue

            for message in updates_message["result"]:
                new_offset = await handler(message)
                if new_offset:
                    offset = new_offset

        except Exception as e:
            logging.error(f"Ошибка в основном цикле: {e}")
            continue


if __name__ == "__main__":
    asyncio.run(main())
