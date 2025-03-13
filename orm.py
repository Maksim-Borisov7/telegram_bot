from models import UsersOrm, CountOrm


def insert_new_user(name, session):
    user = UsersOrm(name=name)
    cnt = CountOrm(count=1)
    user.cnt = cnt
    session.add(user)
    session.commit()


def increase_count(name, session):
    user = session.query(UsersOrm).filter(UsersOrm.name == name).scalar()
    cnt_record = user.cnt
    cnt_record.count += 1
    session.commit()


