from sanic import Blueprint, Request, json

from app.request import AppRequest
from app.services.user_service import UserService


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


@users_bp.get("/<user_id_or_phone>")
async def get_user_by_id(request: AppRequest, user_id: str):
    user = UserService(request.ctx.session_factory).get_user(
        int(user_id) if user_id.isdigit() else user_id, raise_404=True
    )
    return json({"success": True, "message": "User found!"})
