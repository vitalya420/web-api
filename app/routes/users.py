from sanic import Blueprint, Request, json


users_bp = Blueprint("users", "/users")


@users_bp.get("/")
async def get_me(request: Request):
    _ = request.ctx.t
    return json({"success": True, "message": _("Get authorized user")})


@users_bp.put("/")
async def update_user(request: Request):
    _ = request.ctx.t
    return json({"success": True, "message": _("Update authorized user")})


@users_bp.delete("/")
async def delete_user(request: Request):
    _ = request.ctx.t
    return json({"success": True, "message": _("Delete authorized user")})


@users_bp.post("/auth")
async def auth_user(request: Request):
    _ = request.ctx.t
    return json({"success": True, "message": _("Authorize user")})


@users_bp.post("/register")
async def register_user(request: Request):
    _ = request.ctx.t
    return json({"success": True, "message": _("Register new user")})


@users_bp.post("/profile-picture")
async def update_profile_picture(request: Request):
    _ = request.ctx.t
    return json({"success": True, "message": _("Update user's profile picture")})


@users_bp.delete("/profile-picture")
async def delete_profile_picture(request: Request):
    _ = request.ctx.t
    return json({"success": True, "message": _("Delete user's profile picture")})
