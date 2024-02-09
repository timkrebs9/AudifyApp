import logging
from urllib.parse import quote_plus
from urllib.parse import urlencode

from app.auth.config import oauth
from app.core.config import secrets
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.responses import Response


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

auth_router = APIRouter(tags=["Authentication"])


@auth_router.get("/login")
async def login(request: Request) -> Response:
    logger.info("Login attempt")
    if "id_token" not in request.session:
        logger.info("Redirecting to Auth0 for login")
        return await oauth.auth0.authorize_redirect(
            request,
            redirect_uri=request.url_for("callback"),
            audience=secrets["AUTH0_AUDIENCE"],
        )
    logger.info("User already logged in, redirecting to profile")
    return RedirectResponse(url=request.url_for("profile"))


@auth_router.get("/signup")
async def signup(request: Request) -> Response:
    logger.info("Signup attempt")
    if "id_token" not in request.session:
        logger.info("Redirecting to Auth0 for signup")
        return await oauth.auth0.authorize_redirect(
            request,
            redirect_uri=request.url_for("callback"),
            audience=secrets["AUTH0_AUDIENCE"],
            screen_hint="signup",
        )
    logger.info("User already signed up, sending empty response")
    return Response()


@auth_router.get("/logout")
def logout(request: Request) -> Response:
    logger.info("Logout attempt")
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
    logger.info("User logged out")
    return response


@auth_router.get("/callback")
async def callback(request: Request) -> Response:
    logger.info("Callback from Auth0")
    token = await oauth.auth0.authorize_access_token(request)
    request.session["access_token"] = token["access_token"]
    request.session["id_token"] = token["id_token"]
    request.session["userinfo"] = token["userinfo"]
    logger.info("User authenticated, redirecting to profile")
    return RedirectResponse(url=request.url_for("profile"))
