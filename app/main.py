import uvicorn
from app.auth.routes import auth_router
from app.core.config import secrets
from app.core.config import templates
from app.webapp.routes import webapp_router
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.add_middleware(SessionMiddleware, secret_key=secrets["WEBAPP_SECRET_KEY"])


app.include_router(webapp_router)
app.include_router(auth_router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    print("Request for index page received")
    return templates.TemplateResponse("home.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
