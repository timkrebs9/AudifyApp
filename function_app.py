import azure.functions as func
from fastapi.staticfiles import StaticFiles
from WrapperFunction import app as fastapi_app
from starlette.middleware.sessions import SessionMiddleware

from config import config

app = fastapi_app
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key=config['WEBAPP']['SECRET_KEY'])

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)