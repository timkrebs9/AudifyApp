from auth.routes import auth_router
from webapp.routes import webapp_router
from storage.routes import storage_router
from config import app


app.include_router(webapp_router)
app.include_router(auth_router)
app.include_router(storage_router)

def main():
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

if __name__ == '__main__':
    main()