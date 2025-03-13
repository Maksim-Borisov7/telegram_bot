from sqlalchemy import create_engine
from config import USER, PASSWORD, HOST, PORT, DB_NAME
from sqlalchemy.orm import Session
from models import UsersOrm
import requests
from config import BOT_URL


def get_all_users(chat_id):
    engine = create_engine(url=f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}", echo=True)
    session = Session(engine)
    users_all = session.query(UsersOrm).all()
    lst = []
    for value in users_all:
        lst.append(f"Пользователь: {value.name}; Количество сообщений: {value.cnt.count}\n")
    params = {
        "chat_id": chat_id,
        "text": "".join(lst)
    }
    requests.post(BOT_URL + "sendMessage", params=params)
    session.close()
