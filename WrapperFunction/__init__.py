import azure.functions as func
from fastapi import FastAPI
from auth.routes import auth_router

from utils import to_pretty_json
from webapp.routes import webapp_router

app = FastAPI(
    title="FastAPI on Azure Functions",
    description="A sample project to demonstrate the use of FastAPI on Azure Functions.",
    version="0.1.0",

    openapi_tags=[
        {
            "name": "sample",
            "description": "Operations with sample data.",
        },
    ],
)

app.include_router(webapp_router)
app.include_router(auth_router)

