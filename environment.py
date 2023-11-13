from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8")

    def __init__(self):
        try:
            super().__init__()
        except ValidationError as exception:
            print(
                f"Error loading environment variables from .env file:\n{str(exception)}")
            exit(1)


class Variables(Settings):
    uri: str


@lru_cache()
def get_variables() -> Variables:
    return Variables()


variables = get_variables()
