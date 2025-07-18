from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncSession:
        try:
            async with self.session_factory() as session:
                yield session
                await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


db = DatabaseHelper(
    url=settings.PG_URL,
    echo=settings.ECHO
)
