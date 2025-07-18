import aiohttp
from sqlalchemy import select, exists
from config import settings
from database.sql.orm import create_new_user, update_count, read_users
from src.models.models import Users
from .db_helper import db
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


async def add_message_to_database(nickname):
    try:
        async with db.get_session() as session:
            query = select(exists().where(Users.name == nickname))
            result = await session.execute(query)
            user_exists = result.scalar_one_or_none() is not None

            if not user_exists:
                await create_new_user(session, nickname)
                await session.commit()
                logging.info(f"Добавлен новый пользователь: {nickname}")
            else:
                await update_count(nickname, session)
                logging.info(f"Увеличили счетчик сообщений для пользователя: {nickname}")

    except Exception as e:
        logging.error(f"Не удалось подключиться к БД: {e}")
        raise


async def get_all_users(chat_id):
    try:
        async with db.get_session() as session:
            users_all = await read_users(session)
            lst = []
            for value in users_all:
                lst.append(f"Пользователь: {value.name}; Количество сообщений: {value.cnt.count}\n")
            params = {
                "chat_id": chat_id,
                "text": "".join(lst)
            }
            async with aiohttp.ClientSession() as s:
                async with s.post(settings.BOT_URL + "sendMessage", params=params) as response:
                    await response.json()

    except Exception as e:
        logging.error(f"Ошибка при получении данных из базы данных: {e}")
        raise e












