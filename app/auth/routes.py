# from urllib.parse import quote_plus, urlencode

from app.core.config import templates
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse


# from fastapi.responses import RedirectResponse


auth_router = APIRouter(tags=["Authentication"])


@auth_router.get("/login")
async def login(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("home.html", {"request": request})


@auth_router.get("/signup")
async def signup(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("home.html", {"request": request})


@auth_router.get("/logout")
def logout(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("home.html", {"request": request})
