import psycopg2
from config import host, user, password, db_name, port


def add_database(nickname):
    connection = None
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=port
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
                print("Увеличили счетчик сообщений")
            else:
                cursor.execute(
                    f"""INSERT INTO users_count (name, count_message) VALUES
                    ('{nickname}', 1);"""
                )
                print("Добавлен новый пользователь")

    except Exception as ex:
        print("Не удалось подключиться к серверу:", ex)

    finally:
        if connection:
            connection.close()
            print("PostgreSQL connection closed")
