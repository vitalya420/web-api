from typing import overload

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

class UserService:
    @overload
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        """
        Creates service with a new session
        """
        self.session_factory: async_sessionmaker[AsyncSession] = session_factory

    @overload
    def __init__(self, session: AsyncSession):
        """
        Creates service but reuses session. For example if there is running transaction
        """
        self.session = session

    @overload
    async def get_user(self, id: int, *, raise_404: bool = False):
        """Get user by it's id

        Args:
            id (int): User's id
        """

    @overload
    async def get_user(self, phone_number: str, *, raise_404: bool = False):
        """Get user by it's phone number

        Args:
            id (int): User's phone number
        """
