from models import Users, Counts


def insert_new_user(name, session):
    user = Users(name=name)
    cnt = Counts(count=1)
    user.cnt = cnt
    session.add(user)
    session.commit()


def increase_count(name, session):
    user = session.query(Users).filter(Users.name == name).scalar()
    cnt_record = user.cnt
    cnt_record.count += 1
    session.commit()


