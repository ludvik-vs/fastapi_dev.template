from pydantic import BaseSettings, AnyHttpUrl
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Dev Template"
    DEBUG: bool = True
    PORT: int = 8080
    ALLOWED_ORIGINS: List[AnyHttpUrl] = ["*"]

    class Config:
        env_file = ".env"

settings = Settings()
