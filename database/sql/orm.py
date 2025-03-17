from src.models.models import Users, Counts


def create_new_user(name, session):
    user = Users(name=name)
    cnt = Counts(count=1)
    user.cnt = cnt
    session.add(user)
    session.commit()


def read_users(session, user_id=None):
    if user_id:
        return session.query(Users).filter(Users.user_id == user_id)
    return session.query(Users).all()


def update_count(name, session):
    user = session.query(Users).filter(Users.name == name).scalar()
    cnt_record = user.cnt
    cnt_record.count += 1
    session.commit()


def delete_users(session, table):
    if table == Users:
        session.query(Users).delete()
    elif table == Counts:
        session.query(Counts).delete()

