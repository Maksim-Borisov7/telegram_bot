import logging

from faststream.rabbit import RabbitBroker
from config import settings
from src.handlers.send_message import Dispatch

broker = RabbitBroker()


@broker.subscriber('orders')
async def handle_orders(data: str):
    try:
        logging.info(f"Получено сообщение из RabbitMQ: {data}")
        chat_id = settings.CHAT_ID
        params = {"text": data, "chat_id": chat_id}
        await Dispatch.send_message_post(**params)
    except Exception as e:
        logging.error(f"Ошибка в broker: {e}")