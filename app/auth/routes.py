from urllib.parse import quote_plus
from urllib.parse import urlencode

from app.auth.config import oauth
from app.core.config import secrets
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import RedirectResponse


auth_router = APIRouter(tags=["Authentication"])


@auth_router.get("/login")
async def login(request: Request) -> RedirectResponse:
    if "id_token" not in request.session:
        return await oauth.auth0.authorize_redirect(
            request, redirect_uri=request.url_for("callback"), audience=""
        )
    return RedirectResponse(url=request.url_for("profile"))


@auth_router.get("/signup")
async def signup(request: Request) -> RedirectResponse:
    if "id_token" not in request.session:
        return await oauth.auth0.authorize_redirect(
            request,
            redirect_uri=request.url_for("callback"),
            audience="",
            screen_hint="signup",
        )
    return RedirectResponse(url=request.url_for("profile"))


@auth_router.get("/logout")
def logout(request: Request) -> RedirectResponse:
    response = RedirectResponse(
        url="https://"
        + secrets["AUTH0_DOMAIN"]
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": request.url_for("home"),
                "client_id": secrets["AUTH0_CLIENT_ID"],
            },
            quote_via=quote_plus,
        )
    )
    request.session.clear()
    return response


@auth_router.get("/callback")
async def callback(request: Request) -> RedirectResponse:
    """
    Callback redirect from Auth0
    """
    token = await oauth.auth0.authorize_access_token(request)
    # Store `access_token`, `id_token`, and `userinfo` in session
    request.session["access_token"] = token["access_token"]
    request.session["id_token"] = token["id_token"]
    request.session["userinfo"] = token["userinfo"]
    return RedirectResponse(url=request.url_for("profile"))
