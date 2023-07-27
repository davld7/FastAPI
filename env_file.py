from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    mongodb_uri: str

    class Config:
        env_file = "file.env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
