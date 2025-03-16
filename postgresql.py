from sqlalchemy import create_engine, select, exists
from config import PG_URL, BOT_URL
from sqlalchemy.orm import sessionmaker, Session
from orm import insert_new_user, increase_count
from models import Users, Base
import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

engine = create_engine(url=PG_URL, echo=True)
session_factory = sessionmaker(engine)
Base.metadata.create_all(engine, checkfirst=True)


def add_message_to_database(nickname):
    try:
        query = select(exists().where(Users.name == nickname))
        with session_factory() as session:
            if session.execute(query).scalar():
                increase_count(nickname, session)
                logging.info("Увеличили счетчик сообщений")
            else:
                insert_new_user(nickname, session)
                logging.info("Добавлен новый пользователь")

    except Exception as ex:
        logging.critical(f"Не удалось подключиться к БД: {ex}")
        raise ex


def get_all_users(chat_id):
    session_users = Session(engine)
    try:
        with session_users as session:
            users_all = session.query(Users).all()
            lst = []
            for value in users_all:
                lst.append(f"Пользователь: {value.name}; Количество сообщений: {value.cnt.count}\n")
            params = {
                "chat_id": chat_id,
                "text": "".join(lst)
            }
            requests.post(BOT_URL + "sendMessage", params=params)
    except Exception as e:
        logging.error(f"Ошибка при получении данных из базы данных: {e}")
        raise e














