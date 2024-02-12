from app.core.config import templates
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse


webapp_router = APIRouter(tags=["Home"])


@webapp_router.get("/profile")
def profile(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "profile.html",
        {"request": request, "userinfo": request.session["userinfo"]},
    )
