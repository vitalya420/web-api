from contextvars import ContextVar

from sanic import HTTPResponse, Request

from app.db import async_session_maker

_base_model_session_ctx = ContextVar("session")


async def inject_session(request: Request):
    request.ctx.session_maker = async_session_maker
    request.ctx.session = async_session_maker()
    request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)


async def close_session(request: Request, response: HTTPResponse):
    if hasattr(request.ctx, "session_ctx_token"):
        _base_model_session_ctx.reset(request.ctx.session_ctx_token)
        await request.ctx.session.close()
