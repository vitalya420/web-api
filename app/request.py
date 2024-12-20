from dataclasses import dataclass
from typing import Callable

from sanic import Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@dataclass
class RequestContext:
    session: AsyncSession
    session_maker: async_sessionmaker[AsyncSession]
    t: Callable


class AppRequest(Request):

    @staticmethod
    def make_context() -> RequestContext:
        return RequestContext()
