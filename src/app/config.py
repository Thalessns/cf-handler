"""Configuration settings for the application."""
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    APP_HOST: str
    APP_PORT: int


app_config = AppConfig()
