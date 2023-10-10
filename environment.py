from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8")


class Variables(Settings):
    uri: str


@lru_cache()
def get_variables() -> Variables:
    return Variables()


variables = get_variables()
