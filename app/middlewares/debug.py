from app.request import AppRequest


async def debug_middleware(request: AppRequest):
    # Middleware for debugging.
    # Caclulate request proceed time (user time and cpu time)
    # make sure it has highest priority (1)
    # register this middleware if debug if on
    pass
