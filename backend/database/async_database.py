import logging
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.orm import sessionmaker


class AsyncDatabase:
    def __init__(self, db_url: str) -> None:
        logging.exception("Database: initializing")
        self._engine = create_async_engine(db_url, echo=False)
        self._session_factory = sessionmaker(
            bind=self._engine,
            class_=AsyncSession,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )
        logging.exception("Database: initialization finished")

    @property
    def session_factory(
        self,
    ) -> Callable[..., AsyncSession]:
        return self._session_factory

    @property
    def engine(self) -> AsyncEngine:
        return self._engine
