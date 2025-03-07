import psycopg2
from config import HOST, USER, PASSWORD, DB_NAME, PORT
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def add_database(nickname):
    connection = None
    try:
        connection = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB_NAME,
            port=PORT
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT EXISTS(SELECT name FROM users_count WHERE name = '{nickname}')"""
            )
            res = cursor.fetchone()
            if res[0]:
                cursor.execute(
                    f"""UPDATE users_count
                    SET count_message = count_message + 1
                    WHERE name = '{nickname}'"""
                )
                logging.info("Увеличили счетчик сообщений")
            else:
                cursor.execute(
                    f"""INSERT INTO users_count (name, count_message) VALUES
                    ('{nickname}', 1);"""
                )
                logging.info("Добавлен новый пользователь")

    except Exception as ex:
        raise logging.critical("Не удалось подключиться к БД:", ex)

    finally:
        if connection:
            connection.close()
            logging.info("PostgreSQL connection closed")
