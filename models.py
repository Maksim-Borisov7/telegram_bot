from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class UsersOrm(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)

    cnt: Mapped["CountOrm"] = relationship(back_populates="user")


class CountOrm(Base):
    __tablename__ = 'count_message'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    count: Mapped[int]
    fk_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))

    user: Mapped["UsersOrm"] = relationship(back_populates="cnt")
