import os
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote_plus

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()



class Settings(BaseSettings):
    # App
    APP_NAME: str = os.environ.get("APP_NAME", "FastAPI")
    DEBUG: bool = bool(os.environ.get("DEBUG", False))

    # FrontEnd Application
    FRONTEND_HOST: str = os.environ.get("FRONTEND_HOST", "http://localhost:3000")

    # MySql Database Config
    MYSQL_HOST: str = os.environ.get("MYSQL_HOST")
    MYSQL_USER: str = os.environ.get("MYSQL_USER")
    MYSQL_PASS: str = os.environ.get("MYSQL_PASSWORD")
    MYSQL_PORT: int = int(os.environ.get("MYSQL_PORT"))
    MYSQL_DB: str = os.environ.get("MYSQL_DB")
    DATABASE_URI: str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    
    
    # Logging env vars
    print(os.environ.get("MYSQL_HOST"))
    print(os.environ.get("MYSQL_USER"))
    print(os.environ.get("MYSQL_PASSWORD"))
    print(os.environ.get("MYSQL_PORT"))
    print(os.environ.get("MYSQL_DB"))
    

    # JWT Secret Key
    JWT_SECRET: str = os.environ.get(
        "JWT_SECRET"
    )
    JWT_ALGORITHM: str = os.environ.get("ACCESS_TOKEN_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 3)
    )
    REFRESH_TOKEN_EXPIRE_MINUTES: int = int(
        os.environ.get("REFRESH_TOKEN_EXPIRE_MINUTES", 1440)
    )

    # App Secret Key
    SECRET_KEY: str = os.environ.get(
        "SECRET_KEY"
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()