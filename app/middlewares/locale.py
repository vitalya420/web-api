from sanic import Request

from app import app
from app.utils.utils import match_best_language
from app.translation import translations, SUPPORTED_LANGUAGES


@app.middleware("request")
async def set_translator(request: Request):
    accept_lang = request.headers.get("accept-language")

    lang = (
        SUPPORTED_LANGUAGES[0]
        if not accept_lang
        else match_best_language(accept_lang, SUPPORTED_LANGUAGES)
    )
    request.ctx.t = translations[lang].gettext
