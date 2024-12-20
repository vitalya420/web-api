from typing import Union
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession


class UserService:
    def __init__(
        self,
        session_or_factory: Union[
            async_sessionmaker[AsyncSession], AsyncSession, None
        ] = None,
    ):
        self.session_or_factory = session_or_factory

    @asynccontextmanager
    async def get_session(self):
        async with self.session_factory() as session:
            yield session

    async def get_user(self, id_or_phone: Union[int, str], *, raise_404=True):
        pass

    # Helper methods
    async def _get_user_by_id(self, id):
        pass

    async def _get_user_by_phone(self, phone):
        pass
