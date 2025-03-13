from sqlalchemy import create_engine, select, exists
from config import USER, PASSWORD, HOST, PORT, DB_NAME
from sqlalchemy.orm import sessionmaker
from orm import insert_new_user, increase_count
from models import UsersOrm, Base
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

engine = create_engine(url=f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}", echo=True)
session_factory = sessionmaker(engine)
Base.metadata.create_all(engine, checkfirst=True)


def add_to_database(nickname):
    try:
        query = select(exists().where(UsersOrm.name == nickname))
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













