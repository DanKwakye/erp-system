from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    #Database
    DATABASE_URL: str

    #API SETTINGS
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Terra Foods EMS"

    #CORS
    BACKEND_CORS_ORIGINS: list = [
    "http://localhost:3000",
    "http://localhost:5173", 
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174"
]

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()