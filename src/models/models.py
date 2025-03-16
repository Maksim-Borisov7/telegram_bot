from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)

    cnt: Mapped["Counts"] = relationship(back_populates="user")


class Counts(Base):
    __tablename__ = 'count_message'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    count: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))

    user: Mapped["Users"] = relationship(back_populates="cnt")
