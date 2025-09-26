from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()