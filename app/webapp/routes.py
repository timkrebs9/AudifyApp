from app.core.config import templates
from auth.dependencies import protected_endpoint
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import Response


webapp_router = APIRouter(tags=["Home"])


@webapp_router.get("/", response_class=HTMLResponse)
def home(request: Request) -> Response:
    return templates.TemplateResponse("index.html", {"request": request})


@webapp_router.get(
    "/profile",
    dependencies=[Depends(protected_endpoint)],
    response_class=HTMLResponse,
)
def profile(request: Request) -> Response:
    return templates.TemplateResponse(
        "profile.html",
        {"request": request, "userinfo": request.session["userinfo"]},
    )


# webapp_router = APIRouter(tags=["Home"])
#
#
# @webapp_router.get("/")
# def home(request: Request):
#    return templates.TemplateResponse("index.html", {"request": request})
#
#
# @webapp_router.get("/profile", dependencies=[Depends(protected_endpoint)])
# def profile(request: Request):
#    return templates.TemplateResponse(
#        "profile.html",
#        {"request": request, "userinfo": request.session["userinfo"]},
#    )
