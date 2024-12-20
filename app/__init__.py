import os
from sanic import Sanic, text

from .request import AppRequest

app = Sanic("MyFuckingApp", request_class=AppRequest)

locales_dir = os.path.join(os.getcwd(), "locales")

from .middlewares import locale

from app.routes.users import users_bp

app.blueprint([users_bp])


@app.get("/")
async def index(request):
    return text(request.ctx.t("Hello World!"))
