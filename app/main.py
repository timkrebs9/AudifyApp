import uvicorn
from fastapi import FastAPI
from fastapi import Form
from fastapi import Request
from fastapi import status
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    print("Request for index page received")
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/favicon.ico")
async def favicon() -> FileResponse:
    file_name = "favicon.ico"
    file_path = "./static/" + file_name
    return FileResponse(
        path=file_path, headers={"mimetype": "image/vnd.microsoft.icon"}
    )


@app.post("/hello", response_class=HTMLResponse, response_model=None)
async def hello(
    request: Request, name: str = Form(...)
) -> HTMLResponse | RedirectResponse:
    if name:
        print(f"Request for hello page received with name={name}")
        return templates.TemplateResponse(
            "hello.html", {"request": request, "name": name}
        )

    print(
        "Request for hello page received with no name or blank name -- \
            redirecting"
    )
    return RedirectResponse(
        request.url_for("index"), status_code=status.HTTP_302_FOUND
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
