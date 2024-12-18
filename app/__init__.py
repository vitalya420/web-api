import os
from sanic import Sanic, text

app = Sanic("MyFuckingApp")

locales_dir = os.path.join(os.getcwd(), "locales")

from .middlewares import locale

from app.routes.users import users_bp

app.blueprint([users_bp])


@app.get("/")
async def index(request):
    return text(request.ctx.t("Hello World!"))
