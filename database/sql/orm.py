import logging

from sqlalchemy import delete, select
from sqlalchemy.orm import selectinload

from src.models.models import Users, Counts


async def create_new_user(name, session):
    user = Users(name=name)
    cnt = Counts(count=1)
    user.cnt = cnt
    session.add(user)
    await session.commit()
    logging.info(f"Создан пользователь: {name}")


async def read_users(session, user_id=None):
    try:
        if user_id:
            result = await session.execute(
                select(Users)
                .where(Users.user_id == user_id)
                .options(selectinload(Users.cnt))
            )
            return result.scalar_one_or_none()

        result = await session.execute(
            select(Users).options(selectinload(Users.cnt)))
        return result.scalars().all()

    except Exception as e:
        logging.error(f"Ошибка при чтении пользователей: {e}")
        raise


async def update_count(name, session):
    try:
        result = await session.execute(
            select(Users)
            .where(Users.name == name)
            .options(selectinload(Users.cnt)))

        user = result.scalar_one_or_none()

        if user is None:
            logging.warning(f"Пользователь {name} не найден")
            return False

        if not hasattr(user, 'cnt') or user.cnt is None:
            logging.warning(f"У пользователя {name} нет счетчика")
            return False

        user.cnt.count += 1
        await session.commit()
        logging.info(f"Обновлен счетчик для {name}: {user.cnt.count}")
        return True

    except Exception as e:
        await session.rollback()
        logging.error(f"Ошибка при обновлении счетчика: {e}")


async def delete_users(session, table):
    if table == Users:
        await session.execute(delete(Users))
    elif table == Counts:
        await session.execute(delete(Counts))
    await session.commit()

