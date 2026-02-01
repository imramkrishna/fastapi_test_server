"""Application configuration settings."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""
    
    app_name: str = "FastAPI Test Server"
    app_version: str = "1.0.0"
    debug: bool = True
    
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
